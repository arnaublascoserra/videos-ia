import cv2,numpy as np,sys
src,dst,dbg=sys.argv[1:4]
cap=cv2.VideoCapture(src);fps=cap.get(5);fr=[]
while True:
  ok,f=cap.read()
  if not ok:break
  fr.append(f)
n=len(fr);segs=[(0,147),(147,n)]
masks=np.zeros((n,)+fr[0].shape[:2],np.uint8)
for a,b in segs:
  s=np.stack(fr[a:b]).astype(np.int16)
  hsv=np.stack([cv2.cvtColor(f,cv2.COLOR_BGR2HSV) for f in fr[a:b]])
  g=s.mean(3);mn=g.min(0);sd=g.std(0)
  # text fill: white (low sat, very bright) or yellow (hue~25-35, high sat), stable in segment
  white=(mn>200)&(sd<12)&(hsv[...,1].max(0)<70)
  yel=(hsv[...,0].min(0)>18)&(hsv[...,0].max(0)<40)&(hsv[...,1].min(0)>120)&(hsv[...,2].min(0)>170)
  fill=(white|yel).astype(np.uint8)
  emo=((hsv[...,0].max(0)<40)&(hsv[...,1].min(0)>80)&(hsv[...,2].min(0)>120)&(sd<15)).astype(np.uint8)
  emo[:150]=0;emo[300:]=0;emo[:, :300]=0
  # dark outline stable
  dark=((g.max(0)<70)&(sd<12)).astype(np.uint8)
  near=cv2.dilate(dark,np.ones((5,5),np.uint8))
  t=((fill&near)|emo).astype(np.uint8)
  dk=((g.max(0)<90)&(sd<10)).astype(np.uint8);dk[:150]=0;dk[300:]=0
  num2,lab2,st2,_=cv2.connectedComponentsWithStats(dk)
  for i in range(1,num2):
    if st2[i,4]<400: t[lab2==i]=1
  # keep only connected comps that are small (letters), drop big blobs (skin, glasses)
  num,lab,st,_=cv2.connectedComponentsWithStats(cv2.dilate(t,np.ones((3,3),np.uint8)))
  keep=np.zeros_like(t)
  for i in range(1,num):
    if st[i,4]<4000: keep[lab==i]=1
  # grow to cover outline: letters + outline radius
  m=cv2.dilate(keep,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,15)))
  # restrict to rows where text lives
  rows=np.zeros_like(m);rows[150:300]=1;rows[640:790]=1;m=m*rows*255
  masks[a:b]=m
  cv2.imwrite(dbg+'_%d.png'%a,m)
def blend(f,m):
  r=cv2.inpaint(f,m,9,cv2.INPAINT_NS)
  r=cv2.GaussianBlur(r,(0,0),2.5)
  noise=np.random.normal(0,4,f.shape).astype(np.float32)
  r=np.clip(r.astype(np.float32)+noise,0,255).astype(np.uint8)
  a=cv2.GaussianBlur((m>0).astype(np.float32),(0,0),3)[...,None]
  return (f*(1-a)+r*a).astype(np.uint8)
h,w=fr[0].shape[:2];out=cv2.VideoWriter(dst,cv2.VideoWriter_fourcc(*'MJPG'),fps,(w,h))
for i,f in enumerate(fr): out.write(blend(f,masks[i]))
out.release();print(n)
