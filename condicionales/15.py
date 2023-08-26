import os
os.system("cls")

monto = int(input("Monto total vendido: "))

if monto < 5000: comision = 0.05*monto
elif monto >= 5000 and monto <10000: comision = 0.08*monto
elif monto >= 10000 and monto < 20000: comision = 0.10*monto
else: comision = 0.15*monto

sueldobruto = 250 + comision

if sueldobruto > 3500: descuento = 0.15*sueldobruto
else: descuento = 0.08*sueldobruto

sueldoneto = sueldobruto-descuento

print(f"Sueldo bruto   : S/{sueldobruto:.2f}")
print(f"Sueldo neto    : S/{sueldoneto:.2f}")
print(f"Descuento      : S/{descuento:.2f}")
print(f"Comisión       : S/{comision:.2f}")