import os
os.system("cls")

lista = []

numero1 = lista.append(int(input("Primer número: ")))
numero2 = lista.append(int(input("Segundo número: ")))
numero3 = lista.append(int(input("Tercer número: ")))

lista.sort()

print(f"El número intermedio es: {lista[1]}")