# -*- coding: utf-8 -*-
import os

titulos = []
ejemplares = []       # stock actual
stock_inicial = []    # cantidad original (tope máximo permitido por título)

select = ""
opcion = "s"

def limpiar():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def es_entero_no_negativo(cadena):
    if cadena is None:
        return False
    cadena = cadena.strip()
    if cadena == "":
        return False
    if cadena.startswith("-"):
        return False
    return cadena.isdigit()

def normalizar_titulo(t):
    t = " ".join(t.strip().split())
    return t

def existe_titulo(nombre):
    objetivo = nombre.lower()
    i = 0
    while i < len(titulos):
        if titulos[i].lower() == objetivo:
            return True
        i += 1
    return False

def indice_titulo(nombre):
    objetivo = nombre.lower()
    i = 0
    while i < len(titulos):
        if titulos[i].lower() == objetivo:
            return i
        i += 1
    return -1

while select not in ["8","exit","Exit","EXIT"]:
    limpiar()
    print("----- BIBLIOTECA UTN -----")
    print("     ***** MENU *****\n")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir\n")

    select = input("Ingrese que opción desea realizar: ").strip()

    while select not in ["1","2","3","4","5","6","7","8","exit","Exit","EXIT"]:
        select = input("Opción incorrecta, ingrese nuevamente: ").strip()

    match select:

        case "1":
            limpiar()
            print("OPCIÓN 1 - INGRESAR TÍTULOS")
            continuar = "s"
            while continuar.lower() == "s":
                nombre = input("\nINGRESE TÍTULO: ").strip()
                nombre = normalizar_titulo(nombre)
                if not nombre:
                    print("\nERROR! el campo no puede estar vacío")
                elif existe_titulo(nombre):
                    print(f"\nERROR! El título '{nombre}' ya existe, ingrese otro nombre")
                else:
                    titulos.append(nombre)
                    ejemplares.append(0)
                    stock_inicial.append(0)
                    print(f"\n'{nombre}' fue agregado al catálogo con stock inicial = 0")
                seguir = input("\n¿Desea agregar otro título? (s/n): ").strip().lower()
                while seguir not in ["s","n"]:
                    seguir = input("ERROR! Ingrese 's' o 'n': ").strip().lower()
                continuar = seguir
            input("\nPRESIONE ENTER PARA VOLVER AL MENÚ...")

        case "2":
            limpiar()
            print("--- OPCIÓN 2 - INGRESAR EJEMPLARES ---")
            if len(titulos) == 0:
                print("\nERROR! Debe cargar títulos primero, seleccione la opción 1")
            else:
                pendientes = []
                i = 0
                while i < len(titulos):
                    if ejemplares[i] == 0 and stock_inicial[i] == 0:
                        pendientes.append(i)
                    i += 1
                if len(pendientes) == 0:
                    print("\nTodos los títulos ya tienen una cantidad inicial asignada.")
                else:
                    print("\nIngrese la cantidad inicial de ejemplares para los siguientes títulos:")
                    for idx in pendientes:
                        cantidad_copias = input(f"\nCantidad inicial para '{titulos[idx]}': ").strip()
                        while not es_entero_no_negativo(cantidad_copias):
                            cantidad_copias = input("ERROR! Ingrese un número entero válido (>= 0): ").strip()
                        cantidad = int(cantidad_copias)
                        ejemplares[idx] = cantidad
                        stock_inicial[idx] = cantidad
                    print("\nCarga inicial completada.\n")
            input("PRESIONE ENTER PARA VOLVER AL MENÚ...")

        case "3":
            limpiar()
            print("--- OPCIÓN 3 - MOSTRAR CATÁLOGO ---")
            if len(titulos) == 0:
                print("\nERROR! El catálogo está vacío. Agregue títulos primero (Opción 1).")
            else:
                print("\n--- CATÁLOGO DE LA BIBLIOTECA ---\n")
                i = 0
                while i < len(titulos):
                    print(f"-> Título: '{titulos[i]}' | Stock actual: {ejemplares[i]} / Stock inicial: {stock_inicial[i]}")
                    i += 1
            input("\nPRESIONE ENTER PARA VOLVER AL MENÚ...")

        case "4":
            repetir = "s"
            while repetir.lower() == "s":
                limpiar()
                print("--- OPCIÓN 4 - CONSULTAR DISPONIBILIDAD POR TÍTULO ---")
                if len(titulos) == 0:
                    print("\nEl catálogo está vacío. Ingrese títulos con la Opción 1 primero.")
                else:
                    titulo_buscado = input("\nIngrese el título del libro que desea buscar: ").strip()
                    titulo_buscado = normalizar_titulo(titulo_buscado)
                    if not titulo_buscado:
                        print("\nERROR! El nombre del título no puede estar vacío.")
                    else:
                        idx = indice_titulo(titulo_buscado)
                        if idx == -1:
                            print(f"\nEl libro '{titulo_buscado}' no se encuentra en el catálogo")
                        else:
                            print(f"\nDISPONIBILIDAD de '{titulos[idx]}' = {ejemplares[idx]} ejemplares (stock inicial: {stock_inicial[idx]})")
                repetir = input("\n¿Desea consultar otro título? (s/n): ").strip().lower()
                while repetir not in ["s","n"]:
                    repetir = input("ERROR! Ingrese 's' o 'n': ").strip().lower()
            input("\nPRESIONE ENTER PARA VOLVER AL MENÚ...")

        case "5":
            limpiar()
            print("--- OPCIÓN 5 - LISTAR LIBROS AGOTADOS ---")
            if len(titulos) == 0:
                print("\nNo hay títulos cargados aún.")
            else:
                agotados = [titulos[i] for i in range(len(titulos)) if ejemplares[i] == 0]
                if not agotados:
                    print("\nNO HAY LIBROS AGOTADOS EN EL CATÁLOGO")
                else:
                    print("\n --- TÍTULOS CON STOCK 0 ---\n")
                    for titulo in agotados:
                        print(titulo)
            input("\nPRESIONE ENTER PARA VOLVER AL MENÚ...")

        case "6":
            repetir = "s"
            while repetir.lower() == "s":
                limpiar()
                print("OPCIÓN 6 - AGREGAR TITULO")
                nombre = input("\nINGRESE EL TÍTULO DEL NUEVO LIBRO: ").strip()
                nombre = normalizar_titulo(nombre)
                if not nombre:
                    print("\nERROR! El título no puede estar vacío")
                else:
                    if existe_titulo(nombre):
                        print(f"\nERROR! El título '{nombre}' ya existe en el catálogo")
                    else:
                        cantidad_ejemplares = input(f"INGRESE LA CANTIDAD DE EJEMPLARES PARA '{nombre}': ").strip()
                        while not es_entero_no_negativo(cantidad_ejemplares):
                            cantidad_ejemplares = input("ERROR! Ingrese un número entero válido (>= 0): ").strip()
                        cantidad = int(cantidad_ejemplares)
                        titulos.append(nombre)
                        ejemplares.append(cantidad)
                        stock_inicial.append(cantidad)
                        print(f"\nSe agregó correctamente el título '{nombre}' con {cantidad} ejemplares al catálogo")
                repetir = input("\n¿Desea agregar otro título con ejemplares? (s/n): ").strip().lower()
                while repetir not in ["s","n"]:
                    repetir = input("ERROR! Ingrese 's' o 'n': ").strip().lower()
            input("\nPRESIONE ENTER PARA VOLVER AL MENÚ...")

        # --- CASE 7 actualizado ---
        case "7":
            repetir = "s"
            while repetir.lower() == "s":
                limpiar()
                print("--- OPCIÓN 7 - ACTUALIZAR EJEMPLARES (PRÉSTAMO / DEVOLUCIÓN) ---")
                if len(titulos) == 0:
                    print("\nEl catálogo está vacío, no se pueden realizar operaciones.")
                    break  # vuelve al menú principal

                titulo_buscado = input("\nIngrese el título del libro a actualizar: ").strip()
                titulo_buscado = normalizar_titulo(titulo_buscado)
                if not titulo_buscado:
                    print("\nERROR! El título no puede estar vacío")
                else:
                    idx = indice_titulo(titulo_buscado)
                    if idx == -1:
                        print(f"\nERROR! El libro '{titulo_buscado}' no se encuentra en el catálogo")
                    else:
                        # 1) Sin stock inicial -> informar y no preguntar p/d
                        if stock_inicial[idx] == 0:
                            print(f"\nEl título '{titulos[idx]}' todavía no tiene stock inicial asignado.")
                            print("Cargue ejemplares con la Opción 2 antes de registrar movimientos.")
                        # 2) Primera vez (no hubo movimientos): ejemplares == stock_inicial > 0
                        elif ejemplares[idx] == stock_inicial[idx]:
                            print(f"\nNo hay movimientos registrados todavía para '{titulos[idx]}' (stock: {ejemplares[idx]} / inicial: {stock_inicial[idx]}).")
                            # Sugerir iniciar un préstamo directo si hay stock disponible
                            iniciar = input("¿Desea iniciar un préstamo ahora? (s/n): ").strip().lower()
                            while iniciar not in ["s","n"]:
                                iniciar = input("ERROR! Ingrese 's' o 'n': ").strip().lower()
                            if iniciar == "s":
                                if ejemplares[idx] == 0:
                                    print("\nNo hay ejemplares disponibles para prestar.")
                                else:
                                    while True:
                                        cantidad = input("Ingrese la cantidad a prestar: ").strip()
                                        if not (cantidad.isdigit() and int(cantidad) > 0):
                                            print("ERROR! Ingrese un número entero positivo.")
                                            continue
                                        cantidad = int(cantidad)
                                        if cantidad <= ejemplares[idx]:
                                            ejemplares[idx] -= cantidad
                                            print("\nPRÉSTAMO INICIAL REGISTRADO")
                                            print(f"Nuevo stock para '{titulos[idx]}' = {ejemplares[idx]}")
                                            break
                                        else:
                                            print(f"\nERROR! No se pueden prestar {cantidad} ejemplares. Solo hay {ejemplares[idx]} disponibles.")
                                            continue
                            else:
                                print("Sin cambios. Vuelva cuando desee registrar un movimiento.")
                        else:
                            # 3) Ya hubo movimientos -> permitir p/d
                            while True:
                                print(f"\nLibro seleccionado: '{titulos[idx]}' | Stock actual: {ejemplares[idx]} / Stock inicial: {stock_inicial[idx]}")
                                operacion = ""
                                while operacion not in ['p', 'd']:
                                    operacion = input("\n¿Desea realizar un préstamo o una devolución? Ingrese (p / d): ").strip().lower()
                                    if operacion not in ['p', 'd']:
                                        print("\nError! Opción inválida, intente de nuevo ")

                                if operacion == 'p':
                                    if ejemplares[idx] == 0:
                                        print("\nNo hay ejemplares disponibles para prestar.")
                                        continue
                                    # pedir cantidad válida de préstamo
                                    while True:
                                        cantidad = input("Ingrese la cantidad a prestar: ").strip()
                                        if not (cantidad.isdigit() and int(cantidad) > 0):
                                            print("ERROR! Ingrese un número entero positivo.")
                                            continue
                                        cantidad = int(cantidad)
                                        if cantidad <= ejemplares[idx]:
                                            ejemplares[idx] -= cantidad
                                            print("\nPRÉSTAMO EXITOSO")
                                            print(f"Nuevo stock para '{titulos[idx]}' = {ejemplares[idx]}")
                                            break
                                        else:
                                            print(f"\nERROR! No se pueden prestar {cantidad} ejemplares. Solo hay {ejemplares[idx]} disponibles.")
                                            continue
                                    break  # operación válida realizada

                                else:  # devolución
                                    if ejemplares[idx] == stock_inicial[idx]:
                                        print("\nNo se puede devolver porque no hay préstamos activos para este título.")
                                        continue
                                    # pedir cantidad válida de devolución
                                    while True:
                                        cantidad = input("\nIngrese la cantidad a devolver: ").strip()
                                        if not (cantidad.isdigit() and int(cantidad) > 0):
                                            print("ERROR! Ingrese un número entero positivo.")
                                            continue
                                        cantidad = int(cantidad)
                                        if ejemplares[idx] + cantidad <= stock_inicial[idx]:
                                            ejemplares[idx] += cantidad
                                            print("\nDEVOLUCIÓN EXITOSA")
                                            print(f"Nuevo stock para '{titulos[idx]}' = {ejemplares[idx]}")
                                            break
                                        else:
                                            limite = stock_inicial[idx] - ejemplares[idx]
                                            print(f"\nERROR! No puede devolver {cantidad}. Máximo permitido ahora: {limite}")
                                            continue
                                    break  # operación válida realizada

                repetir = input("\n¿Desea realizar otra actualización sobre otro título? (s/n): ").strip().lower()
                while repetir not in ["s","n"]:
                    repetir = input("ERROR! Ingrese 's' o 'n': ").strip().lower()
            input("\nPRESIONE ENTER PARA VOLVER AL MENÚ...")

        case "8" | "exit" | "Exit" | "EXIT":
            limpiar()
            print("FIN DE PROGRAMA\n")
