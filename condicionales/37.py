import os
os.system("cls")

Pamela = int(input("Pamela : "))
Karol = int(input("Karol : "))
Fany = int(input("Fany : "))

mitad = (Pamela + Karol + Fany) // 2

mensaje = ""

if Pamela > mitad : mensaje = "Ganó Pamela"
elif Karol > mitad : mensaje = "Ganó Karol"
elif Fany > mitad : mensaje = "Ganó Fany"

elif Pamela < Karol and Pamela < Fany : mensaje = "Pasan a 2da vuelta : Karol y Fany"
elif Karol < Pamela and Karol < Fany : mensaje = "Pasan a 2da vuelta : Pamela y Fany"
elif Fany < Pamela and Fany < Karol : mensaje = "Pasan a 2da vuelta : Pamela y Karol"

elif Pamela == Karol and Pamela == Fany and Karol == Fany : mensaje = "Elecciones anuladas"
elif Pamela > Karol and Pamela > Fany and Karol == Fany : mensaje = "Elecciones anuladas"
elif Karol > Pamela and Karol > Fany and Pamela == Fany : mensaje = "Elecciones anuladas"
elif Fany > Pamela and Fany > Karol and Pamela == Karol : mensaje = "Elecciones anuladas"

lista = {"Pamela : ": Pamela, "Karol : ": Karol, "Fany: ": Fany}
order = sorted(lista.items(), key=operator.itemgetter(1), reverse=True)

print(mensaje)
print(f"Primer lugar : {order[0]}")
print(f"Segundo lugar : {order[1]}")
print(f"Tercer lugar : {order[2]}")
