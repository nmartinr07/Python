print("=== BIENVENIDO AL CONFIGURADOR DE PERFIL DE NETFLIX ===")

edad = int(input("Introduce tu edad: "))
plan = input("Introduce tu plan (Básico / Estándar / Premium): ")
genero = input("Introduce tu género favorito (Acción / Comedia / Sci-Fi / Anime): ")

plan = plan.strip().lower()     
genero = genero.strip().capitalize()  

# Control parental
if edad < 16 and genero in ("Acción", "Accion"):
    control = "RESTRICCIÓN ACTIVA"
    detalle = "Acceso redirigido a Comedia"
    print("\n[ADVERTENCIA] Acceso al género Acción denegado para menores de 16 años.")
    print("Se ha reajustado automáticamente tu recomendación de catálogo.")
    genero = "Comedia"
else:
    control = "ACCESO PERMITIDO"
    detalle = "Apto para mayores de 16"

if plan == "premium":
    calidad = "Ultra HD (4K)"
elif plan in ("estándar", "estandar"):
    calidad = "Full HD (1080p)"
elif plan in ("básico", "basico"):
    calidad = "HD (720p)"
else:
    calidad = "SD (480p)"
    print("\n[ADVERTENCIA] Plan no reconocido. Se aplica calidad SD (480p).")


match genero:
    case "Sci-fi" | "Sci-Fi" | "Ciencia ficción":
        serie = "Stranger Things"
    case "Anime" | "Manga":
        serie = "One Piece"
    case "Comedia" | "Humor":
        serie = "Wednesday"
    case "Acción" | "Accion":
        serie = "Cobra Kai"
    case _:
        serie = "La Casa de Papel"

print("[CONFIGURACIÓN DE PERFIL EXITOSA]")
print(f"- Control Parental: {control} ({detalle})")
print(f"- Calidad de Video Autorizada: {calidad}")
print(f'- Sugerencia Personalizada de Portada: "{serie}" (Género: {genero})')