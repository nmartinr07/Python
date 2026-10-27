# Práctica 1.2 - Twitch Custom Stream Alerts & Rewards Router

trama = "VIEWER-7890_TIER-2_BITS0250_WATCH045_MOD1"


id_espectador = trama[0:11]
nivel_suscripcion = trama[12:18]

bits_crudo = trama[19:27]
bits_enviados = int(bits_crudo[4:])

horas_crudo = trama[28:36]
horas_vistas = int(horas_crudo[5:])

rol_crudo = trama[37:41]
es_moderador = rol_crudo == "MOD1"

es_suscriptor_activo = nivel_suscripcion != "TIER-0"
es_donador_destacado = bits_enviados > 200
tiene_recompensa_fidelidad = horas_vistas > 40 and es_suscriptor_activo
activar_alerta_shoutout = es_moderador or es_donador_destacado
tiene_acceso_chat_vip = es_moderador or (es_suscriptor_activo and horas_vistas > 10)

print("=" * 50)
print("   TWITCH STREAM OVERLAY - VIEWER METRICS CARD   ")
print("=" * 50)
print(f"ID Espectador: {id_espectador}")
print(f"Nivel de Suscripción: {nivel_suscripcion}")
print(f"Bits Enviados: {bits_enviados} | Horas Vistas: {horas_vistas}")
print(f"Rol del Moderador: {es_moderador}")
print("-" * 50)
print("          ESTADOS Y RECOMPENSAS CALCULADAS       ")
print("-" * 50)
print(f"¿Es Suscriptor Activo?: {es_suscriptor_activo}")
print(f"¿Es Donador Destacado?: {es_donador_destacado}")
print(f"¿Tiene Premio por Fidelidad?: {tiene_recompensa_fidelidad}")
print(f"¿Activar Alerta en Pantalla?: {activar_alerta_shoutout}")
print(f"¿Tiene Acceso al Chat VIP?: {tiene_acceso_chat_vip}")
print("=" * 50)