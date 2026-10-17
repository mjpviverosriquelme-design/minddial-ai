import os, sqlite3, uuid, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Header
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from ml import predict, BASE, KEYS

app=FastAPI(title='MindDial AI - Human Review',version='0.2')
DB=Path(os.getenv('MINDDIAL_DB',str(BASE/'reviews.sqlite3')))
TOKEN=os.getenv('MINDDIAL_REVIEW_TOKEN','')
MAX_BYTES=8*1024*1024

def connect():
    db=sqlite3.connect(DB)
    db.execute('PRAGMA foreign_keys=ON')
    db.execute('CREATE TABLE IF NOT EXISTS evaluations (id TEXT PRIMARY KEY, image_hash TEXT NOT NULL, prediction TEXT NOT NULL, demographics TEXT, created_at TEXT NOT NULL)')
    db.execute('CREATE TABLE IF NOT EXISTS reviews (id TEXT PRIMARY KEY, evaluation_id TEXT NOT NULL, corrected TEXT NOT NULL, reviewer_note TEXT, created_at TEXT NOT NULL, FOREIGN KEY(evaluation_id) REFERENCES evaluations(id))')
    return db
with connect(): pass

@app.get('/')
def home(): return FileResponse(BASE/'static'/'index.html')

@app.post('/api/evaluate')
async def evaluate(image:UploadFile=File(...), age:Optional[int]=Form(None), gender:str=Form('prefer_not_to_say'), ethnicity:str=Form('prefer_not_to_say'), research_consent:bool=Form(False)):
    if image.content_type not in ('image/png','image/jpeg','image/webp'): raise HTTPException(415,'Formato no permitido')
    if age is not None and not (18<=age<=120): raise HTTPException(422,'Edad fuera del rango admitido para este prototipo (18–120)')
    if gender not in ('woman','man','nonbinary','self_described','prefer_not_to_say'): raise HTTPException(422,'Género inválido')
    if ethnicity not in ('hispanic_latino','white','black','asian','indigenous','middle_eastern','multiracial','other','prefer_not_to_say'): raise HTTPException(422,'Etnia inválida')
    data=await image.read(MAX_BYTES+1)
    if len(data)>MAX_BYTES: raise HTTPException(413,'Imagen demasiado grande')
    try: result=predict(data)
    except ValueError as e: raise HTTPException(400,str(e))
    except RuntimeError as e: raise HTTPException(503,str(e))
    eid=str(uuid.uuid4()); result['evaluation_id']=eid;result['review_status']='pending'
    # Demographic fields are stored only when the participant explicitly consents.
    demographic=json.dumps({'age':age,'gender':gender,'ethnicity':ethnicity}) if research_consent else None
    with connect() as db:
        db.execute('INSERT INTO evaluations VALUES (?,?,?,?,?)',(eid,hashlib.sha256(data).hexdigest(),json.dumps(result),demographic,datetime.now(timezone.utc).isoformat()))
    return result

class Review(BaseModel):
    evaluation_id:str
    scores:list[int]=Field(min_length=4,max_length=4)
    note:str=Field(default='',max_length=1000)

@app.post('/api/review')
def review(body:Review,x_review_token:str|None=Header(default=None)):
    if not TOKEN: raise HTTPException(503,'Configura MINDDIAL_REVIEW_TOKEN')
    if x_review_token!=TOKEN: raise HTTPException(403,'Revisor no autorizado')
    if any(s not in (0,1) for s in body.scores): raise HTTPException(422,'Las puntuaciones deben ser 0 o 1')
    with connect() as db:
        row=db.execute('SELECT id FROM evaluations WHERE id=?',(body.evaluation_id,)).fetchone()
        if not row: raise HTTPException(404,'Evaluación inexistente')
        db.execute('INSERT INTO reviews VALUES (?,?,?,?,?)',(str(uuid.uuid4()),body.evaluation_id,json.dumps(dict(zip(KEYS,body.scores))),body.note,datetime.now(timezone.utc).isoformat()))
    total=sum(body.scores)
    return {'saved':True,'review_status':'human_validated','human_total':total,'human_result':'PASS' if total>=3 else 'FAIL','retraining':'pending_offline_validation'}