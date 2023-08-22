import os
os.system("cls")

n = int(input("Número: "))
m = int(input("Cantidad de multiplos: "))

for i in range(1,m+1):
    print(f"{(n*i)}")