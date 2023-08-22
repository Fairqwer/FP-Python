import os
os.system("cls")

numero = int(input("Número: "))
primero = int(input("Desde: "))
ultimo = int(input("Hasta: "))

for x in range(primero,ultimo+1):
    print(f"{numero} x {x} = {numero*x}")
