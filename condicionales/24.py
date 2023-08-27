import os
os.system("cls")

monto = int(input("Monto vendido: "))
sueldobase = monto*0.10

if monto > 5000:
    exceso=((monto-5000)//500)*25
else:
    exceso=0
    
print(f"Sueldo del vendedor: S/{sueldobase+exceso:.2f}")