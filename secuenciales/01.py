varones = int(input("varones : "))
mujeres = int(input("mujeres : "))

total= varones+mujeres

pVarones = varones*100.0/total
pMujeres = mujeres*100.0/total

print( f"El porcentaje de varones es { format(pVarones, '.2f')}% y el porcentaje de mujeres es { format(pMujeres, '.2f')}%")