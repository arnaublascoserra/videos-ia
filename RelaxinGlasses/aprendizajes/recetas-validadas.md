# Recetas validadas (repetir EXACTAMENTE, no inventar referencias nuevas)

Regla: cada vez que Arnau valide una imagen o un vídeo, apuntar aquí modelo + referencias (en orden) + prompt literal + parámetros. Antes de generar, mirar aquí y preguntar a Arnau.
⚠️ Los prompts literales de las recetas 1–3 no se guardaron en su momento (se perdieron al compactar la conversación); solo constan modelo y referencias. A partir de ahora el prompt se copia entero.

## 1. Réplica coche — vídeo validado ✅ (mujer A, 2026-11-04)
Resultado: `proyectos/2026-11-04_arnau_coche-replica/generaciones/coche_video_v1_480p.mp4` ("muy bueno").
- Fondo: `fondos/coche_interior_v1.jpg` (NB2, solo texto, 9:16 2K).
- Foto 1 antes — NB2 9:16 2K — refs: hoja con ojeras + cara_ojeras + producto 8 (+ fondo coche).
- Foto 2 gafas puestas — NB2 — refs: hoja sin ojeras + avatar con gafas puestas encendidas + producto encendido.
- Foto 3 después — NB2 — refs: hoja sin ojeras + foto 3 + producto 8. La mano SUJETA las gafas.
- Vídeo — seedance-2.5, 9 s, 480p, sin audio — image_urls: [foto1 (primer fotograma), foto2, foto3, hoja sin ojeras, producto 8]; prompt "Image 1 is the first frame of the video", 2 planos (0–6 s se pone las gafas, 6–9 s después). Coste 0,87 $ (≈8,7 créditos).
- Nota: la foto 1 tiene un plano distinto de la 2 y la 3 y aun así el vídeo salió bien.

## 2. Gafas puestas encendidas (cualquier avatar) ✅
- gpt-image-2 — refs: [avatar, `proyectos/2026-11-02_arnau_gafas-nuevo14s/fotogramas/img5_mitad_gafas_encendidas.png`, fondo del sitio]. Validada en pelirroja32 y hombre40 (coche).

## 3. Hombre40 coche — fotos clave (2026-11-05)
- Antes v1 (`fotogramas/descartada_imagen_inicio_v1_otro_asiento.jpg`): producto bueno según Arnau, plano distinto. Método = receta 1 foto 1 con hoja con ojeras hombre40 + variante_B + coche + producto 8.
- Gafas encendidas: receta 2 ✅.
- Antes v2 / después v2 (editando la foto de gafas encendidas + recorte de producto + caja): ❌ producto peor y cable USB → NO repetir (la foto de la caja como referencia mete el cable).

## 4. Fotos clave en el MISMO plano (hombre40 coche, v3, 2026-11-05) — pendiente de OK
NB2 (gemini-3.1-flash-image-preview), size 9:16, resolution 2K.
image_urls: [1 foto de gafas encendidas ya aprobada (define plano), 2 hoja con ojeras (antes) / hoja sin ojeras (después), 3 producto 8 real]
Prompt antes:
> Use @image1 for the exact scene: same man, same car, same driver seat, same camera position, same distance, same framing, same light, same navy t-shirt, same background through the windows. Change only this: he is NOT wearing the glasses. His face shows the under-eye dark circles of @image2 (visible, tired look, natural, not purple). With one hand he holds the switched-off white glasses of @image3 at chest height by one temple, temples open, seen in the same three-quarter angle as @image3, exact same shape, proportions and matte white material as @image3, no lights on. His fingers clearly grip the glasses. Neutral, slightly tired expression, mouth closed, looking at the camera. No cable, no box, no other objects. Realistic vertical smartphone selfie photo, natural skin texture. No text, no logos.
Prompt después: igual pero "he has just taken the glasses off… NO dark circles… exactly like the face in @image2… With the index finger of his other hand he gently touches the skin under his eye. Pleasantly surprised, relaxed small smile". ⚠️ Salió con una sola mano haciendo las dos cosas → especificar "LEFT hand holds the glasses, RIGHT hand touches the eye, both hands visible".

## 5. Después con pose de la mujer A (hombre40 coche, v4, 2026-11-06) — pendiente de OK
NB2, 9:16, 2K. image_urls: [1 gafas encendidas del avatar (plano), 2 hoja sin ojeras, 3 producto 8, 4 `proyectos/2026-11-04_arnau_coche-replica/fotogramas/foto3_despues.jpg` (solo pose)]
> Use @image1 for the exact scene: same man, same car, same driver seat, same camera position, same distance, same framing, same light, same navy t-shirt, same background through the windows. Change only this: he has just taken the glasses off. His face is rested and fresh with NO dark circles under the eyes, exactly like the face in @image2. Copy ONLY the pose and hands from @image4 (do not copy the woman, her hair, her clothes or her car): his LEFT hand (on the left side of the photo) holds the switched-off white glasses of @image3 at chest height, fingers clearly gripping the frame from below; his RIGHT hand (on the right side of the photo) is raised to his face and the tip of the index finger gently touches the skin just under his eye. Two separate hands, both clearly visible, anatomically correct. The glasses have the exact same shape, proportions and matte white material as @image3, no lights on. Pleasantly surprised, relaxed smile, looking at the camera. No cable, no box, no other objects. Realistic vertical smartphone selfie photo, natural skin texture. No text, no logos.
Para otro avatar: cambiar "man/navy t-shirt/car" por lo suyo y @image1 por su foto de gafas encendidas.

## 6. Vídeo hombre40 coche (2026-11-06) — pendiente de revisión
seedance-2.5 · duration 9 · aspect_ratio 9:16 · resolution 480p · generate_audio false
image_urls: [1 imagen_inicio_v3 (primer fotograma), 2 gafas_puestas_encendidas_coche, 3 imagen_despues_v4, 4 hoja sin ojeras, 5 producto 8]
Prompt literal:
> Image 1 is the first frame of the video. Vertical 9:16 UGC-style selfie video, 9 seconds, one continuous handheld shot from the front camera of a phone, same man as image 1 and image 4 throughout: early 40s, short dark messy hair, dark beard with some grey, navy blue t-shirt, sitting in the driver seat of a parked car in daylight. Same car interior, same seat, same camera angle and same framing as image 1 for the whole video. He does not speak at any moment, his mouth stays closed, no talking, no lip movement.
> Shot 1 (0-6s): starts exactly like image 1: tired face with visible under-eye dark circles, holding the switched-off white glasses of image 5 in one hand at chest height. He calmly raises the glasses and puts them on, resting under his eyes exactly like image 2. The red light switches on softly: only a thin, dim red glow inside the pads under the eyes, like image 2. He relaxes with the glasses on for a moment, eyes open, small calm expression.
> Shot 2 (6-9s): he takes the glasses off and ends exactly like image 3: fresh rested face with no dark circles, his left hand holds the switched-off glasses at chest height, the index finger of his right hand gently touches the skin under his eye, pleasantly surprised smile with mouth closed, looking at the camera.
> The glasses are always exactly the product of image 5 (white, two oval eye pads, never deformed, never changing size or shape). Consistent face, beard, hair, t-shirt, car and lighting. Realistic skin texture, natural hand movements, slight natural phone shake. No text, no music.

## 7. Hombre58 coche — método 1 sin hablar (2026-11-06) ✅ validado por Arnau (preferido frente al método de Aleix)
Base de la imagen de inicio = fotograma de un vídeo ya generado (como el vídeo 3 de metodo-filedesign).
- 4a inicio: NB2 9:16 2K, [fotograma 1,0 s del vídeo Aleix hombre58, producto 8, hoja ojeras medias] — "Edit @image1… Change only two things: 1) glasses → @image2 (white opaque temples, same size)… 2) moderate under-eye dark circles like @image3". Luego ojeras +70 % gratis mezclando el fotograma base.
- 4b puestas encendidas: NB2, [inicio, producto NB2 encendido, fotograma Aleix 3 s (manos), hombre40 gafas encendidas coche (posición)].
- 5 vídeo: seedance-2.5, 9 s, 9:16, 480p, sin audio; image_urls [inicio, hoja sin ojeras, producto 8, producto NB2 encendido, gafas puestas encendidas]; prompt de 3 planos (0–2 sujeta quietas a la barbilla, 2–6 se las pone + luz tenue, 6–9 plano cercano sin gafas sin ojeras, dedo bajo el ojo), "He does not speak".

## 8. Unboxing de producto en mano, igual que un vídeo de referencia (pelirroja, 2026-11-08) — pendiente de OK de Arnau
1. Sacar fotogramas del plano de referencia y describirlos uno a uno (NO pasar sus fotogramas a la IA: copiaría su baño/manos).
2. Una foto de inicio por cada acción (NB2 9:16 2K) con: foto del avatar en su sitio (manos/ropa) + fotos PROPIAS del producto en la misma vista que el original (girar 180° gratis si hace falta) + caja real. Pedir "NO cable".
3. Un vídeo de 4 s por acción (seedance-2.5 480p sin audio), unidos con corte en el montaje como el original.
4. bajar_luz_led.py en el montaje.
