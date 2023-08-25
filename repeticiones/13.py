import os
os.system("cls")

limite = int(input("Ingrese el limite: "))

suma=0

for i in range(1,limite+1):
    if i%3 == 0 and i%5 != 0:
        suma=suma+i

print(f"La suma de los multiplos de 3 hasta {limite} es: {suma}")