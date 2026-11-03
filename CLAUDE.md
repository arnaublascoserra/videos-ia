# Instrucciones para Claude en este repositorio

Repositorio de Arnau para vídeos con IA en APIMart. Un producto = una carpeta (p. ej. `RelaxinGlasses/`).

## Al empezar
1. `git pull --rebase`.
2. Leer `<Producto>/aprendizajes/lecciones.md`, `prompts-que-funcionan.md` y las últimas filas de `registro-generaciones.md`; y `referencia-aleix/Snowbox/lecciones.md`.
3. Si Arnau pide actualizar la referencia del equipo de Aleix: copiar de nuevo `*/aprendizajes/*.md` de aleixgomez17/referencias-video a `referencia-aleix/<producto>/` (no editar a mano esa carpeta).

## Métodos guardados
- Si Arnau dice **"método 1"** / "usamos el método 1": seguir paso a paso `metodos/METODO_1.md`.

## Antes de gastar
- Explicar plan, modelo y coste estimado y esperar el OK de Arnau.

## Dónde va cada cosa
- Fotos de producto: `<Producto>/productos/` (kit = limpias con fondo liso).
- Avatares: `<Producto>/avatares/<nombre>/`; fondos: `<Producto>/fondos/`.
- Cada vídeo: `<Producto>/proyectos/AAAA-MM-DD_arnau_<nombre>/` con `referencia/`, `trozos/`, `generaciones/`, `final/`.
- Descargas de APIMart: URL en `sistema/pedidos/<nombre>.txt`, push, esperar ~50 s, pull; mover de `sistema/descargas/` al proyecto y el `.txt` a `sistema/pedidos/archivo/`.
- Nunca subir fotos de personas reales (repo público).

## Después de cada generación
- Revisar fotograma a fotograma, añadir fila al registro del producto y lección si la hay.
- Commits: `"[Arnau] …"`.
