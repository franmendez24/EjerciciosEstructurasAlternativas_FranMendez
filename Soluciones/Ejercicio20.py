#Fran Mendez Gonzalez
#19/11/2026
#Una compañía de transporte internacional tiene servicio en algunos países de América del
#Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de
#transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se
#muestra en la tabla:
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son
#transportados, esto por cuestiones de logística y de seguridad. Realice un algoritmo para
#determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

peso = float(input("Introduce el peso del paquete (en gramos): "))
zona = int(input("Introduce la zona de destino (1-5): "))

if peso <= 0:
    print("Error: el peso debe ser mayor que 0.")
elif peso > 5000:
    print("Entrega rechazada: los paquetes de más de 5 kg no se transportan.")
else:
    if zona == 1:
        costo_gramo = 24.00
    elif zona == 2:
        costo_gramo = 20.00
    elif zona == 3:
        costo_gramo = 21.00
    elif zona == 4:
        costo_gramo = 10.00
    elif zona == 5:
        costo_gramo = 18.00
    else:
        costo_gramo = None

    if costo_gramo is None:
        print("Error: la zona debe estar entre 1 y 5.")
    else:
        total = peso * costo_gramo
        print(f"Costo por gramo: {costo_gramo:.2f} €")
        print(f"Cobro por la entrega: {total:.2f} €")