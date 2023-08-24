import os
os.system("cls")

altura = int(input("Altura: "))

if altura >= 4:
        print(f"Ancho:  {altura*2}")
        for i in range(1,altura+1):
                print("*"*(altura*2))
else:
        print("Ingrese un valor igual o mayor a 4")
