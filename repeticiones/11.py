import os
os.system("cls")

contador = 0
capicuas = ""

for num in range(100,1000):
    c3 = num%10
    c1 = num//100
    if c1 == c3:
        contador += 1
        capicuas = capicuas+", "+str(num)

print(f"Hay {contador} números capicúas de tres cifras.")
print("Dichos numeros son"+capicuas)