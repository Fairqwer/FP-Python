import os
os.system("cls")

unidades = int(input("Cantidad de productos: "))

importe = 20 * unidades
descuento = (0.16 if importe > 700 else 0.12 if importe <= 500 else 0.14) * importe
total = importe - descuento
caramelos = 5 if unidades <= 50 else 15 if unidades > 100 else 10

print("Importe de compra    : S/{importe:.2f}")


