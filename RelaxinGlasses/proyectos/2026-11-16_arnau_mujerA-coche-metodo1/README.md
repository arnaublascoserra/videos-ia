# Mujer A coche — método 1 (rehacer "secreto split" para que no se vea falso)
Misma estructura que `final\analisis tiktok retocados\analisis_tiktok_retocado_mujerA_coche_secreto_ES_split.mp4`.
- A_antes.jpg = foto1_antes de la réplica (sin cambios).
- B_puestas_v1.jpg ❌ NB2 con producto NB2 encendido como ref → gafas tipo máscara de esquí. NO usar esa ref para gafas puestas.
- B_puestas_v2.jpg ✅ NB2 refs [foto1_antes, foto2_gafas de la réplica] → forma correcta (banda bajo los ojos); encuadre más cerrado (como el original).
- C_despues_v1.jpg ✅ NB2 refs [foto1_antes, producto 8]: ojeras a la mitad, misma cara y edad.
- Clips seedance-2.5 480p sin audio, 4 s cada uno (mínimo del modelo = 4 s): clip1 [A, B_v2, producto 8] se pone las gafas (se encienden solas al final, válido); clip2 [B_v2, A] luz roja quieta; clip3 [C, producto 8] se toca bajo el ojo.
- Montaje: split A|C 2 s (Antes blanco / Después amarillo, Poppins Bold 62) + clip1 0,3–4,0 + clip2 0,5–3,0 + clip3 0,9–3,8; bajar_luz_led.py en clips 1–2; textos iguales al split original (y=100). Final: `final/analisis_tiktok_retocado_mujerA_coche_secreto_ES_split_metodo1.mp4` (11,1 s).
