import os
os.system("cls")

juan = int(input("Aporte de Juan: "))
rosa = int(input("Aporte de Rosa: "))
daniel = (int(input("Aporte de Daniel: ")))/3

total = juan + rosa + daniel

pJuan = (juan*100)/total
pRosa = (rosa*100)/total
pDaniel = (daniel*100)/total

print(f"El capital total es {total}")
print(f"Porcentaje del aporte de Juan: {pJuan:.2f} %")
print(f"Porcentaje del aporte de Rosa: {pRosa:.2f} %")
print(f"Porcentaje del aporte de Daniel: {pDaniel:.2f} %")