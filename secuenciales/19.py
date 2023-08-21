import os
os.system("cls")

ventas = int(input("Monto vendido: "))
comision = (ventas*9)/100
sueldoBruto = 500 + comision
descuento = (sueldoBruto*11)/100
sueldoNeto = sueldoBruto - descuento

print(f"Comisión: {comision:.2f}")
print(f"Sueldo bruto: {sueldoBruto:.2f}")
print(f"Descuento: {descuento:.2f}")
print(f"Sueldo neto: {sueldoNeto:.2f}")