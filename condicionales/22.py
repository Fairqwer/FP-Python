import os
os.system("cls")

unidadesA = int(input("Unidades de producto A: "))
unidadesB = int(input("Unidades de producto B: "))

if unidadesA > 50: descuentoA = 0.15*(unidadesA*25)
else: descuentoA = 0

if unidadesB > 60: descuentoB = 0.10(unidadesB*30)
else: descuentoB = 0

print(f"Importe bruto producto A:  S/{unidadesA*25}")
print(f"Descuento producto A:      S/{descuentoA}")
print(f"Total a pagar producto A:  S/{(unidadesA*25)-descuentoA}")
print(f"Importe bruto producto B:  S/{unidadesB*30}")
print(f"Descuento producto B:      S/{descuentoB}")
print(f"Total a pagar producto B:  S/{(unidadesB*30)-descuentoB}")
print(f"Suma total a pagar:        S/{((unidadesA*25)-descuentoA)+((unidadesB*30)-descuentoB)}") 