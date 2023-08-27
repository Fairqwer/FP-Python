import os
os.system("cls")

numero = int(input("Número asignado: "))

estadocivil = (numero//1000)%10
edad = numero//10-(((numero//1000)%10)*100)
genero = numero%10

if estadocivil <= 4 and genero <=2:
    estadocivil = "Soltero/a" if estadocivil == 1 else "Casado/a" if estadocivil == 2 else "Divorciado/a" if estadocivil == 3 else "Viudo/a"
    genero = "Masculino" if genero == 1 else "Femenino"

    print(f"Estado civil  :{estadocivil}")
    print(f"Edad          :{edad}")
    print(f"Género        :{genero}")

else: print("Algún dato es inválido.")