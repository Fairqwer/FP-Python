import os
os.system("cls")

numero = int(input("Número: "))
exponente = int(input("Exponente: "))

resultado = 1

for i in range(1,exponente+1):
    resultado = resultado * numero

print(f"La potencia de dicho número es {resultado}")

