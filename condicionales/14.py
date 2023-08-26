import os
os.system("cls")
import random

unidades = int(input("Ingrese las unidades: "))
precio = int(input("Ingrese el precio: "))
tarjeta = random.randrange(1,200)

importe = precio * unidades
descuento = (0.15 if tarjeta%2 == 0 and tarjeta >= 100 else 0.05)*importe

print(f"Número de tarjeta:     {tarjeta}")
print(f"Monto de compra:     S/{importe:.2f}")
print(f"Descuento:           S/{descuento:.2f}")
print(f"Total a pagar:       S/{importe-descuento:.2f}")