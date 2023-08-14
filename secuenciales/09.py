numero = int(input("Escriba el número de cuatro cifras: "))

c1 = numero%10
c2 = (numero//10)%10
c3 = (numero//100)%10
c4 = (numero//1000)%10

suma = c1+c2+c3+c4

print("La suma de los digitos es",suma)