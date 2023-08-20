import os
os.system("cls")

coleccion = []

valor1 = int(input("Primer valor: "))
valor2 = int(input("Segundo valor: "))
valor3 = int(input("Tercer valor: "))
valor4 = int(input("Cuarto valor: "))
valor5 = int(input("Quinto valor: "))

coleccion.append(valor1)
coleccion.append(valor2)
coleccion.append(valor3)
coleccion.append(valor4)
coleccion.append(valor5)

print(f"La lista es la siguiente {coleccion}")

coleccion.sort(reverse = True)

prom = sum(coleccion[0:3])/3

print(f"Promedio de los 3 números mayores: {prom}")

