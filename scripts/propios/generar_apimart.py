"""Genera imágenes y vídeos en APIMart desde GitHub Actions (sin depender del ordenador).

Cada pedido es un JSON en sistema/generar/NOMBRE.json:
  {"tipo": "imagen" | "video",
   "body": { "model": "...", "prompt": "...", ... }}   # mismos parámetros que en el MCP
El resultado se guarda en sistema/descargas/NOMBRE.(jpg|png|mp4) y el registro
(task_id, coste, estado) en sistema/generar/hechos/NOMBRE.json.
La clave va en el secreto APIMART_API_KEY. Se usa Idempotency-Key = NOMBRE para no
cobrar dos veces si el trabajo se repite."""
import json, os, glob, time, urllib.request, urllib.error

BASE = "https://api.apimart.ai"
KEY = os.environ["APIMART_API_KEY"]
H = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}

def call(method, path, body=None, extra=None):
    req = urllib.request.Request(BASE + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={**H, **(extra or {})})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {"http_error": e.code, "detail": e.read().decode(errors="replace")[:2000]}

def task_id_of(resp):
    d = resp.get("data", resp)
    if isinstance(d, list) and d:
        d = d[0]
    return d.get("task_id") or d.get("id")

def first_url(task):
    d = task.get("data", task)
    res = d.get("result") or {}
    for key in ("images", "videos"):
        for item in res.get(key, []) or []:
            u = item.get("url")
            if isinstance(u, list) and u:
                return u[0], d
            if isinstance(u, str):
                return u, d
    return None, d

os.makedirs("sistema/descargas", exist_ok=True)
os.makedirs("sistema/generar/hechos", exist_ok=True)
for f in sorted(glob.glob("sistema/generar/*.json")):
    nombre = os.path.basename(f)[:-5]
    log_path = f"sistema/generar/hechos/{nombre}.json"
    if glob.glob(f"sistema/descargas/{nombre}.*") or os.path.exists(log_path):
        continue
    pedido = json.load(open(f, encoding="utf-8"))
    tipo, body = pedido["tipo"], pedido["body"]
    path = "/v1/images/generations" if tipo == "imagen" else "/v1/videos/generations"
    resp = call("POST", path, body, {"Idempotency-Key": f"vi-{nombre}"})
    tid = task_id_of(resp) if "http_error" not in resp else None
    log = {"nombre": nombre, "tipo": tipo, "envio": resp, "task_id": tid}
    if not tid:
        log["estado"] = "error_envio"
    else:
        limite = time.time() + (20 * 60 if tipo == "video" else 5 * 60)
        while time.time() < limite:
            time.sleep(10)
            t = call("GET", f"/v1/tasks/{tid}")
            d = t.get("data", t)
            estado = d.get("status")
            if estado in ("completed", "failed", "cancelled", "error"):
                url, d = first_url(t)
                log.update(estado=estado, coste_creditos=d.get("credits_cost"), detalle=d.get("error") or d.get("fail_reason"))
                if url:
                    ext = "mp4" if tipo == "video" else ("png" if ".png" in url else "jpg")
                    urllib.request.urlretrieve(url, f"sistema/descargas/{nombre}.{ext}")
                    log["url"] = url
                break
        else:
            log["estado"] = "tiempo_agotado"   # se puede consultar luego con el task_id
    json.dump(log, open(log_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(nombre, log.get("estado"), log.get("coste_creditos"))
