import os
os.system("cls")


unidades = int(input("Unidades: "))

compra = 20 * unidades
descuento = ( 0.12 if compra <= 500 else 0.16 if compra > 700 else 0.14) * compra
caramelos = 5 if unidades <= 50 else 100 if unidades > 100 else 10

print(f"Compra        : S/ {compra:.2f}")
print(f"Descuento     : S/ {descuento:.2f}")
print(f"Total a pagar : S/ {compra - descuento:.2f}")
print(f"Caramelos     : {caramelos}")

unidades = int(input("Cantidad de productos: "))

importe = 20 * unidades
descuento = (0.16 if importe > 700 else 0.12 if importe <= 500 else 0.14) * importe
total = importe - descuento
caramelos = 5 if unidades <= 50 else 15 if unidades > 100 else 10

print("Importe de compra    : S/{importe:.2f}")

