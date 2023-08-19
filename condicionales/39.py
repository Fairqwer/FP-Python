import os
os.system("cls")

bHorasAusencia = float(input("Horas Ausencia: ")) <= 1.5
bTDefectuosos = int(input("Tornillos Defectuosos: ")) < 300
bTBuenos = int(input("Tornillos Buenos: ")) > 1000


if not bHorasAusencia and not bTDefectuosos and not bTBuenos : grados = 0
elif bHorasAusencia and not bTDefectuosos and not bTBuenos : grados = 7
elif not bHorasAusencia and bTDefectuosos and not bTBuenos : grados = 8
elif not bHorasAusencia and not bTDefectuosos and bTBuenos : grados = 9
elif bHorasAusencia and bTDefectuosos and not bTBuenos : grados = 12
elif bHorasAusencia and not bTDefectuosos and bTBuenos : grados = 13
elif not bHorasAusencia and bTDefectuosos and bTBuenos : grados = 15
elif bHorasAusencia and bTDefectuosos and bTBuenos : grados = 20

print(f"{grados:.2f}")