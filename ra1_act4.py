
print("=== FASE 1: INICIANDO MULTI-SUMMON (10-PULL) ===")
xp_total = 0

for tirada in range(1, 11):
    xp = 100 + (tirada * 10)
    xp_total = xp_total + xp
    print(f"Abriendo sobre {tirada}... ¡Drop registrado! (+{xp} XP)")

print(f">>> Invocación completada. Total de XP ganada: {xp_total} XP")

print("\n=== FASE 2: DECODIFICANDO TRAMA DE DROPS ===")
trama_drops = "CRCCERCCRE"
comunes = 0
raros = 0
epicos = 0
polvo_estelar = 0

print(f"Procesando drops del servidor: {trama_drops}")

for letra in trama_drops:
    if letra == 'C':
        comunes = comunes + 1
        polvo_estelar = polvo_estelar + 10
        print("* Registro: Drop Común ('C') procesado (+10 Polvo Estelar)")
    elif letra == 'R':
        raros = raros + 1
        polvo_estelar = polvo_estelar + 50
        print("* Registro: Drop Raro ('R') procesado (+50 Polvo Estelar)")
    else:
        epicos = epicos + 1
        polvo_estelar = polvo_estelar + 250
        print("* Registro: Drop Épico ('E') procesado (+250 Polvo Estelar)")

print(">>> REPORTE DE DROPS COMPLETO:")
print(f"- Ítems Comunes: {comunes}")
print(f"- Ítems Raros: {raros}")
print(f"- Ítems Épicos: {epicos}")
print(f"- Polvo Estelar Total: {polvo_estelar}")

print("\n=== FASE 3: SIMULADOR DE COMPRA AUTOMÁTICA ===")
gemas = int(input("Introduce tu saldo de gemas para invocar (160 gemas/sobre): "))
sobres = 0

print("[Procesando...]")
while gemas >= 160:
    gemas = gemas - 160
    sobres = sobres + 1
    print(f"Gema gastada. Sobres acumulados: {sobres} | Gemas restantes: {gemas}")

print("\n>>> COMPRA COMPLETADA:")
print(f"- Sobres totales adquiridos: {sobres}")
print(f"- Saldo final sobrante: {gemas} gemas")