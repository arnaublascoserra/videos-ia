# Uso: python bajar_luz_led_fuerte.py entrada salida [kv=0.6] [ks=0.35]
# Versión más fuerte de bajar_luz_led.py para primeros planos del producto encendido:
# baja brillo (kv) y saturación (ks) del rojo/naranja intenso y también del halo rosado alrededor.
import cv2,numpy as np,sys
src,dst=sys.argv[1],sys.argv[2]
kv=float(sys.argv[3]) if len(sys.argv)>3 else 0.6
ks=float(sys.argv[4]) if len(sys.argv)>4 else 0.35
cap=cv2.VideoCapture(src); fps=cap.get(5); w=int(cap.get(3)); h=int(cap.get(4))
out=cv2.VideoWriter(dst,cv2.VideoWriter_fourcc(*'MJPG'),fps,(w,h))
while True:
  ok,f=cap.read()
  if not ok: break
  hsv=cv2.cvtColor(f,cv2.COLOR_BGR2HSV).astype(np.float32)
  H,S,V=hsv[...,0],hsv[...,1],hsv[...,2]
  warm=((H<=30)|(H>=160)).astype(np.float32)
  core=np.clip((S-90)/70,0,1)*np.clip((V-130)/60,0,1)*warm
  halo=np.clip((S-35)/60,0,1)*np.clip((V-150)/60,0,1)*warm*0.6
  s=np.maximum(core,halo)
  s=cv2.GaussianBlur(cv2.dilate(s,np.ones((3,3),np.uint8)),(0,0),2.5)
  H2=np.where(s>0.2, np.where(H<=30, H*(1-0.6*s), H), H)
  hsv[...,0]=H2; hsv[...,2]=V*(1-kv*s); hsv[...,1]=S*(1-ks*s)
  out.write(cv2.cvtColor(hsv.clip(0,255).astype(np.uint8),cv2.COLOR_HSV2BGR))
out.release(); print('ok',dst)
