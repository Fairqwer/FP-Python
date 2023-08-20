import os
os.system("cls")

tarifa = int(input("Tarifa horaria: "))
horasTrabajadas = int(input("Horas trabajadas: "))

sueldoBasico = (tarifa*horasTrabajadas)*30
sueldoBruto = sueldoBasico + (sueldoBasico*20)/100
sueldoNeto = sueldoBruto - (sueldoBruto*10)/100

print(f"Sueldo básico:    {sueldoBasico:.2f}")
print(f"Sueldo bruto:     {sueldoBruto:.2f}")
print(f"Sueldo neto:      {sueldoNeto:.2f}")