#Fran Mendez Gonzalez
#19/11/2026
#Escribe un programa que pida un número entero entre uno y doce e imprima el número
#de días que tiene el mes correspondiente.

mes = int(input("Introduce un número de mes (1-12): "))

if mes < 1 or mes > 12:
    print("Error: el número debe estar entre 1 y 12.")
elif mes in (1, 3, 5, 7, 8, 10, 12):
    print("El mes tiene 31 días.")
elif mes in (4, 6, 9, 11):
    print("El mes tiene 30 días.")
else:
    print("El mes tiene 28 días (29 si el año es bisiesto).")
