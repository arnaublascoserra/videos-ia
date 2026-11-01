import cv2,numpy as np,sys
src,dst=sys.argv[1],sys.argv[2]
cap=cv2.VideoCapture(src); fps=cap.get(5); fr=[]
while True:
  ok,f=cap.read()
  if not ok: break
  fr.append(f)
mn=np.stack([cv2.cvtColor(f,cv2.COLOR_BGR2GRAY) for f in fr]).min(0)
m=np.zeros(mn.shape,np.uint8); b=(slice(215,360),slice(95,625))
m[b]=(mn[b]>185).astype(np.uint8)*255; m[285:355,438:512]=255
m=cv2.dilate(m,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(17,17)),1)
h,w=m.shape; out=cv2.VideoWriter(dst,cv2.VideoWriter_fourcc(*'MJPG'),fps,(w,h))
for f in fr: out.write(cv2.inpaint(f,m,5,cv2.INPAINT_NS))
out.release(); print(len(fr), int(m.sum()/255))
