#Fran Mendez Gonzalez
#19/11/2026
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un
#dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara
#opuesta al resultado obtenido.
#• Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-
#5 y 3-4.
#• Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se
#mostrará el mensaje: “ERROR: número incorrecto.”.

dado = int(input("Introduzca número del dado: "))

if dado < 1 or dado > 6:
    print("ERROR: número incorrecto.")
else:
    opuesto = 7 - dado

    if opuesto == 1:
        letras = "uno"
    elif opuesto == 2:
        letras = "dos"
    elif opuesto == 3:
        letras = "tres"
    elif opuesto == 4:
        letras = "cuatro"
    elif opuesto == 5:
        letras = "cinco"
    else:
        letras = "seis"

    print(f'En la cara opuesta está el "{letras}".')