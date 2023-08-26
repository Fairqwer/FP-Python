import os
os.system("cls")

numero = int(input("Número: "))

c1 = numero%10
c2 = (numero//10)%10
c3 = (numero//100)%10

if c2+1 == c3 and c2-1 == c1:
    print("Es un número con cifras consecutivas")
elif c2-1 ==c3 and c2+1 == c1:
    print("Es un número con cifras consecutivas")
else:
    print("No es un número con cifras consecutivas")