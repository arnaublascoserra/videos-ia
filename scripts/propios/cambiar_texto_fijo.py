import cv2,numpy as np,subprocess,sys
from PIL import Image,ImageDraw,ImageFont,ImageFilter
ov=cv2.imread('text_overlay.png',cv2.IMREAD_UNCHANGED)
emo=ov[288:347,450:509].copy()
# capa nueva
W,H=720,1280
font=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Bold.otf',50)
lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay)
l1='Si tienes ojeras,'; l2='esto es para ti'
ew=emo.shape[1]; gap=12
w1=d.textlength(l1,font=font); w2=d.textlength(l2,font=font)+gap+ew
y1=233; y2=y1+55
d.text(((W-w1)/2,y1),l1,font=font,fill=(255,255,255,255))
x2=(W-w2)/2; d.text((x2,y2),l2,font=font,fill=(255,255,255,255))
a=np.array(lay)[...,3]
# sombra
sh=Image.fromarray(a).filter(ImageFilter.GaussianBlur(3))
sha=np.roll(np.array(sh).astype(float)*0.55,(2,1),(0,1))
rgb=np.zeros((H,W,3),float); A=np.zeros((H,W),float)
A=sha/255.
txt=np.array(lay)[...,:3].astype(float); ta=a/255.
rgb=txt*ta[...,None]; A2=ta+A*(1-ta)
# emoji (BGR->RGB)
ex=int(x2+d.textlength(l2,font=font)+gap); ey=y2+2
e=emo[...,[2,1,0]].astype(float); ea=emo[...,3]/255.
rgb[ey:ey+e.shape[0],ex:ex+ew]=e*ea[...,None]+rgb[ey:ey+e.shape[0],ex:ex+ew]*(1-ea[...,None])
A2[ey:ey+e.shape[0],ex:ex+ew]=ea+A2[ey:ey+e.shape[0],ex:ex+ew]*(1-ea)
col=np.where(A2[...,None]>0,rgb/np.maximum(A2[...,None],1e-6),0)
# donde solo hay sombra, color negro
col=np.where(ta[...,None]>0,col,col)
newl=np.dstack([col.clip(0,255),A2*255]).astype(np.uint8)
cv2.imwrite('texto_es_layer.png',cv2.cvtColor(newl,cv2.COLOR_RGBA2BGRA))
# mascara del texto viejo
old=(ov[...,3]>15).astype(np.uint8)
old=cv2.dilate(old,np.ones((7,7),np.uint8))
def proc(inp,out):
    cap=cv2.VideoCapture(inp); fps=cap.get(5)
    p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s','720x1280','-r',str(fps),'-i','-','-an','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',out],stdin=subprocess.PIPE)
    na=newl[...,3:4]/255.; nc=cv2.cvtColor(newl[...,:3],cv2.COLOR_RGB2BGR).astype(float)
    while True:
        ok,f=cap.read()
        if not ok: break
        top=f[150:420].copy()
        f[150:420]=cv2.inpaint(top,old[150:420],6,cv2.INPAINT_TELEA)
        f=(nc*na+f*(1-na)).astype(np.uint8)
        p.stdin.write(f.tobytes())
    p.stdin.close(); p.wait()
for a_,b_ in zip(sys.argv[1::2],sys.argv[2::2]): proc(a_,b_); print('ok',b_)
