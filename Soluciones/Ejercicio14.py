#Fran Mendez Gonzalez
#19/11/2026
#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la
#cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta
#del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
#productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo
#A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es
#de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
#cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

precio_inicial = float(input("Precio inicial por kilo (€): "))
kilos = float(input("Kilos de uva entregados: "))
tipo = input("Tipo de uva (A/B): ").upper()
tamaño = int(input("Tamaño (1/2): "))

precio_final = None

if tipo == "A":
    if tamaño == 1:
        precio_final = precio_inicial + 0.20
    elif tamaño == 2:
        precio_final = precio_inicial + 0.30
elif tipo == "B":
    if tamaño == 1:
        precio_final = precio_inicial - 0.30
    elif tamaño == 2:
        precio_final = precio_inicial - 0.50

if precio_final is None:
    print("Error: el tipo debe ser A o B y el tamaño 1 o 2.")
else:
    ganancia = precio_final * kilos
    print(f"Precio final por kilo: {precio_final:.2f} €")
    print(f"El productor recibirá: {ganancia:.2f} €")