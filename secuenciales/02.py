metros=int(input("Metros: "))

centimetros=metros*100
pulgadas=centimetros/2.54
pies=pulgadas/12
yardas=pies/3

print(f"La cantidad en centimetros es: { format(centimetros,'.2f')} cm")
print(f"La cantidad en pulgadas es: { format(pulgadas,'.2f')} pgd")
print(f"La cantidad en pies es: { format(pies,'.2f')} ft")
print(f"La cantidad en yardas es: { format(yardas,'.2f')} yd")
