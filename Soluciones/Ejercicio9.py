#Fran Mendez Gonzalez
#17/11/2026
#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
c = float(input("Introduce el tercer número: "))

if b > a:
    a, b = b, a
if c > a:
    a, c = c, a
if c > b:
    b, c = c, b

print(f"De mayor a menor: {a}, {b}, {c}")