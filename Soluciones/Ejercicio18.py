#Fran Mendez Gonzalez
#19/11/2026
#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
#correspondiente. Si introducimos otro número nos da un error.

numero = int(input("Introduce el día de la semana (1-7): "))

if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3:
    print("Miércoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sábado")
elif numero == 7:
    print("Domingo")
else:
    print("Error: el número debe estar entre 1 y 7.")