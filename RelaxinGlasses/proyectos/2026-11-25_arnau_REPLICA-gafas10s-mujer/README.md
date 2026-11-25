# Réplica «gafas 10 s – versión mujer» (25-11-2026) — avatar R («la del pepino»), dormitorio de noche
Copia exacta de nuestra réplica del hombre (`2026-11-21_arnau_REPLICA-gafas10seg`, publicada 22-11, 9.609 vistas FB). Cambia: persona (R), escenario (dormitorio, lámpara cálida), ropa (camiseta pijama crudo).

Imágenes NB2 9:16 2K: B0 (R a partir de V1_I1b_R_sofa) → ojeras suaves gratis con `scripts/propios/marcar_ojeras.py` D=10 (elegida por Arnau; la marcada era D=15) · I3 (gafas en manos, ref REP1_I3) · I5 (gafas puestas, ref REP1_I5) · I5_cerca (recorte gratis para c1) · I4a/I4b_manos (manos de mujer sujetando, fondo dormitorio, ref REP1_I4a/b).
Descartadas: I4a/I4b v1 (producto como antifaz: la referencia `productos/recortes/apagado_recorte.jpg` da una forma ancha → usar REP1_I4a como referencia de producto), v2 (patillas flotando), v3 (en la mesita: el vídeo original no tiene ese plano).
Clips seedance-2.5, 4 s, 480p, sin audio, seed 2611: c1 (I5_cerca, luz ~0,9 s) · c2 (B0, señala) · c3 (primer I3 → último I5) · c4 (primer I4a_manos → último I4b_manos, de un clip salen c4a y c4b) · c5 (I5, se quita y sonríe). Todos válidos a la primera.
bajar_luz_led.py en c1 lo empeora (parece irritación en la piel): se entrega el original.
Montaje: ver LEEME_montaje.txt en `final\clips para editar\2026-11-25_REPLICA_gafas10s_mujer\`.
Coste: imágenes 1,54 + clips 19,4 = ≈ 20,9 créditos.
Lección: antes de generar, comprobar que cada plano pedido existe en el vídeo que se copia.
