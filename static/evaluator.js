let pyodide=null;
let report=()=>{};
const $=()=>({set textContent(value){report(value)}});
async function loadPyodide(){const m=await import('https://cdn.jsdelivr.net/pyodide/v0.27.7/full/pyodide.mjs');return m.loadPyodide();}
async function preprocess(file){
 // Browser-native grayscale extraction; CLAHE is performed in Pyodide.
 const bitmap=await createImageBitmap(file);
 try{
   const canvas=document.createElement('canvas');
   if(bitmap.width*bitmap.height>16000000)throw Error('La imagen es demasiado grande. Usa una imagen de hasta 16 megapíxeles.');
   canvas.width=bitmap.width;canvas.height=bitmap.height;
   const ctx=canvas.getContext('2d',{willReadFrequently:true});
   ctx.fillStyle='#fff';ctx.fillRect(0,0,canvas.width,canvas.height);ctx.drawImage(bitmap,0,0);
   const rgba=ctx.getImageData(0,0,canvas.width,canvas.height).data;
   const gray=new Uint8Array(canvas.width*canvas.height);
   for(let i=0,j=0;i<rgba.length;i+=4,j++){
     gray[j]=Math.round(.299*rgba[i]+.587*rgba[i+1]+.114*rgba[i+2]);
   }
   return {gray,width:canvas.width,height:canvas.height};
 }finally{bitmap.close()}
}
async function boot(){
 if(pyodide)return pyodide;
 $('status').textContent='Loading Python scientific packages…';
 const runtime=await loadPyodide();
 await runtime.loadPackage(['numpy','scikit-learn','scikit-image','joblib']);
 runtime.runPython(`import numpy as np, joblib
from skimage.feature import hog
from skimage.transform import resize
from skimage.exposure import equalize_adapthist
def evaluate_gray(gray, width, height):
    img=np.asarray(gray,dtype=np.uint8).reshape(height,width)
    # Approximation of OpenCV INTER_AREA and CLAHE; browser parity is not yet established.
    img=resize(img,(128,128),order=1,anti_aliasing=True,preserve_range=True).astype(np.uint8)
    img=(equalize_adapthist(img,clip_limit=0.02,kernel_size=(16,16))*255).clip(0,255).astype(np.uint8)
    x=hog(img,orientations=9,pixels_per_cell=(8,8),cells_per_block=(2,2),block_norm='L2-Hys').astype('float32').reshape(1,-1)
    scores=[]
    for key in ('circle','numbers','placement','hands'):
        model=joblib.load('/tmp/'+key+'.joblib')
        if model.n_features_in_ != x.shape[1]:
            raise ValueError('Incompatible feature dimensions for '+key)
        scores.append(int(model.predict(x)[0]))
    return scores`);
 pyodide=runtime;
 return pyodide;
}

export async function evaluateDrawing(file,onProgress=()=>{}){
 report=onProgress;
 const py=await boot();
 report('Cargando los cuatro modelos…');
 for(const key of ['circle','numbers','placement','hands']){
  if(!py.FS.analyzePath('/tmp/'+key+'.joblib').exists){
   const response=await fetch(new URL('./models/'+key+'.joblib',import.meta.url));
   if(!response.ok)throw Error('No se pudo cargar el modelo '+key+' (HTTP '+response.status+')');
   py.FS.writeFile('/tmp/'+key+'.joblib',new Uint8Array(await response.arrayBuffer()));
  }
 }
 report('La IA está evaluando tu reloj…');
 const img=await preprocess(file);
 py.globals.set('input_gray',img.gray);py.globals.set('input_width',img.width);py.globals.set('input_height',img.height);
 let result;
 try{
  result=py.runPython('evaluate_gray(input_gray,input_width,input_height)');
  const scores=Array.from(result.toJs());
  if(scores.length!==4||scores.some(s=>s!==0&&s!==1))throw Error('Puntuaciones no válidas');
  return {scores,review_status:'not_reviewed',experimental:true,preprocessing:'browser approximation; parity unverified'};
 }finally{
  if(result)result.destroy();
  for(const key of ['input_gray','input_width','input_height'])py.globals.delete(key);
 }
}
