#Fran Mendez Gonzalez
#17/11/2026
#Crea un programa que pida al usuario dos números y muestre su división si el segundo
#no es cero, o un mensaje de aviso en caso contrario.

num1 = float(input("Introduce el primer número (dividendo): "))
num2 = float(input("Introduce el segundo número (divisor): "))

if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Aviso: no se puede dividir entre cero.")
