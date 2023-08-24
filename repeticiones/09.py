import os
os.system("cls")

altura = int(input("Altura: "))
print(f"Ancho:  {altura*2}")

for i in range(1,altura+1):
        print("*"*(altura*2))
