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
