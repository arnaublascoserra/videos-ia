# MÉTODO 1 — Vídeo UGC con personaje + producto (base Filedesign, adaptado)

Cuando Arnau diga **"usamos el método 1"**, seguir estos pasos en orden. Es el método con el que se hizo el vídeo de RelaxinGlasses del 2026-11-03 (`RelaxinGlasses/metodo-filedesign/`, resultado final: `04_video/edicion/video3_es_subtitulado.mp4`).

Origen: vídeo de YouTube de Filedesign (OpenArt) https://www.youtube.com/watch?v=KB8vV20lf34 + PDF "AI_UGC_Ad_Prompts", pasado a APIMart y corregido con lo que aprendimos.

## Reglas de siempre
- Hablar con Arnau en español; los prompts a APIMart en **inglés**.
- **Antes de lanzar cualquier generación: explicar qué, modelo y coste, y esperar su OK.** "No generes nada" = no generar.
- Borrador siempre en la calidad más barata (480p); la final (1080p) solo cuando el borrador esté bien.
- Fotos de personas reales nunca al repo (es público): usar `upload_image` de APIMart.
- Descargas: URL en `sistema/pedidos/<nombre>.txt` → push → esperar ~60 s → pull → mover de `sistema/descargas/` a la carpeta del proyecto y el `.txt` a `sistema/pedidos/archivo/`. Copiar también a la carpeta de Arnau en el PC (`...\Referencias videos ia\<carpeta del método>\`).
- Tras cada generación: revisar fotogramas (hoja de 12 fotogramas), apuntar fila en `registro-generaciones.md` del producto.

## Estructura de carpetas (por producto)
```
<Producto>/metodo-1_<nombre>/
  01_personaje/  02_hoja_personaje/  03_producto/  04_video/{fotogramas,edicion}
```

## Paso 1 — Personaje (≈0,1–0,2 créditos)
- Modelo: **gpt-image-2**, 4K/2k, vertical. Prompt de Arnau describiendo la persona (edad, rasgos, pelo, ropa) — foto realista tipo smartphone.
- Arnau elige una. Si hay que cambiar el fondo a **gris liso**: NO reeditar con IA (baja calidad y cambia colores) → recorte gratis con RVM (`scripts/`) sobre gris.

## Paso 2 — Hoja de personaje (≈0,15 créditos cada una)
- Modelo: **Nano Banana 2** (`gemini-3.1-flash-image-preview`), `size 16:9`, `resolution 4K`, image_urls = [personaje del paso 1].
- Prompt: character sheet de la misma persona (varias vistas: frente, perfil, tres cuartos, cuerpo entero) con la ropa del vídeo, fondo gris, **prioridad absoluta a la identidad de la cara**, sin reír si afecta a la consistencia.
- Si las caras pequeñas no se parecen: pegado de cara gratis (inswapper) → versión `_CARA_PEGADA`.
- Arnau elige la buena y se renombra `HOJA_PERSONAJE_BUENA_<ropa>.jpg`.

## Paso 3 — Producto
- Preferir **fotos propias/limpias del producto** (fondo liso, sin texto) antes que generadas.
- Necesarias: 1 foto **apagado** en el ángulo en que se sujetará en mano (RelaxinGlasses: `producto_8_tres_cuartos_patillas_abiertas.jpg`) y 1 foto **encendido** (generada con Nano Banana 2 si hace falta, revisando que no invente piezas).
- Nano Banana 2 con muchas referencias inventa detalles (bisagras) → si pasa, usar la foto real.

## Paso 4 — Imágenes de control (≈0,14 créditos cada una, Nano Banana 2, 9:16, 2K)
Claves para que el vídeo salga bien (lo que arregló el vídeo 1):
- **Imagen de inicio (primer fotograma)**: la persona en el sitio y encuadre del vídeo, sujetando el producto apagado en el ángulo de la foto de producto, con el "antes" marcado (p. ej. ojeras). Hecha con Nano Banana 2 (gpt-image-2 ignoró el ángulo).
- **Imagen del producto en uso**: la misma persona con el producto puesto/encendido, como debe verse (luz suave, posición correcta). Prompt usado:
  > Edit @image1: the same woman, a few seconds later, now WEARING the glasses from @image2, switched on. Position exactly like in @image3: [...]. The red LED light is soft and dim: only a thin red glow inside the pads [...]. Keep everything else exactly as in @image1: same face, same under-eye dark circles, same hair, same sweater, same sofa, same window light, same vertical selfie framing. Realistic smartphone photo. No text, no logos.

## Paso 5 — Prompt maestro + vídeo (Seedance 2.5)
- Modelo **seedance-2.5**, `duration` fija (nunca Auto), `aspect_ratio 9:16`, `generate_audio true`, borrador `resolution 480p` (≈0,096 $/s → 22 s ≈ 21 créditos); final 1080p ≈ 118 créditos.
- **image_urls en este orden** (= image 1…5 en el prompt):
  1. imagen de inicio (primer fotograma)
  2. hoja de personaje buena
  3. producto apagado
  4. producto encendido
  5. persona con el producto en uso
- `first_frame_image` NO funciona en APIMart → el prompt empieza con **"Image 1 is the first frame of the video."**
- Plantilla (5 planos, 22 s):
```
Image 1 is the first frame of the video. Vertical 9:16 UGC-style selfie video, 22 seconds, shot in 5 continuous segments (~4s each, last one ~6s), same woman as image 1 and image 2 throughout — [descripción persona, ropa, sitio, luz]. She holds her phone at arm's length, front camera, slight natural handheld movement, authentic and relaxed selfie energy, talking directly to camera like she's telling a close friend about something that genuinely helped her. [Idioma: "She speaks in Spanish with a natural accent from Spain (Castilian Spanish), at a relaxed natural pace." si es en español]

Shot 1 (0–4s): exactly like image 1. She holds the switched-off product of image 3 still at chin height, without turning or bending it. [antes visible]. She says: "[frase 1]"
Shot 2 (4–8s): she puts on / uses the product of image 3 [...] like image 4 and image 5. She says: "[frase 2]"
Shot 3 (8–12s): using it exactly like image 5 [acción relajada]. [luz suave solo donde toca]. She says: "[frase 3]"
Shot 4 (12–16s): [quita el producto] [después claramente mejor que en el plano 1]. She says: "[frase 4]"
Shot 5 (16–22s): she holds the product of image 3 still next to her face and smiles. She says: "[CTA]" Then she keeps smiling at the camera for the last two seconds without speaking.

Consistent character identity, outfit, setting and lighting across all five shots. The product is always exactly image 3 (off) and image 4 (on), never deformed. Natural ambient room sound, light phone-mic audio quality, no background music. Realistic skin texture, natural hand movements, no uncanny distortions on the product.
```
- Frases: ~4 s cada una (en español, acortarlas: se tarda más en decirlas).
- Versión en otro idioma = vídeo nuevo entero (los labios van con el audio); no hay lip-sync en APIMart.

## Paso 6 — Revisión
- Hoja de 12 fotogramas (0,5 s … 21,5 s) para ver producto deformado, luz, antes/después.
- Silencios con `ffmpeg silencedetect` para saber cuándo habla (no hay transcripción automática). Arnau escucha el audio.
- Problemas típicos: el producto se deforma cuando se mueve en la mano (sobre todo al quitárselo); la luz LED sale más fuerte que en la imagen de referencia.

## Paso 7 — Edición (gratis)
- **Subtítulos** con ffmpeg + ASS (`RelaxinGlasses/metodo-filedesign/04_video/edicion/subs.py`): Poppins Bold 46, blanco con borde negro, mayúsculas, 2–4 palabras, sincronizados con los tramos de voz, parte baja (MarginV 120).
- Versión final usada: `edicion/subs_final.py` (frase entera por subtítulo, minúsculas, Poppins 28, borde negro, MarginV 110; tiempos sacados de los subtítulos automáticos de CapCut).
- CapCut web: subtítulos automáticos en español gratis (sirven para saber exactamente qué dice y cuándo), pero la versión gratuita bloquea exportaciones tras varias ("función Pro") → exportar el final con ffmpeg.
- **Música** viral: NO está en CapCut web (solo stock). Se añade al publicar en TikTok/Instagram, volumen 10–20 %. Para anuncio de pago, solo la biblioteca comercial.
- Voz con ElevenLabs solo si la de Seedance no vale (hay que cuadrar cada frase con los labios).

## Coste de referencia (RelaxinGlasses, 22 s)
Imágenes ≈ 1 crédito en total · cada vídeo borrador 480p ≈ 21 créditos · final 1080p ≈ 118 créditos.
