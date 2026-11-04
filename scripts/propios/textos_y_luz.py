import cv2,numpy as np,subprocess,json,sys
from PIL import Image,ImageDraw,ImageFont,ImageFilter
W,H=720,1280
F=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Bold.otf',50)
EF=ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf',109)
def emoji_img(ch,size=54):
    im=Image.new('RGBA',(160,160),(0,0,0,0)); ImageDraw.Draw(im).text((10,10),ch,font=EF,embedded_color=True)
    im=im.crop(im.getbbox()); return im.resize((size,size),Image.LANCZOS)
def layer(text,emo):
    lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay)
    words=text.split(); lines=[];cur=''
    manual='|' in text
    e=emoji_img(emo) if emo else None; ew=(e.width+12) if e else 0
    for w_ in words:
        t=(cur+' '+w_).strip()
        if d.textlength(t,font=F)>600: lines.append(cur);cur=w_
        else: cur=t
    lines.append(cur)
    if manual: lines=[x.strip() for x in text.split('|')]
    if e and not manual and d.textlength(lines[-1],font=F)+ew>600: lines.append('')
    y=233
    for i,l in enumerate(lines):
        last=(i==len(lines)-1)
        lw=d.textlength(l,font=F)+(ew if (last and e) else 0)
        x=(W-lw)/2
        d.text((x,y),l,font=F,fill=(255,255,255,255))
        if last and e: lay.alpha_composite(e,(int(x+d.textlength(l,font=F)+(12 if l else 0)),y+4))
        y+=58
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
segs=[(a,b,layer(t,e)) for a,b,t,e in spec]
cap=cv2.VideoCapture(src);fps=cap.get(5);i=0
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(fps),'-i','-','-an','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',out],stdin=subprocess.PIPE)
while True:
    ok,f=cap.read()
    if not ok:break
    t=i/fps;i+=1
    f=cv2.resize(f,(W,H),interpolation=cv2.INTER_LANCZOS4)
    if 2.0<=t<=6.8: f=dim(f)
    for a,b,L in segs:
        if a<=t<b:
            al=L[...,3:4]/255.; f=(L[...,:3]*al+f*(1-al)).astype(np.uint8)
    p.stdin.write(f.tobytes())
p.stdin.close();p.wait();print('ok',out)
