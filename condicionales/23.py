import os
os.system("cls")

notaMatematicas = int(input("Nota en Matenáticas: "))
notaFisica = int(input("Nota en Física: "))

if notaMatematicas > 17: propinaM = 3*notaMatematicas
else: propinaM = 1*notaMatematicas

if notaFisica > 15: propinaF = 2*notaFisica
else: propinaF = 0.50*notaFisica

if (notaMatematicas+notaFisica)/2 > 16: obsequio = "Reloj"
else: obsequio = "No hay"

print(f"Propina en Matemáticas:     S/{propinaM:.2f}")
print(f"Propina en Física:          S/{propinaF:.2f}")
print(f"Total:                      S/{propinaM+propinaF:.2f}")
print(f"Obsequio:                   {obsequio}")