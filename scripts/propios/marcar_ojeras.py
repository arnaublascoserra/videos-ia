"""Marca las ojeras de una IMAGEN, gratis. YuNet detecta la cara; bajo cada ojo resta luz de forma
uniforme (igual en los dos lados) en una media luna que cubre la bolsa, conservando toda la textura,
y le da un tono marrón grisáceo leve.
Uso: python marcar_ojeras.py yunet.onnx entrada.jpg salida.jpg D(puntos de luz, p.ej. 8-16)"""
import cv2,numpy as np,sys
model,src,dst,D=sys.argv[1],sys.argv[2],sys.argv[3],float(sys.argv[4])
f=cv2.imread(src); H,W=f.shape[:2]
det=cv2.FaceDetectorYN.create(model,'',(W,H),0.6); _,faces=det.detect(f)
fc=max(faces,key=lambda r:r[2]*r[3]); x,y,w,h=fc[:4]; eyes=[fc[4:6],fc[6:8]]
lab=cv2.cvtColor(f,cv2.COLOR_BGR2LAB).astype(np.float32)
sh=np.zeros((H,W),np.float32)
for ex,ey in eyes:
  cv2.ellipse(sh,(int(ex),int(ey+0.04*h)),(int(0.12*w),int(0.11*h)),0,0,180,1,-1)
  cv2.ellipse(sh,(int(ex),int(ey)),(int(0.085*w),int(0.038*h)),0,0,360,0,-1)
sh=cv2.GaussianBlur(sh,(0,0),0.025*w); sh/=sh.max()
lab[...,0]-=D*sh
lab[...,1]+=0.05*D*sh
lab[...,2]+=0.04*D*sh
cv2.imwrite(dst,cv2.cvtColor(np.clip(lab,0,255).astype(np.uint8),cv2.COLOR_LAB2BGR),[cv2.IMWRITE_JPEG_QUALITY,95])
print('ok')
