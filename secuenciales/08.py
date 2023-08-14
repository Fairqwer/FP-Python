r = int(input("Radio del cilindro: "))
h = int(input("Altura del cilindro: "))

areabase = 3.1416*(r*r)
arealateral = 2*3.1416*r*h
areatotal = 2*areabase*arealateral

print(f"El area base del cilindro es {format (areabase, '.2f')} m, el area lateral es {format (arealateral, '.2f')} m y el area total es {format (areatotal, '.2f')} m.")