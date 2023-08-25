import os
os.system("cls")

par = 0
impar = 0

for i in range(1000,10000):
    if i > 0:
        cifra = i % 10

        if cifra%2 == 0:
            par = par + cifra
        else:
            impar = impar + cifra

        i = i // 10

        print(i)