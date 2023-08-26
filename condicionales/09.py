import os
os.system("cls")

codigo = int(input("Ingrese el código del producto\n101\n102\n103\n104\n"))
unidades = int(input("Ingrese la cantidad de unidades: "))

precio = 17 if codigo == 101 else 25 if codigo == 102 else 16 if codigo == 103 else 27 if codigo == 104 else print("Código incorrecto")
importe = precio * unidades

if unidades > 0 and unidades < 11: descuento = 0.05*importe
elif unidades > 10 and unidades < 21: descuento = 0.08*importe
elif unidades > 20 and unidades < 31: descuento = 0.10*importe
else: descuento = 0.13*importe

print(f"Importe de compra   : S/{importe:.2f}")
print(f"Descuento           : S/{descuento:.2f}")
print(f"Total a pagar       : S/{importe-descuento:.2f}")