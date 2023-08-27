import os
os.system("cls")

donacion = int(input("Monto de donación: "))

if donacion >= 10000: 
    salud = 0.30*donacion
    comedor = 0.50*donacion
    bolsa = 0.20*donacion
else:
    salud = 0.25*donacion
    comedor = 0.60*donacion
    bolsa = 0.15*donacion

print(f"Monto invertido en salud:         S/:{salud:.2f}")
print(f"Monto invertido en el comedor:    S/:{comedor:.2f}")
print(f"Monto invertido en la bolsa:      S/:{bolsa:.2f}")