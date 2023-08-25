import os
os.system("cls")

texto = str(input("Ingrese un texto: "))

while True:

    opcion = input("Seleccione: \nA) Convertir texto a minúsculas \nB) Convertir texto a mayúsculas \nC) Salir \n")
    
    if opcion == "A":
        print("\n"+texto.lower()+"\n")
        break
    
    elif opcion == "B":
        print("\n"+texto.upper()+"\n")
        break

    elif opcion == "C":
        print("\nSaliendo del programa.\n")
        break

    else:
        print("\nIngrese una opción válida.\n")