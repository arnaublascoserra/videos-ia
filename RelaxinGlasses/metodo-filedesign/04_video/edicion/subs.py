# Frases con tramos de voz medidos (silencedetect)
segs = [
 (0.49, 3.48, "Este es mi ritual de 10 minutos para los ojos cansados."),
 (4.04, 7.76, "Mantengo pulsado y sale esta luz roja suave bajo los ojos."),
 (8.84, 10.51, "Luz roja y pulsos suaves,"),
 (10.87, 13.05, "y se apaga sola a los 10 minutos."),
 (14.53, 15.64, "Parezco otra persona,"),
 (16.16, 18.39, "como si hubiera dormido toda la noche del tirón."),
 (19.21, 21.58, "Tienes el enlace en mi perfil si quieres probarlas."),
]
def chunks(words, n=3):
    out, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) >= n or w.endswith((',', '.')):
            out.append(cur); cur = []
    if cur:
        if len(cur) == 1 and out: out[-1] += cur
        else: out.append(cur)
    return out
def ts(t):
    h=int(t//3600); m=int(t%3600//60); s=t%60
    return f"{h}:{m:02d}:{s:05.2f}"
head = """[Script Info]
ScriptType: v4.00+
PlayResX: 480
PlayResY: 854
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TT,Poppins,46,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,4,2,2,20,20,120,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
lines=[]
for a,b,txt in segs:
    cs = chunks(txt.split())
    total = sum(len(' '.join(c)) for c in cs)
    t = a
    for c in cs:
        s = ' '.join(c).rstrip(',.')
        d = (b-a)*len(' '.join(c))/total
        end = t+d
        last = (c is cs[-1])
        lines.append(f"Dialogue: 0,{ts(t)},{ts(end+0.15 if last else end)},TT,,0,0,0,,{{\\fad(40,0)}}{s.upper()}")
        t = end
open('subs.ass','w').write(head+'\n'.join(lines)+'\n')

