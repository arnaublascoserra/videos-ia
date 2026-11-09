# Instrucciones para Claude en este repositorio

Repositorio de Arnau para vídeos con IA en APIMart. Un producto = una carpeta (p. ej. `RelaxinGlasses/`). Hablar con Arnau en español; los prompts a APIMart van en inglés.

## Al empezar
1. `git pull --rebase`.
2. Leer, en este orden:
   - `<Producto>/aprendizajes/recetas-validadas.md` → **si ya hay una receta para lo que se pide, repetirla exactamente** (mismo modelo, mismas referencias en el mismo orden, mismo prompt). No inventar referencias nuevas.
   - `<Producto>/aprendizajes/lecciones.md` y `prompts-que-funcionan.md`.
   - Las últimas filas de `<Producto>/aprendizajes/registro-generaciones.md`.
3. Referencia del equipo de Aleix (`referencia-aleix/`), solo cuando aplique:
   - Cambiar la persona de un vídeo real (método réplica): `referencia-aleix/BackAlign/lecciones.md` y `prompts-que-funcionan.md`.
   - Producto pequeño o detalles diminutos: `referencia-aleix/NailCheck/lecciones.md`.
   - Lo demás: `referencia-aleix/Snowbox/lecciones.md`.
4. Si Arnau pide actualizar la referencia de Aleix: copiar de nuevo `*/aprendizajes/*.md` de aleixgomez17/referencias-video a `referencia-aleix/<producto>/`. No editar esa carpeta a mano ni el repo de Aleix.

## Métodos
- **"Método 1"** (vídeo UGC con personaje + producto, Seedance 2.5): seguir paso a paso `metodos/METODO_1.md`. Es el método por defecto para vídeos nuevos.
- **"Método réplica"**: replicar un TikTok existente cambiando la persona por un avatar (ejemplos: `gafas-v11`, `2026-11-04_arnau_coche-replica`). Ver receta 1 de `recetas-validadas.md`.
- Pedir las fotos de referencia de un método no significa hacer todo el vídeo con ese método.

## Antes de gastar (siempre)
- Explicar en pasos qué se va a hacer, con qué modelo y cuánto cuesta, y **esperar el OK de Arnau**. "No generes nada" = no generar.
- Enseñar cada prompt en inglés **con su traducción al español** debajo.
- Avanzar paso a paso: una fase, revisión con Arnau, siguiente fase.
- Vídeo: primero borrador en la calidad más barata (480p); 1080p solo cuando el borrador esté aprobado.
- No relanzar una tarea que siga en `processing` (se cobra dos veces).

## Después de cada generación
- Revisar fotograma a fotograma (hoja de 12 fotogramas) y comparar con las referencias.
- Añadir fila al `registro-generaciones.md` del producto y, si se aprende algo, una lección con `(Arnau, fecha, proyecto)`.
- **Si Arnau valida una imagen o un vídeo:** apuntarlo en `recetas-validadas.md` con modelo, referencias en orden, **prompt literal completo** y parámetros.
- Commits: `"[Arnau] …"`.

## Dónde va cada cosa
- Fotos de producto: `<Producto>/productos/` (kit = limpias con fondo liso).
- Avatares: `<Producto>/avatares/<nombre>/`; fondos: `<Producto>/fondos/`.
- Cada vídeo: `<Producto>/proyectos/AAAA-MM-DD_arnau_<nombre>/` con `referencia/`, `trozos/`, `generaciones/`, `final/`.
- Descargas de APIMart: URL en `sistema/pedidos/<nombre>.txt`, push, esperar ~50 s, pull; mover de `sistema/descargas/` al proyecto y el `.txt` a `sistema/pedidos/archivo/`.
- Vídeo terminado: copiarlo también al PC de Arnau, en `Referencias videos ia\final\listos para publicar\`, con el nombre `AAAA-MM-DD_avatar_tipo_idioma.mp4`.
- Nunca subir fotos de personas reales: el repo es público, así que se suben con `upload_image` de APIMart.

## Edición
- Solo subtítulos (scripts de `RelaxinGlasses/metodo-filedesign/04_video/edicion/`) y exportar sin música: Arnau la añade al publicar en TikTok.
- Para mejorar un 480p sin que parezca más IA: `scripts/propios/textos_y_luz_1080.py`. No usar GFPGAN (`mejorar_caras.py`) en estos vídeos.
