codigo = input("Introduce el codigo de la factura: ")

anio = codigo[4:7]
num = codigo[9:11]

importeTotal = float(input("Introduce el importe total de la factura: "))
descuento = int(input("Introduce el descuento: "))

print("\n--RESUMEN FACTURA--")
print(f"Año: ")