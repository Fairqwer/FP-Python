kilometros = int(input("Cantidad de kilometros recorridos en el primer tramo: "))
pies = int(input("Cantidad de pies recorridos en el segundo tramo: "))
millas = int(input("Cantidad de millas recorridas en el tercer tramo: "))


Tmetros = kilometros*1000 + pies/3.2808 + millas*1609

Tyardas = kilometros*1094 + pies/3281 + millas*1.609

print(f"El total del recorrido en metros es { format(Tmetros,'.2f')} m y en yardas es { format (Tyardas,'.2f')} yd")