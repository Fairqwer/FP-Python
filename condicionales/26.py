import os
os.system("cls")

monto = int(input("Ingrese monto: "))

if monto > 5000:
    prestamo=0.30*monto
    interes=prestamo*0.10
else:
    prestamo=0.20*monto
    interes=prestamo*0.10

print(f"A pagar    : S/ {monto-prestamo}")
print(f"Prestamo   : S/ {prestamo}")
print(f"Intereses  : S/ {interes}")