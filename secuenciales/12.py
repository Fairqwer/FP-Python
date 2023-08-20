import os
os.system("cls")

a = int(input("Ingrese valor a: "))
b = int(input("Ingrese valor b: "))
c = int(input("Ingrese valor c: "))

x1 = (-b+(((b*b)-4*a*c)**0.5))/(2*a)
x2 = (-b-(((b*b)-4*a*c)**0.5))/(2*a)

print(f"Primera solucion = {x1:.2f}")
print(f"Segunda solucion = {x2:.2f}")

