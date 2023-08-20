import os
os.system("cls")

donacion = int(input("Monto de donación: "))

salud = (donacion*25)/100
comedor = (donacion*35)/100
escuela = (donacion*25)/100
asilo = (donacion*15)/100

print(f"Monto dirigido al centro de salud:    S/ {salud:.2f}")
print(f"Monto dirigido al comedor infaltil:   S/ {comedor:.2f}")
print(f"Monto dirigido a la escuela infantil: S/ {escuela:.2f}")
print(f"Monto dirigido al asilo de ancianos:  S/ {asilo:.2f}")