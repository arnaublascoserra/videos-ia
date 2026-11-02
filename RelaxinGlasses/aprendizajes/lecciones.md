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
