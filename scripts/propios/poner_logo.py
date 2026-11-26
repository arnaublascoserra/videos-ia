"""Pone el logo (PNG con transparencia) sobre una imagen.
Uso: python poner_logo.py base.jpg logo.png salida.jpg cx cy ancho modo
modo=impreso -> se integra con la luz de la superficie (pedestal, expositor)
modo=marca   -> marca de agua pequeña, con halo blanco suave para leerse en cualquier fondo"""
import sys,numpy as np
from PIL import Image,ImageFilter
b,l,o=sys.argv[1:4];cx,cy,w=map(int,sys.argv[4:7]);modo=sys.argv[7]
base=Image.open(b).convert('RGB');logo=Image.open(l).convert('RGBA')
h=int(logo.height*w/logo.width);logo=logo.resize((w,h),Image.LANCZOS)
x0,y0=cx-w//2,cy-h//2
B=np.asarray(base).astype(np.float32)/255;L=np.asarray(logo).astype(np.float32)/255
reg=B[y0:y0+h,x0:x0+w];a=L[...,3:4];c=L[...,:3]
if modo=='impreso':
  lum=reg.mean(axis=2,keepdims=True);ref=np.percentile(lum,70)
  shade=np.clip(lum/ref,0.75,1.1)          # sombras y brillos de la superficie
  c=c*shade;a=a*0.95
else:
  halo=np.asarray(logo.split()[3].filter(ImageFilter.GaussianBlur(w*0.02))).astype(np.float32)[...,None]/255
  reg=reg*(1-halo*0.45)+1.0*halo*0.45; a=a*0.92
reg=reg*(1-a)+c*a
B[y0:y0+h,x0:x0+w]=reg
Image.fromarray((np.clip(B,0,1)*255).astype(np.uint8)).save(o,quality=95)
print('ok',o)
