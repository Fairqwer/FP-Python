import os
os.system("cls")

ca = int(input("Cateto adyacente: "))
co = int(input("Cateto opuesto: "))

h = ((ca*ca) + (co*co)) ** 0.5

print(f"La hipotenusa es {h:.2f}")