numero = int(input("Escriba el número de cuatro cifras: "))

c1 = str((numero%10))
c2 = str((numero//10)%10)
c3 = str((numero//100)%10)
c4 = str((numero//1000)%10)

print("El numero al revés es",c1+c2+c3+c4)