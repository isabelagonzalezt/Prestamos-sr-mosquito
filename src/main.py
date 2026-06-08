import funciones
from datetime import datetime

usuarios = {}
items = {}
prestamos = {}
ventas = {}

while True:
    print("""            ______              _                                 
            | ___ \            | |                                
            | |_/ / __ ___  ___| |_ __ _ _ __ ___   ___  ___      
            |  __/ '__/ _ \/ __| __/ _` | '_ ` _ \ / _ \/ __|     
            | |  | | |  __/\__ \ || (_| | | | | | | (_) \__ \     
            \_|  |_|  \___||___/\__\__,_|_| |_| |_|\___/|___/     
                                                                
                                                                
     _____       ___  ___                      _ _        
    /  ___|      |  \/  |                     (_) |       
    \ `--. _ __  | .  . | ___  ___  __ _ _   _ _| |_ ___  
     `--. \ '__| | |\/| |/ _ \/ __|/ _` | | | | | __/ _ \ 
    /\__/ / |_   | |  | | (_) \__ \ (_| | |_| | | || (_) |
    \____/|_(_)  \_|  |_/\___/|___/\__, |\__,_|_|\__\___/ 
                                    | |                 
                                    |_|                 """)

    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Registrar usuario")
    print("2. Registrar ítem")
    print("3. Registrar préstamo")
    print("4. Registrar devolución")
    print("5. consultar items con mas de 30 dias")
    print("6. Administrador")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        funciones.registrar_usuario(usuarios)

    elif opcion == "2":

        funciones.registrar_item(items)

    elif opcion == "3":

        funciones.registrar_prestamo(
            usuarios,
            items,
            prestamos
        )

    elif opcion == "4":

        funciones.registrar_devolucion(
            usuarios,
            items,
            prestamos,
            ventas
        )

    elif opcion == "5":
    
            funciones.consultar_items_30_dias(
                usuarios,
                items,
                prestamos
            )

    elif opcion == "6":
         funciones.menu_admin(usuarios, items, prestamos, ventas)

    elif opcion == "7":

        print("Fin del programa")
        break

    else:

        print("Opción inválida")