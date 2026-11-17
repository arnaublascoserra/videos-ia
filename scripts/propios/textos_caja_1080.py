# Textos estilo TikTok (caja blanca redondeada, letra negra) sobre vídeo 1080x1920.
# Uso: python3 textos_caja_1080.py entrada.mp4 salida.mp4 '[[inicio,fin,"línea1|línea2","emoji",y_px],...]'
import sys,json,subprocess,tempfile,os
from PIL import Image,ImageDraw,ImageFont
src,dst,spec=sys.argv[1],sys.argv[2],json.loads(sys.argv[3])
F=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Bold.otf',52)
EF=ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf',109)
def emoji(ch,size=54):
    chars=[c for c in ch if not 0xFE00<=ord(c)<=0xFE0F]
    out=[]
    for c in chars:
        im=Image.new('RGBA',(160,160),(0,0,0,0));ImageDraw.Draw(im).text((10,10),c,font=EF,embedded_color=True)
        bb=im.getbbox();im=im.crop(bb).resize((size,size));out.append(im)
    w=sum(i.width for i in out)+4*(len(out)-1);e=Image.new('RGBA',(w,size),(0,0,0,0));x=0
    for i in out:e.alpha_composite(i,(x,0));x+=i.width+4
    return e
tmp=tempfile.mkdtemp();pngs=[]
for k,(a,b,txt,emo,y) in enumerate(spec):
    lines=txt.split('|');lay=Image.new('RGBA',(1080,1920),(0,0,0,0));d=ImageDraw.Draw(lay)
    e=emoji(emo) if emo else None;lh=70
    widths=[d.textlength(l,font=F)+((e.width+14) if (e and i==len(lines)-1) else 0) for i,l in enumerate(lines)]
    W=max(widths)+64;H=lh*len(lines)+36;x0=(1080-W)//2
    d.rounded_rectangle((x0,y,x0+W,y+H),radius=26,fill=(255,255,255,245))
    for i,l in enumerate(lines):
        lx=(1080-widths[i])//2;ly=y+18+i*lh
        d.text((lx,ly),l,font=F,fill=(0,0,0,255))
        if e and i==len(lines)-1: lay.alpha_composite(e,(int(lx+d.textlength(l,font=F)+14),ly+6))
    p=os.path.join(tmp,'t%d.png'%k);lay.save(p);pngs.append((a,b,p))
cmd=['ffmpeg','-v','error','-y','-i',src]
for a,b,p in pngs: cmd+=['-i',p]
fc='';last='[0:v]'
for k,(a,b,p) in enumerate(pngs):
    out='[v%d]'%k;fc+=f"{last}[{k+1}:v]overlay=0:0:enable='between(t,{a},{b})'{out};";last=out
cmd+=['-filter_complex',fc.rstrip(';'),'-map',last,'-c:v','libx264','-crf','20','-preset','veryfast','-pix_fmt','yuv420p','-an',dst]
subprocess.run(cmd,check=True,stdin=subprocess.DEVNULL);print('ok',dst)
