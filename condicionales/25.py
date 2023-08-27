import os
os.system("cls")

sueldo = int(input("Sueldo base: "))
hijos = int(input("Hijos: "))

if hijos > 1:
    bonificacion = (0.125*sueldo)+(40*hijos)
else: bonificacion = 0.10*sueldo

print(f"Bonificacion:  S/{bonificacion:.2f}")
print(f"Sueldo neto:   S/{sueldo+bonificacion:.2f}")