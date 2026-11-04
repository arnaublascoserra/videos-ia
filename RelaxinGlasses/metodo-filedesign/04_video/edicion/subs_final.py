def t(s):  # "ss:ff" a 30 fps
    a,b=s.split(':'); return int(a)+int(b)/30
segs=[("00:07","03:10","este es mi ritual de 10 minutos para los ojos cansados"),
("03:20","05:02","mantengo pulsado"),
("05:03","07:20","y sale esta luz roja suave bajo los ojos"),
("08:20","10:12","luz roja y microcorrientes suaves"),
("10:19","12:17","y se apaga sola a los 10 minutos"),
("14:07","15:19","parezco otra persona"),
("15:25","18:12","como si hubiera dormido toda la noche del tirón"),
("18:26","21:23","tienes el enlace en mi perfil si quieres probarlas")]
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
open('subs_final.ass','w').write(head+"\n".join(f"Dialogue: 0,{ts(t(a))},{ts(t(b))},S,,0,0,0,,{x}" for a,b,x in segs)+"\n")
