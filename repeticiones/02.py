import os
os.system("cls")

multiplicando = int(input("Multiplicando = "))
multiplicador = int(input("Multiplicador = "))

producto = 0
while multiplicador > 0 :
    producto += multiplicando
    multiplicador -= 1

print(f"Producto: {producto}")