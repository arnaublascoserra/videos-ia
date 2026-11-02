# Prompts que han funcionado — RelaxinGlasses

## R1. Cambiar a la persona de un TikTok por el avatar (con ojeras)
**Modelo:** `seedance-2.0-face` · **Vídeo:** trozo ≤ 15 s, texto borrado · **Imagen 1:** `avatares/mujer47/cara_ojeras.jpg` (o `solo_cara_ajustada.jpg` sin ojeras) · `duration` entera, 720p, sin audio · **Coste:** 0,69 $ por 4 s · **Usado en:** gafas-v11 plano 2
```
Replace the young man in video 1 with the woman from image 1, in EVERY frame of the video, from the first frame to the last, including when the white eye mask covers part of her face. Image 1 shows only her face and hair. She is a 47-year-old Spanish woman with long layered dark brown hair with caramel highlights and a few grey strands, hazel-brown eyes, warm light olive skin with real texture, fine lines and faint freckles, and clearly visible dark circles and tired hollow under-eyes exactly like image 1. She is NOT the young man with short black curly hair from video 1: she has long brown hair in every frame. She wears the same plain white crew-neck t-shirt as in video 1. She performs exactly the same movements as in video 1 at the same moments: she touches the dark circle under her eye with her finger, then puts on the white plastic under-eye LED mask, and the mask lights up with a soft, dim red glow. The white mask looks exactly as in video 1. Same living room with the wooden table, flowers and windows behind her, same daylight, same camera framing and timing as video 1. Casual everyday smartphone video. No watermarks, no logos, no on-screen text.
```

## R2. Plano nuevo corto sin vídeo de referencia ("después": se acerca y se toca las ojeras)
**Modelo:** `seedance-2.5` · **Imágenes:** 1 = cara sin ojeras, 2 = fondo, 3 = producto · 4 s, 720p, 9:16, sin audio · **Coste:** 0,87 $ · ⚠️ el producto salió con forma de gafas de sol: añadir una imagen del producto puesto
```
[Reference] Image 1 is the woman: copy her exact face, hair and skin. Image 2 is the room: her home dining room. Image 3 is the EXACT product, reproduce it identically.
[Person] A real 47-year-old Spanish woman, long layered dark brown hair with caramel highlights and a few grey strands, hazel-brown eyes, warm light olive skin with real texture, fine lines and faint freckles, fresh even under-eyes with no dark circles, exactly like image 1. Plain white crew-neck t-shirt.
[Action – one continuous 4-second take, real-time] Handheld vertical selfie video, front camera. She stands in the dining room from image 2 wearing the switched-off white under-eye mask from image 3. She takes the mask off with one hand, then leans in close to the camera until her face fills most of the frame, gently touches the skin under both eyes with her fingertips to show her fresh under-eyes, and smiles at the camera with a pleased, closed-lip smile.
[Realism] Casual UGC smartphone video, natural daylight, real skin texture, slight hand shake. NOT cinematic, no beauty filter.
NEVER change her face. NEVER show dark circles at the end. NEVER airbrush the skin. NEVER change the product shape. NEVER add text, logos or watermarks. NEVER add other people.
```

## R3. Limpiar una foto de producto (fondo liso)
**Modelo:** `gpt-image-2` · `size: 4:3`, `1k` · **Coste:** 0,0085 $
```
Edit image 1 into a clean product photo. Keep ONLY the white plastic under-eye LED mask, exactly as it is: same shape, same proportions, same curves, same glossy white plastic, same angle. Remove the box, the text, the cable, the hand and everything else. Place the mask alone on a seamless plain light grey background with a soft natural shadow under it, soft natural daylight. Do NOT redesign or change any part of the product. No text, no logos, no watermark, no hands.
```

## R4. Quitar texto/mano de un fotograma para usarlo de fondo
**Modelo:** `gpt-image-2` · **Coste:** 0,0085 $
```
Edit image 1: remove the text and the emoji completely, remove the hand and the object it holds. Keep EVERYTHING else exactly the same: same camera position and angle, same sofa, cushions, wall, rug and daylight. The empty room only, no people, no hands. Realistic smartphone photo, no text, no watermark.
```

## ❌ Vídeo de 14 s con 5 imágenes sueltas (no funcionó)
Ver `registro-generaciones.md` (2026-11-02, gafas-nuevo14s): el producto salió como un antifaz que tapa los ojos. Siguiente intento: imagen de inicio con el producto ya puesto en `image_urls` + "Image 1 is the first frame of the video".
