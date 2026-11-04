def t(s):  # "ss:ff" a 30 fps
    a,b=s.split(':'); return int(a)+int(b)/30
segs=[(0.38,3.51,"okay, this is my new 10-minute ritual for tired eyes"),
(4.17,5.08,"long press"),
(5.43,9.37,"and this soft red light sits right under my eyes"),
(9.97,12.10,"red light plus gentle microcurrents"),
(12.50,14.64,"and it turns off by itself after 10 minutes"),
(15.76,17.61,"I literally look like a different person"),
(17.89,19.15,"like I slept straight through the night"),
(20.16,21.58,"link in bio if you want to try them")]
def ts(x): return f"0:{int(x//60):02d}:{x%60:05.2f}"
head="""[Script Info]
ScriptType: v4.00+
PlayResX: 480
PlayResY: 854
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: S,Poppins,28,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,2.5,1,2,50,50,110,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
open('subs_final_en.ass','w').write(head+"\n".join(f"Dialogue: 0,{ts(a)},{ts(b)},S,,0,0,0,,{x}" for a,b,x in segs)+"\n")
