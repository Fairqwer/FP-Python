n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))

n1c1 = str(n1%10)
n1c2 = str((n1//10)%10)
n1c3 = str((n1//100)%10)

n2c1 = str(n2%10)
n2c2 = str((n2//10)%10)
n2c3 = str((n2//100)%10)

print("Resultado:",n2c1+n1c2+n2c3,"y",n1c1+n2c2+n1c3)
