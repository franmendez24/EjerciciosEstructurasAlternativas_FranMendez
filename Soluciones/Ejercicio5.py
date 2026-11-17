#Fran Mendez Gonzalez
#17/11/2026
#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha
#introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

usuario = input("Nombre de usuario: ")
contrasena = input("Contraseña: ")

if usuario == "pepe" and contraseña == "asdasd":
    print("Has entrado al sistema")
else:
    print("Error: usuario o contraseña incorrectos")
