# Cola de reproducción 
cola_reproduccion = [
    "SONG: Blinding Lights - The Weeknd",
    "AD: Coca-Cola Summer Splash",
    "SONG: Starboy - The Weeknd",
    "ERROR: Audio File Corrupt (0x302)",
    "SONG: Die With A Smile - Bruno Mars",
    "AD: Spotify Premium Promo",
    "SONG: One Dance - Drake",
    "CRITICAL: Battery Low 2%",
    "SONG: Stay - Justin Bieber"
]

canciones_reproducidas = 0

estado_final = "Cola completada sin interrupciones"

print("=== SPOTIFY SMART QUEUE MANAGER ===")

for elemento in cola_reproduccion:
    # Filtro de anuncios
    if "AD:" in elemento:
        print(f"[Saltando Anuncio] -> {elemento}")
        continue

    # Filtro de errores
    if "ERROR:" in elemento:
        print(f"[Fallo de Conexión] -> Omitiendo archivo dañado: {elemento}")
        continue

    # Apagado de emergencia
    if "CRITICAL:" in elemento:
        print(f"[ALERTA DEL SISTEMA] -> {elemento}. Apagando reproductor...")
        estado_final = "Interrumpido por batería crítica"
        break

    # Reproducción válida
    if "SONG:" in elemento:
        print(f"🔊 Reproduciendo: {elemento}... [OK]")
        canciones_reproducidas += 1

# Reporte final
print("\n" + "=" * 40)
print("     REPORTE FINAL DE REPRODUCCIÓN      ")
print("=" * 40)
print(f"- Canciones reproducidas con éxito: {canciones_reproducidas}")
print(f"- Estado final: {estado_final}")
print("=" * 40)