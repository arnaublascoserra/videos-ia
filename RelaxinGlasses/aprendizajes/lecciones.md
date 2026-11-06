# Lecciones aprendidas — RelaxinGlasses

Lecciones propias de este producto. Leer también `../../referencia-aleix/Snowbox/lecciones.md` (la versión más completa de las lecciones comunes del equipo de Aleix).

**Cómo aportar:** lección nueva con `(Arnau, fecha, proyecto)`. Si una prueba la contradice, añadir `⚠️` debajo; si la confirma, `✔️`.

---

## Producto
- **Las fotos de AliExpress del producto solo (de frente) parecen unas gafas de sol cerradas.** Seedance 2.5 sin vídeo de referencia se inventó un antifaz que tapa los ojos y unas gafas de sol. Hay que darle siempre una imagen del producto **puesto en una cara** (debajo de los ojos). *(Arnau, 2026-11-02, gafas-nuevo14s)*
- **Limpiar fotos de producto con gpt-image-2** ("keep ONLY the mask… remove the box, text, cable… plain light grey background… Do NOT redesign") funciona muy bien si el producto se ve entero en la foto (0,0085 $). Si una mano tapa parte del producto, se inventa la forma. *(Arnau, 2026-11-02, kit)*

## Luz LED
- **La intensidad de la luz se hereda del vídeo de referencia:** pedir "soft, dim, much weaker than in video 1" no la bajó. Se baja gratis con `scripts/propios/bajar_luz_led.py`. *(Arnau, 2026-11-01, gafas-v11)*

## Avatar y caras
- **Si la foto de cara del avatar incluye ropa o fondo, seedance-2.0-face los mete en el vídeo** (salió con el jersey y el dormitorio de la foto). Con un recorte solo de cara y pelo conservó la camiseta y el salón del original. *(Arnau, 2026-11-01, gafas-v11)*
- **Cambio hombre → mujer** (chico joven de piel oscura → mujer mediterránea de 47) salió perfecto con seedance-2.0-face y plantilla E. *(Arnau, 2026-11-01, gafas-v11)*
- **Para un antes/después de ojeras:** usar como img1 una versión del avatar CON ojeras (hecha con ChatGPT). Las ojeras se ven muy bien en el vídeo. El "después" se hace en otro plano con el avatar sin ojeras. *(Arnau, 2026-11-02, gafas-v11)*

## Planos y modelos
- **Planos muy cortos (1,4 s) ralentizados ×2,9 hasta 4 s** y devueltos a su velocidad en el montaje quedaron naturales. *(Arnau, 2026-11-01, gafas-v11)*
- **seedance-2.0 con 2 cambios a la vez (sofá + manos):** solo hizo el del fondo. Un cambio grande por pasada. *(Arnau, 2026-11-02, gafas-v11)*
- **seedance-2.5 sin vídeo de referencia obedece bien acciones cortas nuevas** (se quita las gafas, se acerca a cámara, se toca las ojeras), pero se inventa el producto si no tiene una buena referencia de él puesto. *(Arnau, 2026-11-02, gafas-v11)*
- ⚠️ Lección de Xavi (Snowbox, 2026-11-02): `first_frame_image` NO funciona por APIMart; usar `image_urls` y empezar el prompt con "Image 1 is the first frame of the video".

## Precios (APIMart, nov 2026)
- seedance-2.0 / 2.0-face: ~0,17 $/s en 720p con vídeo de referencia (0,69 $ por 4 s).
- seedance-2.5 sin vídeo de referencia: 480p 0,096 $/s · 720p 0,216 $/s · 1080p 0,535 $/s. Con vídeo de ref.: (duración ref + generada) × 0,13 $ en 720p. Fijar siempre `duration` (en "Auto" reserva 30 s).
- gpt-image-2: ~0,0085–0,015 $ por imagen.
- **Producto manipulado en vídeo sin referencia se deforma:** en el vídeo de 14 s (seedance-2.5 desde fotogramas) las gafas puestas se ven bien, pero al ponerlas/quitarlas se doblan como una tira de goma, sin patillas ni almohadillas. Además, pedir "thin, slim" en los fotogramas simplificó el producto. Para planos con el producto en la mano: partir de un vídeo real con el producto (como la réplica) o hacer planos cortos en los que el producto apenas se mueva. *(Arnau, 2026-11-02, gafas-nuevo14s)*
- **Las ojeras de `cara_ojeras.jpg` (hecha con ChatGPT) son demasiado marcadas para el vídeo:** se ven falsas. Usar una versión más suave. *(Arnau, 2026-11-02, gafas-v11)*
- **Aclarar ojeras gratis:** `scripts/propios/aclarar_ojeras.py yunet.onnx entrada.mp4 salida.avi 0.7` (cara con YuNet de opencv_zoo, descargable desde media.githubusercontent.com; sube la luz solo de lo que está más oscuro que la mejilla y se salta los fotogramas en que las gafas tapan la zona). Quitó la mayor parte de las ojeras demasiado marcadas sin efecto plástico. *(Arnau, 2026-11-02, gafas-v11)*
- **Cambiar manos con seedance-2.0 + vídeo de referencia no funciona** (3 intentos): ni sin foto, ni con 2 cambios, ni con foto de manos de referencia y un solo cambio. Las manos del vídeo original se imponen. *(Arnau, 2026-11-04, gafas-v11)*
- **Quitar un plano problemático gratis:** producto recortado (rembg isnet-general-use + limpiar huecos por color de fondo) pegado sobre el fondo limpio, zoom lento con ffmpeg zoompan; el texto fijo del vídeo se recupera como capa con mediana + baja varianza entre fotogramas (`texto_hook_overlay.png`). *(Arnau, 2026-11-04, gafas-v11 v5)*
- **Cambiar el texto fijo de un vídeo a otro idioma (gratis):** `scripts/propios/cambiar_texto_fijo.py` — máscara del texto viejo sacada por baja varianza entre fotogramas, inpainting TELEA por fotograma y texto nuevo (Inter Bold 50, sombra suave, emoji reutilizado del original) encima en la misma posición. Los restos quedan tapados por el texto nuevo. *(Arnau, 2026-11-04, gafas-v11 ES)*
- **Mejorar un vídeo de 480p sin que parezca más IA (gratis):** subir a 1080×1920 (lanczos) + nitidez suave (unsharp 1,2 px, 35 %) + grano gaussiano σ=3, CRF 23 (~4 MB/9 s). **GFPGAN (mejorar_caras.py) NO**: aunque sea al 40–70 % alisa la piel y quita pecas y arrugas (aspecto retocado), justo lo contrario de lo que se busca. Script: `scripts/propios/textos_y_luz_1080.py`. *(Arnau, 2026-11-05, coche-replica)*

## ⭐ Regla: reutilizar lo que ya salió bien (Arnau, 2026-11-05)
- **Antes de generar una imagen, buscar en `registro-generaciones.md` y en `fotogramas/` una imagen del mismo tipo que Arnau ya haya validado, y repetir su método exacto (modelo + referencias + estructura del prompt).** No inventar referencias nuevas.
- **Foto de un personaje con el producto PUESTO y encendido (validada por Arnau):** `proyectos/2026-11-02_arnau_gafas-nuevo14s/fotogramas/img5_mitad_gafas_encendidas.png` (gpt-image-2). Para un personaje nuevo: gpt-image-2, image_urls = [retrato del personaje, img5_mitad_gafas_encendidas.png], "replace the woman with the woman from image 1… keep the glasses EXACTLY as in image 2".
- ❌ NO usar `producto_NB2_encendido_4k.jpg` (foto de estudio con botones/LEDs/USB a la vista) como referencia del producto puesto: la IA copia esos detalles y no se parece a cómo se ve puesto. ❌ Tampoco `avatar_gafas_puestas_encendidas.jpg` (salen dos almohadillas sueltas).
- **No decir que una imagen "está bien" comparándola con la foto de estudio: compararla con la imagen que Arnau ya validó.**
- Ojeras para el "antes": tono marrón-grisáceo como `avatares/mujer47/cara_ojeras.jpg`; si se pide solo "not purple" quedan casi invisibles.
- ⚠️ (2026-11-06, hombre coche) Si en la foto de inicio el producto en la mano es mucho más grande que puesto en la cara (≈1,5×), Seedance lo encoge de golpe al ponérselo y queda fatal. Antes de lanzar el vídeo, comprobar que el producto en mano mida como mucho ≈1,1–1,2× el ancho de la cara. Arreglo gratis: cortar el tramo del encogimiento (salto de corte tipo TikTok).
- ❌ (2026-11-06, hombre coche, método Aleix) **seedance-2.0-face no cambió a un hombre por otro hombre parecido** (40 años, barba, pelo oscuro): en los 2 trozos salió la cara del TikTok original (16,3 créditos perdidos). En el v11 funcionó porque el cambio era grande (chico joven → mujer de 47). Para avatares parecidos al original: no usar video_urls o probar antes un trozo corto.
- **Rebajar ojeras gratis:** si la hoja con ojeras se hizo editando la hoja sin ojeras (misma maqueta), alinear las dos (cv2.phaseCorrelate) y mezclar un 50 % de la hoja sin ojeras solo donde la otra es más oscura → nivel intermedio sin gastar créditos. *(Arnau, 2026-11-06, hombre58)*
