from datetime import datetime

# ==========================================
# FUNCIONES DE VALIDACIÓN DE USUARIOS
# ==========================================


# Solicita y valida el nombre del usuario
# Debe tener mínimo 3 letras y no contener números
def validar_nombre():

    while True:

        nombre = input("Ingrese el nombre: ")

        if len(nombre) < 3:
            print("Error: el nombre debe tener mínimo 3 letras")
            continue

        if not nombre.isalpha():
            print("Error: el nombre no puede contener números")
            continue

        return nombre


# Solicita y valida el apellido del usuario
# Debe tener mínimo 3 letras y no contener números
def validar_apellido():

    while True:

        apellido = input("Ingrese el apellido: ")

        if len(apellido) < 3:
            print("Error: el apellido debe tener mínimo 3 letras")
            continue

        if not apellido.isalpha():
            print("Error: el apellido no puede contener números")
            continue

        return apellido


# Solicita y valida el documento del usuario
# Debe contener únicamente números, tener entre
# 3 y 15 dígitos y no estar registrado previamente
# no puede estar ya en usuarios
def validar_documento(usuarios):

    while True:

        documento = input("Ingrese el documento: ")

        if not documento.isdigit():
            print("Error: el documento solo puede contener números")
            continue

        if len(documento) < 3 or len(documento) > 15:
            print("Error: el documento debe tener entre 3 y 15 dígitos")
            continue

        if documento in usuarios:
            print("Error: el documento ya está registrado")
            continue

        return documento


# Solicita y valida el correo electrónico
# Debe contener @ y terminar en .com
def validar_correo():

    while True:

        correo = input("Ingrese el correo electrónico: ")

        if "@" not in correo:
            print("Error: el correo debe contener @")
            continue

        if not correo.endswith(".com"):
            print("Error: el correo debe terminar en .com")
            continue

        return correo


# Solicita y valida el tiempo de préstamo
# Solo se permiten los valores 5, 10, 15 o 30 días
# Solicita y valida el tiempo de préstamo
# Solo se permiten los valores 5, 10, 15 o 30 días
def validar_tiempo_prestamo():

    while True:

        tiempo = input(
            "Ingrese tiempo de préstamo en días (5, 10, 15 o 30): "
        )

        if not tiempo.isdigit():
            print("Error: debe ingresar un número")
            continue

        tiempo = int(tiempo)

        if tiempo not in [5, 10, 15, 30]:
            print("Error: tiempo no permitido")
            continue

        return tiempo


# ==========================================
# FUNCIÓN PRINCIPAL DE REGISTRO
# ==========================================

# Registra un nuevo usuario en el sistema
# utilizando las funciones de validación
def registrar_usuario(usuarios):

    print("\n--- REGISTRO DE USUARIO ---")

    # Solicitar y validar todos los datos
    nombre = validar_nombre()
    apellido = validar_apellido()
    documento = validar_documento(usuarios)
    correo = validar_correo()
    tiempo_prestamo = validar_tiempo_prestamo()

    # Guardar la información del usuario
    # usando el documento como clave principal
    usuarios[documento] = {
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "tiempo_prestamo": tiempo_prestamo,
        "prestamos": 0
    }

    print("\nUsuario registrado correctamente")

# ==========================================
# FUNCIONES DE VALIDACIÓN DE ÍTEMS
# ==========================================

# Solicita y valida el nombre del ítem
# Debe tener mínimo 3 caracteres
def validar_nombre_item():

    while True:

        nombre = input("Ingrese el nombre del ítem: ")

        if len(nombre) < 3:
            print("Error: el nombre debe tener mínimo 3 caracteres")
            continue

        return nombre


# Solicita y valida la categoría del ítem
def validar_categoria():

    while True:

        print("\nCategorías disponibles:")
        print("1. Videojuegos")
        print("2. Libros")
        print("3. Música y video")
        print("4. Herramientas")
        print("5. Dinero")
        print("6. Misceláneo y varios")

        opcion = input("Seleccione una categoría: ")

        if opcion == "1":
            return "Videojuegos"

        elif opcion == "2":
            return "Libros"

        elif opcion == "3":
            return "Música y video"

        elif opcion == "4":
            return "Herramientas"

        elif opcion == "5":
            return "Dinero"

        elif opcion == "6":
            return "Misceláneo y varios"

        print("Error: opción inválida")


# Solicita y valida el precio de compra
def validar_precio():

    while True:

        precio = input("Ingrese el precio de compra: ")

        if not precio.isdigit():
            print("Error: solo se permiten números")
            continue

        return int(precio)


# Genera automáticamente el ID del ítem
def generar_id(categoria, items):

    if categoria == "Videojuegos":
        prefijo = "VID"

    elif categoria == "Libros":
        prefijo = "LIB"

    elif categoria == "Música y video":
        prefijo = "MUS"

    elif categoria == "Herramientas":
        prefijo = "HER"

    elif categoria == "Dinero":
        prefijo = "DIN"

    else:
        prefijo = "MIS"

    numero = len(items) + 1

    if numero < 10:
        codigo = prefijo + "00" + str(numero)

    elif numero < 100:
        codigo = prefijo + "0" + str(numero)

    else:
        codigo = prefijo + str(numero)

    return codigo


# Solicita y valida el estado del ítem
def validar_estado():

    while True:

        print("\nEstado del ítem:")
        print("1. Excelente")
        print("2. Bueno")
        print("3. Regular")
        print("4. Malo")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            return "Excelente"

        elif opcion == "2":
            return "Bueno"

        elif opcion == "3":
            return "Regular"

        elif opcion == "4":
            return "Malo"

        print("Error: opción inválida")


# ==========================================
# REGISTRO DE ÍTEMS
# ==========================================

# Registra un nuevo ítem dentro del inventario
def registrar_item(items):

    print("\n--- REGISTRO DE ÍTEM ---")

    # Solicitar y validar los datos
    nombre = validar_nombre_item()
    categoria = validar_categoria()
    precio = validar_precio()
    estado = validar_estado()

    # Generar el ID automáticamente
    id_item = generar_id(categoria, items)

    # Guardar la información del ítem
    items[id_item] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "estado": estado,
        "disponible": True
    }

    print("\nÍtem registrado correctamente")
    print("ID generado:", id_item)

# ==========================================
# REGISTRAR PRÉSTAMO
# ==========================================

# Registra un préstamo para un usuario existente
def registrar_prestamo(usuarios, items, prestamos):

    print("\n--- REGISTRO DE PRÉSTAMO ---")

    # Verificar que existan usuarios
    if len(usuarios) == 0:
        print("No existen usuarios registrados.")
        return

    # Verificar que existan ítems
    if len(items) == 0:
        print("No existen ítems registrados.")
        return

    # Solicitar documento del usuario
    documento = input("Ingrese el documento del usuario: ")

    # Verificar que el usuario exista
    if documento not in usuarios:
        print("El usuario no existe.")
        print("Debe registrar el usuario primero.")
        return

    # Mostrar inventario disponible
    print("\n--- ÍTEMS DISPONIBLES ---")

    for id_item in items:

        if items[id_item]["disponible"]:

            print(
                id_item,
                "-",
                items[id_item]["nombre"]
            )

    # Solicitar ID del ítem
    # Verificar que el ítem exista
    while True:

        id_item = input(
        "Ingrese el ID del ítem (0 para cancelar): "
        )

        if id_item == "0":
            print("Préstamo cancelado.")
            return

        if id_item not in items:
            print("El ítem no existe.")
            continue

        if not items[id_item]["disponible"]:
            print("El ítem ya está prestado.")
            continue

        break
        

    # Verificar disponibilidad
    if not items[id_item]["disponible"]:
        print("El ítem ya está prestado.")
        return

    # Solicitar fecha
    fecha = input("Ingrese la fecha del préstamo (dd/mm/aaaa): ")

    # Generar ID del préstamo
    id_prestamo = "PRE" + str(len(prestamos) + 1).zfill(3)

    # Guardar préstamo
    prestamos[id_prestamo] = {

        "documento": documento,
        "id_item": id_item,
        "fecha": fecha,

        # Tomamos automáticamente los días
        # definidos para el usuario
        "dias_prestamo":
        usuarios[documento]["tiempo_prestamo"],
        "nombre":items[id_item]["nombre"],
        "estado": "Activo"
    }

    # Marcar el ítem como prestado
    items[id_item]["disponible"] = False

    # Aumentar contador de préstamos
    usuarios[documento]["prestamos"] += 1

    print("\nPréstamo registrado correctamente.")
    print("Código del préstamo:", id_prestamo)


# ==========================================
# REGISTRAR DEVOLUCIÓN
# ==========================================

def registrar_devolucion(usuarios, items, prestamos, ventas):

    print("\n--- REGISTRO DE DEVOLUCIÓN ---")

    if len(usuarios) == 0:

        print("No existen usuarios registrados.")
        return

    while True:

        documento = input("Ingrese documento (0 para cancelar): ")

        if documento == "0":

            print("Proceso cancelado.")
            return

        if documento not in usuarios:

            print("Usuario no encontrado.")

        else:

            break

    prestamos_activos = []

    for id_prestamo in prestamos:

        if prestamos[id_prestamo]["documento"] == documento and prestamos[id_prestamo]["estado"] == "Activo":

            prestamos_activos.append(id_prestamo)

    if len(prestamos_activos) == 0:

        print("El usuario no tiene préstamos activos.")
        return

    print("\nPRÉSTAMOS ACTIVOS")

    for id_prestamo in prestamos_activos:

        print(id_prestamo, "-", prestamos[id_prestamo]["nombre"])

    while True:

        id_prestamo = input("\nIngrese el ID del préstamo (0 para cancelar): ")

        if id_prestamo == "0":

            print("Proceso cancelado.")
            return

        if id_prestamo not in prestamos_activos:

            print("ID de préstamo inválido.")

        else:

            break

    while True:

        fecha_devolucion = input(
            "Ingrese la fecha de devolución (dd/mm/aaaa): "
        )

        try:

            fecha_prestamo = prestamos[id_prestamo]["fecha"]

            fecha1 = datetime.strptime(
                fecha_prestamo,
                "%d/%m/%Y"
            )

            fecha2 = datetime.strptime(
                fecha_devolucion,
                "%d/%m/%Y"
            )

            dias_transcurridos = (
                fecha2 - fecha1
            ).days

            break

        except:

            print("Fecha inválida.")

    dias_prestamo = prestamos[id_prestamo]["dias_prestamo"]

    id_item = prestamos[id_prestamo]["id_item"]

    # DEVOLUCIÓN A TIEMPO
    if dias_transcurridos <= dias_prestamo:

        prestamos[id_prestamo]["estado"] = "Devuelto"

        items[id_item]["disponible"] = True

        nombre = usuarios[documento]["nombre"]
        apellido = usuarios[documento]["apellido"]

        nombre_archivo = (nombre + "_" + fecha_devolucion.replace("/", "") +
            "_" + id_prestamo +".txt")

        archivo = open(nombre_archivo, "w")

        archivo.write("CERTIFICADO DE DEVOLUCION\n")
        archivo.write("=========================\n\n")

        archivo.write(f"Nombre: {nombre} {apellido}\n")
        archivo.write(f"Documento: {documento}\n")
        archivo.write(f"ID Prestamo: {id_prestamo}\n")
        archivo.write(f"ID Item: {id_item}\n")
        archivo.write(f"Fecha Prestamo: {fecha_prestamo}\n")
        archivo.write(f"Fecha Devolucion: {fecha_devolucion}\n")
        archivo.write(f"Dias Permitidos: {dias_prestamo}\n")
        archivo.write(f"Dias Transcurridos: {dias_transcurridos}\n")
        archivo.write("\nESTADO: DEVUELTO A TIEMPO")

        archivo.close()

        print("\nDevolución registrada correctamente.")
        print("Certificado generado:", nombre_archivo)

    # DEVOLUCIÓN TARDÍA
    elif dias_transcurridos <= 30:

        prestamos[id_prestamo]["estado"] = "Devuelto"

        items[id_item]["disponible"] = True

        nombre = usuarios[documento]["nombre"]
        apellido = usuarios[documento]["apellido"]

        nombre_archivo = (nombre + "_" + fecha_devolucion.replace("/", "") +
            "_" + id_prestamo +".txt")

        archivo = open(nombre_archivo, "w")

        archivo.write("CERTIFICADO DE DEVOLUCION\n")
        archivo.write("=========================\n\n")

        archivo.write(f"Nombre: {nombre} {apellido}\n")
        archivo.write(f"Documento: {documento}\n")
        archivo.write(f"ID Prestamo: {id_prestamo}\n")
        archivo.write(f"ID Item: {id_item}\n")
        archivo.write(f"Fecha Prestamo: {fecha_prestamo}\n")
        archivo.write(f"Fecha Devolucion: {fecha_devolucion}\n")
        archivo.write(f"Dias Permitidos: {dias_prestamo}\n")
        archivo.write(f"Dias Transcurridos: {dias_transcurridos}\n")
        archivo.write("\nESTADO: DEVUELTO A TIEMPO")

        archivo.close()

        print("\nDevolución registrada correctamente.")
        print("Certificado generado:", nombre_archivo)

# ==========================================
# GENERAR VENTA
# ==========================================
    else:
        prestamos[id_prestamo]["estado"] = "Vendido"

        nombre = usuarios[documento]["nombre"]
        apellido = usuarios[documento]["apellido"]

        precio = items[id_item]["precio"]

        subtotal = precio
        impuesto = subtotal * 0.23
        total = subtotal + impuesto
#GUARDAR LA VENTA
        ventas[id_prestamo] = {
        "documento": documento,
        "id_item": id_item,
        "precio": precio,
        "impuesto": impuesto,
        "total": total
        }

        nombre_archivo = nombre + "_" + documento + "_VENTA.txt"

        archivo = open(nombre_archivo, "w")

        archivo.write("FACTURA DE VENTA\n")
        archivo.write("=========================\n\n")

        archivo.write("Nombre: " + nombre + " " + apellido + "\n")
        archivo.write("Documento: " + documento + "\n")
        archivo.write("ID Prestamo: " + id_prestamo + "\n")
        archivo.write("ID Item: " + id_item + "\n")
        archivo.write("Fecha Prestamo: " + fecha_prestamo + "\n")
        archivo.write("Fecha Devolucion: " + fecha_devolucion + "\n\n")

        archivo.write("MOTIVO DE LA VENTA\n")
        archivo.write("-------------------------\n")
        archivo.write("El articulo fue retenido por mas de 30 dias despues de finalizar el tiempo de prestamo.\n\n")

        archivo.write("Articulo: " + items[id_item]["nombre"] + "\n")
        archivo.write("Precio del articulo: $" + str(precio) + "\n")
        archivo.write("Subtotal: $" + str(subtotal) + "\n")
        archivo.write("Impuesto por conchudez (23%): $" + str(round(impuesto)) + "\n")
        archivo.write("TOTAL A PAGAR: $" + str(round(total)) + "\n")

        archivo.write("\nESTADO: ARTICULO VENDIDO AL PRESTATARIO")

        archivo.close()

        # El préstamo queda vendido
        prestamos[id_prestamo]["estado"] = "Vendido"

        # El artículo deja de existir en el inventario
        del items[id_item]

        print("\nEl préstamo superó los 30 días.")
        print("Se generó automáticamente una factura de venta.")
        print("Factura generada:", nombre_archivo)


# ==========================================
# CONSULTAR ÍTEMS CON MÁS DE 30 DÍAS
# ==========================================

def consultar_items_30_dias(usuarios, items, prestamos):

    print("\n--- ÍTEMS CON MÁS DE 30 DÍAS PRESTADOS ---")

    encontrados = False

    hoy = datetime.now()

    for id_prestamo in prestamos:

        if prestamos[id_prestamo]["estado"] == "Activo":

            fecha_prestamo = prestamos[id_prestamo]["fecha"]

            fecha = datetime.strptime(
                fecha_prestamo,
                "%d/%m/%Y"
            )

            dias_transcurridos = (
                hoy - fecha
            ).days

            if dias_transcurridos > 30:

                documento = prestamos[id_prestamo]["documento"]
                id_item = prestamos[id_prestamo]["id_item"]

                print("\nID Préstamo:", id_prestamo)
                print("ID Ítem:", id_item)
                print(
                    "Nombre Ítem:",
                    items[id_item]["nombre"]
                )
                print(
                    "Usuario:",
                    usuarios[documento]["nombre"],
                    usuarios[documento]["apellido"]
                )
                print(
                    "Días prestado:",
                    dias_transcurridos
                )

                print("------------------------")

                encontrados = True

    if encontrados:

        print(
            "\nADVERTENCIA:"
        )

        print(
            "Existen artículos con más de 30 días de préstamo."
        )

        print(
            "Estos artículos deben pasar al proceso de venta."
        )

    else:

        print(
            "\nNo existen préstamos activos con más de 30 días."
        )
#MENÚ DEL ADMINISTRADOR
def menu_admin(usuarios,items,prestamos, ventas):
    administradores = {
        "Isabela Gonzalez Toro": "1017930887",
        "Alejandro Usme López": "1018235618",
        "Edwin David Garcia Rios": "1025891364"
    }
    print("\n-ACCESO ADMINISTRADOR-")

    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario not in administradores:
        print("Usuario con acceso no permitido")
        return
    if administradores[usuario]!=clave:
        print("Contraseña incorrecta")
        return
    if usuario in administradores and administradores[usuario] == clave:
#Se accede al menú de administración
        while True:
            print("\n---MENU ADMINISTRADORES---")
            print("1. Total préstamos registrados")
            print("2. Total ítems devueltos")
            print("3. Total ventas realizadas")
            print("4. Total pago realizado")
            print("5. Lista de usuarios")
            print("6. Usuario con más y menos préstamos")
            print("7. Salir")

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                print("\nTOTAL DE PRÉSTAMOS REGISTRADOS: ", len(prestamos))
            elif opcion == "2":
                devueltos = 0
                for id_prestamo in prestamos:
                    if prestamos[id_prestamo]["estado"]=="Devuelto":
                        devueltos += 1
                print("\nTOTAL DE ITEMS DEVUELTOS: ", devueltos)
            elif opcion == "3":
                print("\nTOTAL DE VENTAS: ", len(ventas))
            elif opcion == "4":
                pagos = 0 
                for id_venta in ventas:
                    pagos += ventas[id_venta]["total"]
                print("\nTOTAL PAGO REALIZADO: $", pagos)
            elif opcion == "5":
                print("\nLISTA DE USUARIOS")
                if len(usuarios) == 0:
                    print("No hay usuarios registrados")
                else:
                    for documento in usuarios:
                        print(documento,
                              "-",
                              usuarios[documento]["nombre"],
                              usuarios[documento]["apellido"]
                              )
            elif opcion == "6":
                if len(usuarios) == 0:
                    print("No hay usuarios registrados")
                else:
                    mayor_doc = ""
                    menor_doc = "" 
                    mayor = -1
                    menor = 999999
                    for documento in usuarios:
                        cantidad = usuarios[documento]["prestamos"]
                        if cantidad > mayor:
                            mayor = cantidad
                            mayor_doc = documento
                        if cantidad < menor:
                            menor = cantidad
                            menor_doc = documento
                    print("\nUSUARIO CON MÁS PRÉSTAMOS")
                    print(usuarios[mayor_doc]["nombre"],
                          usuarios[mayor_doc]["apellido"],
                          "-",
                          mayor
                          )
                    print("-"*100)
                    print("\nUSUARIO CON MENOS PRÉSTAMOS")
                    print(usuarios[menor_doc]["nombre"],
                          usuarios[menor_doc]["apellido"],
                          "-",
                          menor)
            elif opcion == "7":
                break
            else:
                print("Opción inválida")

