# Vídeos con IA (APIMart) — Arnau

Repositorio para crear vídeos de producto (UGC) con IA en APIMart. Organizado igual que el del equipo de Aleix: **una carpeta por producto**.

```
RelaxinGlasses/      ← producto: gafas LED antiojeras (ver su README)
  aprendizajes/  productos/  avatares/  fondos/  proyectos/
referencia-aleix/    ← copia de los aprendizajes de aleixgomez17/referencias-video (NO editar; se actualiza copiando de su repo)
  BackAlign/  NailCheck/  Snowbox/
scripts/             ← retoques gratis: los 9 de Aleix + propios/ (quitar_texto_estatico.py, bajar_luz_led.py)
sistema/             ← automático
  pedidos/       escribir la URL de APIMart en un .txt y hacer push → GitHub la descarga en ~50 s en descargas/
  descargas/     resultados descargados (moverlos luego al proyecto y el .txt a pedidos/archivo/)
.github/workflows/   descarga automática
```

## Antes de generar
1. Leer `<Producto>/aprendizajes/` y `referencia-aleix/Snowbox/lecciones.md` (lecciones comunes más completas).
2. Explicar plan, modelo y coste estimado, y esperar el OK antes de gastar.
3. Después de cada generación: añadir la fila a `registro-generaciones.md` del producto y la lección si la hay.

## Importante
- El repo es **público**: APIMart lee las imágenes y vídeos desde `raw.githubusercontent.com`. No subir fotos de personas reales (usar `upload_image` de APIMart).
- Fotos de producto limpias: sin textos, flechas, logos ni cajas, fondo liso, ≥ 500 px, proporción 0,4–2,5.

Origen de `referencia-aleix/`: commit `ac612d5` (2026-11-02) de aleixgomez17/referencias-video.
