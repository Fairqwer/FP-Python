import os
os.system("cls")

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if a > b and b > c: print("Los numeros fueron ingresados de forma descendente.")
elif a < b and b < c: print("Los numeros fueron ingresados de forma ascendente.")
else: print("Los números fueron ingresados de forma desordenada.")