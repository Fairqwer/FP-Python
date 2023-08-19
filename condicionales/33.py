import os
os.system("cls")

tdz = int(input("Minutos de tardanza: "))
obs = int(input("Nùmero de observaciones: "))

if tdz == 0 : ptdz = 10
elif tdz >= 1 and tdz <= 2 : ptdz = 8
elif tdz >= 3 and tdz <= 5 : ptdz = 6
elif tdz >= 6 and tdz <= 9 : ptdz = 4
elif tdz > 9 : ptdz = 0

if obs == 0 : pobs = 10
elif obs == 1 : pobs = 8
elif obs == 2 : pobs = 5
elif obs == 3 : pobs = 1
elif obs > 3 : pobs = 0

total = ptdz + pobs

if total < 11 : bono = 2.5 * total
elif total >= 11 and total <= 13 : bono = 5 * total
elif total >= 14 and total <= 16 : bono = 7.5 * total
elif total >= 17 and total <= 19 : bono = 10 * total
elif total >= 20 : bono = 12.5 * total

print(f"Puntaje puntualidad     : {ptdz}")
print(f"Puntaje rendimiento     : {pobs}")
print(f"Puntaje total           : {total}")
print(f"Bono anual              : {bono:.2f}") 