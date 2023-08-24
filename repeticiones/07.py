import os
os.system("cls")

num = int(input("Ingrese el número: "))
x = 1

for i in range(1,num+1):
    x *= i

print(f"El factorial de dicho número es {x}")