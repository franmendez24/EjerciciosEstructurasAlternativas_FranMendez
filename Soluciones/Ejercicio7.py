#Fran Mendez Gonzalez
#17/11/2026
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
#exponente. Pueden ocurrir tres cosas:
#• El exponente sea positivo, sólo tienes que imprimir la potencia.
#• El exponente sea 0, el resultado es 1.
#• El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente (entero): "))

if exponente > 0:
    print(f"{base} elevado a {exponente} = {base ** exponente}")
elif exponente == 0:
    print(f"{base} elevado a 0 = 1")
else:
    if base == 0:
        print("Aviso: 0 elevado a un exponente negativo no está definido.")
    else:
        resultado = 1 / (base ** (-exponente))
        print(f"{base} elevado a {exponente} = {resultado}")