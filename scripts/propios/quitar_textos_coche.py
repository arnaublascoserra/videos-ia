import cv2,numpy as np,sys
src,dst=sys.argv[1],sys.argv[2]
cap=cv2.VideoCapture(src);fps=cap.get(5);fr=[]
while True:
  ok,f=cap.read()
  if not ok:break
  fr.append(f)
n=len(fr);g=np.stack([cv2.cvtColor(f,cv2.COLOR_BGR2GRAY) for f in fr]).astype(np.float32)
# segment boundaries by change in top band
band=g[:,140:270,:]
d=[np.abs(band[i]-band[i-1]).mean() for i in range(1,n)]
cuts=[0]+[i for i in range(1,n) if d[i-1]>12]+[n]
segs=[];prev=0
for c in cuts[1:]:
  if c-prev>8: segs.append((prev,c)); prev=c
  elif c==n and segs: segs[-1]=(segs[-1][0],n)
if prev<n and (not segs or segs[-1][1]<n): segs.append((prev,n))
print('segs',segs)
masks=np.zeros((n,)+g.shape[1:],np.uint8)
k=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))
for a,b in segs:
  s=g[a:b];sd=s.std(0);mx=s.min(0)
  m=np.zeros(g.shape[1:],np.uint8)
  # bright stable text (white or yellow) + dark outline around it
  t=((sd<10)&(mx>170)).astype(np.uint8)
  t[:140]=0;t[300:]=0
  t=cv2.dilate(t,k,1)*255
  masks[a:b]=np.maximum(masks[a:b],t)
# bubble (whole video)
bub=np.zeros(g.shape[1:],np.uint8);bub[648:768,56:332]=255
if len(sys.argv)<4: masks|=bub
h,w=g.shape[1:];out=cv2.VideoWriter(dst,cv2.VideoWriter_fourcc(*'MJPG'),fps,(w,h))
for i,f in enumerate(fr): out.write(cv2.inpaint(f,masks[i],7,cv2.INPAINT_TELEA))
out.release();print(n)
