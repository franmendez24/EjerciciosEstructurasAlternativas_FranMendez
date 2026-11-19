#Fran Mendez Gonzalez
#19/11/2026
#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

bisiesto = (año % 4 == 0 and año % 100 != 0) or año % 400 == 0

fecha_correcta = True

if año < 1 or mes < 1 or mes > 12 or dia < 1:
    fecha_correcta = False
else:
    if mes in (1, 3, 5, 7, 8, 10, 12):
        dias_mes = 31
    elif mes in (4, 6, 9, 11):
        dias_mes = 30
    else:  # febrero
        if bisiesto:
            dias_mes = 29
        else:
            dias_mes = 28

    if dia > dias_mes:
        fecha_correcta = False

if fecha_correcta:
    print(f"La fecha {dia:02d}/{mes:02d}/{año} es correcta.")
else:
    print("La fecha no es correcta.")