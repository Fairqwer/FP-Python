import os
os.system("cls")

lista = []

nota1 = lista.append(int(input("Primera nota: ")))
nota2 = lista.append(int(input("Segunda nota: ")))
nota3 = lista.append(int(input("Tercera nota: ")))
nota4 = lista.append(int(input("Cuarta nota: ")))
nota5 = lista.append(int(input("Quinta nota: ")))

lista.sort()

print(f"Mayor nota eliminada: {lista[0]}")
print(f"Menos nota elimiada: {lista[4]}")
print(f"Promedio: {sum(lista[1:4])/3:.2f}")