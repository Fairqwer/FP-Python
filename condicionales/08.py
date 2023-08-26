import os
os.system("cls")

examenesAprobados = int(input("Cantidad de exámenes aprobados: "))

if examenesAprobados <= 3:
    if examenesAprobados == 1: propina = 25
    elif examenesAprobados == 2: propina = 30
    elif examenesAprobados == 3: propina = 35
    else: propina = 20

    print(f"La propina mensual es de S/ {propina}")

else: print("Solo hay tres exámenes por mes.")