import os
os.system("cls")

cuota = int(input("Cuota : "))
dia = int(input("Dìa de pago: "))

if dia <= 10 : descuento = 5 if 0.02*cuota < 5 else 0.02*cuota if 5 < 0.02*cuota else 0
elif dia > 20 : descuento = -10 if -0.03*cuota < -10 else -0.03*cuota if -10 < -0.03*cuota else 0
else : descuento = 0

total = cuota - descuento

print (f"Total a pagar     = S/ {total:.2f}")