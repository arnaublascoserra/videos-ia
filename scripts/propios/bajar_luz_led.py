import cv2,numpy as np,sys
src,dst=sys.argv[1],sys.argv[2]
cap=cv2.VideoCapture(src); fps=cap.get(5); w=int(cap.get(3)); h=int(cap.get(4))
out=cv2.VideoWriter(dst,cv2.VideoWriter_fourcc(*'MJPG'),fps,(w,h))
while True:
  ok,f=cap.read()
  if not ok: break
  hsv=cv2.cvtColor(f,cv2.COLOR_BGR2HSV).astype(np.float32)
  H,S,V=hsv[...,0],hsv[...,1],hsv[...,2]
  warm=((H<=35)|(H>=165)).astype(np.float32)
  s=np.clip((S-100)/80,0,1)*np.clip((V-150)/60,0,1)*warm
  s=cv2.dilate(s,np.ones((3,3),np.uint8)); s=cv2.GaussianBlur(s,(0,0),2.5)
  H2=np.where(s>0.2, np.where(H<=35, H*(1-0.6*s), H), H)  # pull yellow toward red
  hsv[...,0]=H2; hsv[...,2]=V*(1-0.42*s); hsv[...,1]=S*(1-0.1*s)
  out.write(cv2.cvtColor(hsv.clip(0,255).astype(np.uint8),cv2.COLOR_HSV2BGR))
out.release()
