import os
os.system("cls")

ingresos = int(input("Ingreso mensual: "))
costoCasa = int(input("Costo de la casa: "))

if ingresos < 1250:
    cuotaInicial = (0.15)*costoCasa
    cuotasMensuales = (costoCasa-cuotaInicial)/120
else:
    cuotaInicial = (0.30)*costoCasa
    cuotasMensuales = (costoCasa-cuotaInicial)/75

print(f"Cuota inicial: S/ {cuotaInicial:.2f}")
print(f"Cuota mensual: S/ {cuotasMensuales:.2f}")