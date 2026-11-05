import cv2,numpy as np,subprocess,sys
src,out,layer=sys.argv[1],sys.argv[2],sys.argv[3]
L=cv2.imread(layer,cv2.IMREAD_UNCHANGED); a=L[...,3].astype(np.float32)/255.
a=cv2.dilate(a,np.ones((5,5),np.uint8)); a=cv2.GaussianBlur(a,(0,0),1.5)
a=cv2.resize(a,(1080,1920),interpolation=cv2.INTER_LINEAR)[...,None]
cap=cv2.VideoCapture(src);fps=cap.get(5);rng=np.random.default_rng(0)
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s','1080x1920','-r',str(fps),'-i','-','-an','-c:v','libx264','-preset','medium','-crf','23','-pix_fmt','yuv420p','-movflags','+faststart',out],stdin=subprocess.PIPE)
while True:
    ok,f=cap.read()
    if not ok:break
    u=cv2.resize(f,(1080,1920),interpolation=cv2.INTER_LANCZOS4)
    bl=cv2.GaussianBlur(u,(0,0),1.2); e=cv2.addWeighted(u,1.35,bl,-0.35,0)
    e=np.clip(e.astype(np.float32)+rng.normal(0,3.0,e.shape[:2])[...,None],0,255)
    o=(e*(1-a)+u.astype(np.float32)*a).astype(np.uint8)
    p.stdin.write(o.tobytes())
p.stdin.close();p.wait();print('ok',out)
