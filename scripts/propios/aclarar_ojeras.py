"""Aclara las ojeras de un vídeo, gratis: detecta la cara con YuNet (OpenCV) y sube la luz
solo de los píxeles bajo los ojos que están más oscuros que la mejilla, manteniendo la textura.
Uso: python aclarar_ojeras.py yunet.onnx entrada.mp4 salida.avi fuerza(0-1) [--frames t1,t2 prefijo]"""
import cv2,numpy as np,sys
model,src,dst,k=sys.argv[1],sys.argv[2],sys.argv[3],float(sys.argv[4])
cap=cv2.VideoCapture(src); fps=cap.get(5); W=int(cap.get(3)); H=int(cap.get(4))
det=cv2.FaceDetectorYN.create(model,'',(W,H),0.6)
out=cv2.VideoWriter(dst,cv2.VideoWriter_fourcc(*'MJPG'),fps,(W,H)); prev=None; n=0
while True:
  ok,f=cap.read()
  if not ok: break
  _,faces=det.detect(f)
  if faces is not None and len(faces):
    fc=max(faces,key=lambda r:r[2]*r[3]); cur=np.array(fc[:14],float)
    prev=cur if prev is None else 0.6*prev+0.4*cur
  if prev is None: out.write(f); n+=1; continue
  x,y,w,h=prev[:4]; eyes=[prev[4:6],prev[6:8]]
  lab=cv2.cvtColor(f,cv2.COLOR_BGR2LAB).astype(np.float32); L=lab[...,0]
  low=cv2.GaussianBlur(L,(0,0),5)
  mask=np.zeros((H,W),np.float32)
  hsv=cv2.cvtColor(f,cv2.COLOR_BGR2HSV); white=((hsv[...,2]>185)&(hsv[...,1]<45)).astype(np.uint8)
  white=cv2.dilate(white,np.ones((15,15),np.uint8))
  active=[]
  for ex,ey in eyes:
    cx,cy=int(ex),int(ey+0.24*h); r=max(4,int(0.04*w))
    em=np.zeros((H,W),np.uint8); cv2.ellipse(em,(int(ex),int(ey+0.115*h)),(int(0.145*w),int(0.072*h)),0,0,360,1,-1)
    frac=white[em>0].mean() if em.any() else 1
    cheekw=white[max(0,cy-r):cy+r,max(0,cx-r):cx+r].mean()
    active.append(frac<0.08 and cheekw<0.2)
  for (ex,ey),act in zip(eyes,active):
    if not act: continue
    c=(int(ex),int(ey+0.115*h)); ax=(int(0.145*w),int(0.072*h))
    cv2.ellipse(mask,c,ax,0,0,360,1,-1)
    # reference cheek brightness
    cx,cy=int(ex),int(ey+0.24*h); r=max(4,int(0.04*w))
    ref=np.median(low[max(0,cy-r):cy+r,max(0,cx-r):cx+r])
    reg=(mask>0)
    deficit=np.clip(ref-low,0,None)
    lab[...,0]=np.where(reg, L+k*deficit, L)
    # warm the purple/brown towards cheek colour
    for ch in (1,2):
      refc=np.median(cv2.GaussianBlur(lab[...,ch],(0,0),5)[max(0,cy-r):cy+r,max(0,cx-r):cx+r])
      lowc=cv2.GaussianBlur(lab[...,ch],(0,0),5)
      lab[...,ch]=np.where(reg, lab[...,ch]+0.6*k*(refc-lowc), lab[...,ch])
    mask[:]=0
  newf=cv2.cvtColor(np.clip(lab,0,255).astype(np.uint8),cv2.COLOR_LAB2BGR)
  # feathered blend
  m=np.zeros((H,W),np.float32)
  for (ex,ey),act in zip(eyes,active):
    if act: cv2.ellipse(m,(int(ex),int(ey+0.115*h)),(int(0.145*w),int(0.072*h)),0,0,360,1,-1)
  m=cv2.GaussianBlur(m,(0,0),max(3,0.02*w))[...,None]
  out.write((f*(1-m)+newf*m).astype(np.uint8)); n+=1
out.release(); print(n,'frames')
