import os
os.system("cls")

cantidad = int(input("Ingrese el monto: "))

billete200 = cantidad // 200
cantidad = cantidad % 200

billete100 = cantidad // 100
cantidad = cantidad % 100

billete50 = cantidad // 50
cantidad = cantidad % 50

billete20 = cantidad // 20
cantidad = cantidad % 20

billete10 = cantidad // 10
cantidad = cantidad % 10

moneda5 = cantidad // 5
cantidad = cantidad % 5

moneda2 = cantidad // 2
cantidad = cantidad % 2

moneda1 = cantidad // 1
cantidad = cantidad % 1

print(f"Billetes de 200: {billete200}")
print(f"Billetes de 100:  {billete100}")
print(f"Billetes de 50:  {billete50}")
print(f"Billetes de 20:  {billete20}")
print(f"Billetes de 10:  {billete10}")
print(f"Monedas de 5:    {moneda5}")
print(f"Monedas de 2:    {moneda2}")
print(f"Monedas de 1:    {moneda1}")