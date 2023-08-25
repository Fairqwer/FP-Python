import os
os.system("cls")

numero = int(input("Número: "))

c1 = numero%10
c2 = (numero//10)%10
c3 = (numero//100)%10
c4 = (numero//1000)%10

if c1 > c2 and c1 > c3 and c1 > c4: mayorc=c1
elif c2 > c1 and c2 > c3 and c2 > c4: mayorc=c2
elif c3 > c2 and c3 > c1 and c3 > c4: mayorc=c3
else: mayorc=c4

if c1 < c2 and c1 < c3 and c1 < c4: menorc=c1
elif c2 < c1 and c2 < c3 and c2 < c4: menorc=c2
elif c3 < c2 and c3 < c1 and c3 < c4: menorc=c3
else: menorc=c4

print(str(mayorc)+str(menorc))