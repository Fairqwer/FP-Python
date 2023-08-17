import os
os.system("cls")

categoria = input("Categoria: ")
promedio =float(input("Promedio: "))

pension_actual = 550 if categoria == "A" else 500 if categoria == "B" else 450 if categoria == "C" else 400 if categoria == "D" else print("Error")
if promedio < 14 : descuento = 0
elif promedio >= 14 and promedio < 16 : descuento = (0.10)*pension_actual
elif promedio >= 16 and promedio < 18 : descuento = (0.12)*pension_actual
elif promedio >= 18 and promedio <= 20 : descuento = (0.15)*pension_actual
else : print("Error")

nueva_pension = pension_actual - descuento

print(f"Pension actual        :S/ {pension_actual:.2f}")
print(f"Descuento             :S/ {descuento:.2f}")
print(f"Pension nueva         :S/ {nueva_pension:.2f}")