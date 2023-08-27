import os
os.system("cls")

genero = input("A)Masculino\nB)Femenino:\n")
edad = int(input("Edad: "))

if genero == "A" and edad < 25: categoria="MA"
elif genero == "A": categoria = "MB"
elif genero == "B" and edad < 23: categoria="FA"
else: categoria= "FB"

print("Categoria del empleado:",categoria)