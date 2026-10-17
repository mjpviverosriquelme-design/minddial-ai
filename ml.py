"""MindDial: inference and feature extraction. Predictions are screening demonstrations, not diagnoses."""
from pathlib import Path
import cv2, numpy as np, joblib
from skimage.feature import hog
BASE=Path(__file__).resolve().parent
NAMES=['Closed circle','All 12 numbers','Correct number placement','Hands pointing to 11 and 2']
KEYS=['circle','numbers','placement','hands']

def features(data):
    arr=np.frombuffer(data,dtype=np.uint8)
    gray=cv2.imdecode(arr,cv2.IMREAD_GRAYSCALE)
    if gray is None: raise ValueError('La imagen no se puede interpretar')
    # Consistent preprocessing shared by training and inference
    gray=cv2.resize(gray,(128,128),interpolation=cv2.INTER_AREA)
    gray=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8)).apply(gray)
    return hog(gray,orientations=9,pixels_per_cell=(8,8),cells_per_block=(2,2),block_norm='L2-Hys').astype('float32')

# Each criterion has its own independently replaceable prediction function.
# A replacement must include its matching preprocessing and be validated before activation.
def _run_model(key, data):
    path=BASE/'models'/f'{key}.joblib'
    if not path.exists():
        raise RuntimeError(f'Missing trained model: {path.name}')
    model=joblib.load(path)
    x=features(data).reshape(1,-1)
    if getattr(model,'n_features_in_',x.shape[1]) != x.shape[1]:
        raise RuntimeError(f'Incompatible features for {key}; use its original preprocessing')
    score=int(model.predict(x)[0])
    if score not in (0,1): raise RuntimeError(f'Invalid score from {key}')
    confidence=None
    if hasattr(model,'predict_proba'):
        classes=list(model.classes_)
        confidence=float(model.predict_proba(x)[0,classes.index(score)])
    return score,confidence

def predict_circle(data): return _run_model('circle',data)
def predict_numbers(data): return _run_model('numbers',data)
def predict_placement(data): return _run_model('placement',data)
def predict_hands(data): return _run_model('hands',data)

PREDICTORS={
    'circle':predict_circle,
    'numbers':predict_numbers,
    'placement':predict_placement,
    'hands':predict_hands,
}

def predict(data):
    outputs=[]
    for key,name in zip(KEYS,NAMES):
        score,confidence=PREDICTORS[key](data)
        outputs.append({'key':key,'name':name,'score':score,'confidence':confidence})
    total=sum(item['score'] for item in outputs)
    return {'criteria':outputs,'total':total,'result':'PASS' if total>=3 else 'FAIL',
            'notice':'Research prototype only. This result is not a medical diagnosis.'}
