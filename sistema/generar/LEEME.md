# Generar desde el móvil (sin ordenador)
1. Claude deja un pedido `NOMBRE.json` aquí (`{"tipo": "imagen"|"video", "body": {...}}`).
2. La acción «Generar en APIMart» lo envía con la clave del secreto `APIMART_API_KEY`, espera y descarga el resultado en `sistema/descargas/NOMBRE.*`.
3. El registro (task_id, coste, estado) queda en `hechos/NOMBRE.json`. Un pedido con registro no se vuelve a enviar.
Nada se genera sin el OK de Arnau: el pedido solo se crea después de su OK.

**Regla de Arnau (28-11):** usar este método SOLO cuando Arnau no esté en el ordenador. Si está en el ordenador, generar con el MCP de APIMart del ordenador (así no se gasta el límite de la clave de GitHub).
