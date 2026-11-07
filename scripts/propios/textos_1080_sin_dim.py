import cv2,numpy as np,subprocess,json,sys
from PIL import Image,ImageDraw,ImageFont,ImageFilter
W,H=720,1280
F=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Bold.otf',50)
EF=ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf',109)
def _emoji1(ch,size):
    im=Image.new('RGBA',(160,160),(0,0,0,0)); ImageDraw.Draw(im).text((10,10),ch,font=EF,embedded_color=True)
    im=im.crop(im.getbbox()); return im.resize((size,size),Image.LANCZOS)
def emoji_img(ch,size=54):
    chars=[c for c in ch if c not in '\ufe0f\u200d ']
    ims=[_emoji1(c,size) for c in chars]
    if len(ims)==1: return ims[0]
    out=Image.new('RGBA',(size*len(ims)+6*(len(ims)-1),size),(0,0,0,0))
    for i,im in enumerate(ims): out.alpha_composite(im,(i*(size+6),0))
    return out
def layer(text,emo,color=(255,255,255),y0=233):
    FP='/usr/share/fonts/opentype/inter/Inter-Bold.otf'
    lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay)
    e=emoji_img(emo) if emo else None; ew=(e.width+12) if e else 0
    if '|' in text:
        lines=[x.strip() for x in text.split('|') if x.strip()]
    else:
        f0=ImageFont.truetype(FP,50); lines=[];cur=''
        for w_ in text.split():
            t=(cur+' '+w_).strip()
            if d.textlength(t,font=f0)>600: lines.append(cur);cur=w_
            else: cur=t
        lines.append(cur)
    sz=50
    while True:
        Fl=ImageFont.truetype(FP,sz)
        if max(d.textlength(l,font=Fl)+(ew if k==len(lines)-1 else 0) for k,l in enumerate(lines))<=660 or sz<=30: break
        sz-=2
    if e and sz!=50: e=e.resize((max(1,int(e.width*sz/50)),max(1,int(e.height*sz/50))),Image.LANCZOS); ew=e.width+12
    y=y0; lh=int(sz*1.16)
    for i,l in enumerate(lines):
        last=(i==len(lines)-1)
        lw=d.textlength(l,font=Fl)+(ew if (last and e) else 0)
        x=(W-lw)/2
        d.text((x,y),l,font=Fl,fill=tuple(color)+(255,))
        if last and e: lay.alpha_composite(e,(int(x+d.textlength(l,font=Fl)+12),y+int(4*sz/50)))
        y+=lh
    a=np.array(lay)
    sh=np.array(Image.fromarray(a[...,3]).filter(ImageFilter.GaussianBlur(3))).astype(float)*0.55
    sh=np.roll(sh,(2,1),(0,1))/255.
    ta=a[...,3]/255.; A=ta+sh*(1-ta)
    rgb=a[...,:3].astype(float)*ta[...,None]
    col=np.where(A[...,None]>0,rgb/np.maximum(A[...,None],1e-6),0)
    return np.dstack([cv2.cvtColor(col.clip(0,255).astype(np.uint8),cv2.COLOR_RGB2BGR),(A*255).astype(np.uint8)])
def dim(f):
    hsv=cv2.cvtColor(f,cv2.COLOR_BGR2HSV).astype(np.float32);Hh,S,V=hsv[...,0],hsv[...,1],hsv[...,2]
    warm=((Hh<=12)|(Hh>=165)).astype(np.float32)
    s=np.clip((S-110)/80,0,1)*np.clip((V-140)/60,0,1)*warm
    s=cv2.GaussianBlur(cv2.dilate(s,np.ones((5,5),np.uint8)),(0,0),4)
    hsv[...,2]=V*(1-0.35*s); hsv[...,1]=S*(1-0.25*s)
    return cv2.cvtColor(hsv.clip(0,255).astype(np.uint8),cv2.COLOR_HSV2BGR)
src,out,spec=sys.argv[1],sys.argv[2],json.loads(sys.argv[3])
OW,OH=1080,1920
segs=[(x[0],x[1],cv2.resize(layer(x[2],x[3],x[4] if len(x)>4 else (255,255,255),x[5] if len(x)>5 else 233),(OW,OH),interpolation=cv2.INTER_LANCZOS4)) for x in spec]
rng=np.random.default_rng(0)
cap=cv2.VideoCapture(src);fps=cap.get(5);i=0
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{OW}x{OH}','-r',str(fps),'-i','-','-an','-c:v','libx264','-preset','medium','-crf','16','-pix_fmt','yuv420p',out],stdin=subprocess.PIPE)
while True:
    ok,f=cap.read()
    if not ok:break
    t=i/fps;i+=1
    f=cv2.resize(f,(OW,OH),interpolation=cv2.INTER_LANCZOS4)
    pass
    bl=cv2.GaussianBlur(f,(0,0),1.2); f=cv2.addWeighted(f,1.35,bl,-0.35,0)
    f=np.clip(f.astype(np.float32)+rng.normal(0,3.0,f.shape[:2])[...,None],0,255).astype(np.uint8)
    for a,b,L in segs:
        if a<=t<b:
            al=L[...,3:4]/255.; f=(L[...,:3]*al+f*(1-al)).astype(np.uint8)
    p.stdin.write(f.tobytes())
p.stdin.close();p.wait();print('ok',out)
