import os
os.system("cls")

precio = int(input("Ingrese el precio por docenas: "))
docenas = int(input("Ingrese las docenas: "))

montoTotal = precio*docenas

if docenas >= 6: descuento = 0.15*montoTotal
else: descuento = 0.10*montoTotal

if docenas >= 30: lapiceros = (docenas//3)*2
else: lapiceros = 0

print(f"Monto de compra:    S/{montoTotal:.2f}")
print(f"Descuento:          S/{descuento}")
print(f"Total a pagar:      S/{montoTotal-descuento:.2f}")
print(f"Lapiceros:          S/{lapiceros}")