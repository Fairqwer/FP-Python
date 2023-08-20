import os
os.system("cls")

unidades = int(input("Unidades: "))
precio = int(input("Precio del producto: "))

importecompra = unidades*precio
descuento1 = (importecompra*15)/100
descuento2 = ((importecompra - descuento1)*15)/100
importeapagar = importecompra - descuento1 - descuento2

print(f"El importe de compra es S/ {importecompra:.2f}")
print(f"El primer descuento es S/ {descuento1:.2f}")
print(f"El segundo descuento es S/ {descuento2:.2f}")
print(f"El importe a pagar es S/ {importeapagar:.2f}")
