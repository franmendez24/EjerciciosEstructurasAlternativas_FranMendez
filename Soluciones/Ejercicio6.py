#Fran Mendez Gonzalez
#17/11/2026
#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

cadena = input("Introduce una cadena: ")

if len(cadena) == 1 and cadena.isalpha() and cadena.isupper():
    print("Es una letra mayúscula.")
else:
    print("No es mayúscula.")