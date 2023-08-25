import os
os.system("cls")

edad1 = int(input("Primera edad: "))
edad2 = int(input("Segunda edad: "))
edad3 = int(input("Tercera edad: "))

if edad1 > edad2 and edad1 > edad3: mayor=edad1
elif edad2 > edad1 and edad2 > edad3: mayor=edad2
else: mayor=edad3

if edad1 < edad2 and edad1 < edad3: menor=edad1
elif edad2 < edad1 and edad2 < edad3: menor=edad2
else: menor=edad3

print(f"La edad mayor es {mayor}")
print(f"La edad menor es {menor}")