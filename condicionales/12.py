import os
os.system("cls")

numero = int(input("Número: "))

if numero == 1 : print("Lunes")
elif numero == 2 : print("Martes")
elif numero == 3 : print("Miercoles")
elif numero == 4 : print("Jueves")
elif numero == 5 : print("Viernes")
elif numero == 6 : print("Sabado")
elif numero == 7 : print("Domingo")
else : print("Error, el número ingresado es erroneo.")

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

if numero in range(1,8) : print(dias[numero - 1])
else: print("Error, el número ingresado es erroneo")
