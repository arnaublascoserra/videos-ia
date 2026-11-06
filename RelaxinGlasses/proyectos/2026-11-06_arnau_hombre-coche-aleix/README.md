# Hombre40 en el coche — método de Aleix (vídeo a vídeo)

Referencia: TikTok del hombre en el coche (snaptik_7652707556514729238, 9,1 s, 576×1024, 2 planos con fundido a negro en ~6 s).

## Pasos
1. ✅ Analizar referencia (2 planos, texto arriba + burbuja de comentario, producto parecido, luz roja fuerte).
2. ✅ Preparar trozos (`scripts/propios/quitar_textos_coche.py`): texto de arriba borrado; **burbuja NO borrada** (al borrarla se emborronan las gafas; se tapará con texto propio en el montaje). Sin audio.
   - `trozos/trozo1_antes.mp4`: fotogramas 0–133 (0–5,58 s) → 6,0 s.
   - `trozos/trozo2_despues.mp4`: fotogramas 158–218 (6,58–9,1 s) → 3,96 s (minterpolate).
3. ⏳ Fotos de cara recortadas (con ojeras / sin ojeras).
4. Prompt plantilla E adaptada.
5. Generar seedance-2.0-face 720p sin audio (duration 6 + 4).
6. Revisar · 7. Montaje (bajar LED, textos 14 y 6, tapar burbuja, 1080) · 8. Receta.
