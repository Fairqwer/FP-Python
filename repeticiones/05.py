import os
os.system("cls")

numero = int(input("Número: "))

# x = 1
# while x <= 12 :
#   print(f"{numero} x {x} = {(numero * x)}")
#   x += 1

# x = 1
# while x <= 12 :
#   print(f"{numero} x {(' ' if x < 10 else '')}{x} = 
#       {(' ' if (numero*x) < 10 else '')}{(numero * x)}")
#   x += 1

for x in range(1,13):
    print(f"{numero} x {x} = {numero*x}")