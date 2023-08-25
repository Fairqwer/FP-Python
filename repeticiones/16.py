import os
os.system("cls")

texto = str(input("Ingrese texto: "))

for i in range(len(texto)-1,-1,-1):
    print(texto[i], end="")