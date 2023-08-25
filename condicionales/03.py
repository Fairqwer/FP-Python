import os
os.system("cls")

grados = int(input("Ingrese el ángulo: "))

if grados == 0: print(f"{grados} es un ángulo nulo.")
if grados > 0 and grados < 90: print(f"{grados} es un ángulo agudo.")
if grados == 90: print(f"{grados} es un ángulo recto.")
if grados > 90 and grados < 180: print(f"{grados} es un ángulo obtuso.")
if grados == 180: print(f"{grados} es un ángulo llano.")
if grados > 180 and grados < 360: print(f"{grados} es un ángulo cóncavo.")
if grados == 360: print(f"{grados} es un ángulo completo.")
