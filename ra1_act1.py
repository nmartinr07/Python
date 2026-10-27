trama_red = "ARAGORN   -0850-1.20-1"

nombre = trama_red[0:10].strip()
#separador1 = trama_red[10]
base_ataque =int(trama_red[11:15])
#separador2 = trama_red [15]
multiplicador_critico = float(trama_red [16:20])
potenciador = bool(int(trama_red [21]))

dano_critico = base_ataque * multiplicador_critico

print("========================================")
print("        REPORTE DE PERSONAJE RPG        ")
print("========================================")
print(f"Nombre del heroe: {nombre}")
print(f"Base de Ataque: {base_ataque} pts")
print(f"Multiplicador critico: {multiplicador_critico}x")
print(f"Potenciador activo: {potenciador}")
print("----------------------------------------")
print(f"DAÑO CRITICO MAC: {dano_critico} pts")
print("========================================")