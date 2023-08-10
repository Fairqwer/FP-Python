pies = int(input("Pies : "))
pulgadas = int(input("Pulagadas: "))


metros= (pies*12 + pulgadas)*2.54 /100

print(f"Metros = { format(metros, '.2f')}")