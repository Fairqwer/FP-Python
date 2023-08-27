import os
os.system("cls")

montovendido = int(input("Monto vendido: "))

sueldobruto = 600+(0.15*montovendido)

if sueldobruto > 1800:
    descuento = 0.10*sueldobruto
else:
    descuento = 0.05*sueldobruto

if montovendido > 1000:
    polos = 3
else:
    polos = 1

print(f"Sueldo bruto    : S/ {sueldobruto:.2f}")
print(f"Descuento       : S/ {descuento:.2f}")
print(f"Sueldo neto     : S/ {sueldobruto-descuento:.2f}")
print(f"Polos           : {polos}")