import os
os.system("cls")

numeromax = int(input("Número máximo: "))

divisores = 2

for i in range(2,numeromax+1):
    
    for x in range(2,i+1):
        if i%x == 0:
            divisores += 1
