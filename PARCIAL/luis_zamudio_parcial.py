# La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las
# copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que
# utilice listas paralelas (una para titulos[] y otra para ejemplares[]). Cada título debe estar
# vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas.
# Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario
# elija salir.

# 1. Ingresar títulos → permite agregar los títulos de los libros.
# 2. Ingresar ejemplares → cantidad de copias para cada título.
# 3. Mostrar catálogo → muestra todos los libros con su stock.
# 4. Consultar disponibilidad → busca un título y muestra cuántos ejemplares hay.
# 5. Listar agotados → muestra los títulos con 0 ejemplares.
# 6. Agregar título → permite sumar un nuevo libro al catálogo.
# 7. Actualizar ejemplares (préstamo/devolución) → modifica el stock.
# 8. Salir → termina el programa.

import os

titulos = []
ejemplares = []
select = ""
opcion = "s"

while select != "8" and select != "exit" and select != "Exit" and select != "EXIT":
    # Limpiar pantalla
    if os.name == 'nt': 
        _ = os.system('cls')
    else: 
        _ = os.system('clear')
    
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

    # Ingreso de opción
    select = input("Ingrese que opción desea realizar: ")
    
    # Validación de datos de ingreso
    while select not in ["1","2","3","4","5","6","7","8", "exit", "Exit", "EXIT"]:
        select = input("Opción incorrecta, ingrese nuevamente: ")
    
    #print(f"Usted ha ingresado la oción {select}")

    match select:

        case "1": # 1. Ingresar títulos → permite agregar los títulos de los libros.

            # Limpiar pantalla
            if os.name == 'nt': _ = os.system('cls')
            else: _ = os.system('clear')

            print("OPCIÓN 1 - INGRESAR TÍTULOS")
            
            while True:
                nombre = input("\nINGRESE TÍTULO: ").strip() # Se eliminan los espacios extra

                # Verificaciones
                if not nombre: # Se chequea que el no hay texto vacío
                    print("\nERROR! el campo no puede estar vacío")
                    continue # Vuelve al inicio del bucle

                titulos_existentes = [] # Con esta lista se verificará que no haya títulos repetidos
                for i in titulos:
                    titulo_minuscula = i.lower() # Se pasa todo a minúscula para hacer la comparación
                    titulos_existentes.append(titulo_minuscula)
                
                if nombre.lower() in titulos_existentes:
                    print(f"\nERROR! El título '{nombre}' ya existe, ingrese otro nombre")
                    continue
                
                # Al finalizar las verificaciones se agrega el título a la lista
                titulos.append(nombre)
                print(f"\n'{nombre}' fue agregado al catálogo de la Biblioteca Universitaria")

                while True: 
                    opcion = input("\n¿Desea agregar otro título? (s/n): ")
                    if opcion.lower() in ["s", "n"]:
                        break # Se termina el ciclo para volver al inicio del while
                    else: 
                        print("\nERROR! Ingrese solo 's' o 'n' para continuar:  ")
                    
                if opcion.lower() == "n":
                        break

            print("\nSe terminaron de agregar títulos\n")
            input("PRESIONE ENTER PARA VOLVER AL MENÚ...")


        case "2": # 2. Ingresar ejemplares → cantidad de copias para cada título.

            # Limpiar la pantalla nuevamente
            if os.name == 'nt': _ = os.system('cls')
            else: _ = os.system('clear')

            print("--- OPCIÓN 2 - INGRESAR EJEMPLARES ---")

            if not titulos: # Este if previene ingresar a este case si hoy hay títulos cargados previamente
                print("\nERROR! Debe cargar títulos primero, seleccione la opción 1")
            elif len(titulos) == len(ejemplares):
                print("\nCada título ya tiene cargada su cantidad de ejemplares correspondiente")
            else:
                print("\nIngrese la cantidad de ejemplares en los siguientes títulos: ")

                indice = len(ejemplares)

                for i in range(len(ejemplares), len(titulos)):
                    titulo_aux = titulos[i]
                    while True:
                        cantidad_copias = input(f"\nINGRESE CANTIDAD DE EJEMPLARES PARA '{titulos[i]}': ")
                        if cantidad_copias.isdigit():
                            break
                        else:
                            print("\nError! ingrese un número válido\n")
                    
                    ejemplares.append(int(cantidad_copias))
                
                print("\n            --- RESUMEN ---\n")
                
                for i in range(indice, len(titulos)):
                    titulo_agregado = titulos[i]
                    copias_agregadas = ejemplares[i]
                    print(f"Se agregaron {copias_agregadas} ejemplares al título '{titulo_agregado}'")

            input("\nPRESIONE ENTER PARA VOLVER AL MENÚ...")


        case "3": # 3. Mostrar catálogo → muestra todos los libros con su stock.
            
            # Limpiar pantalla
            if os.name == 'nt': _ = os.system('cls')
            else: _ = os.system('clear')

            print("--- OPCIÓN 3 - MOSTRAR CATÁLOGO ---")

            if not titulos:  # Se verifica que la lista de títulos no esté vacía
                print("\nERROR! El catálogo está vacío. Agregue títulos primero (Opción 1).")

            elif len(titulos) != len(ejemplares): # Se verifica que ambas listas tengan la misma longitud. Si no, hay títulos sin ejemplares.
                print("\nERROR! Faltan ingresar los ejemplares de algunos títulos (Opción 2).")
           
            else:
                print("\n--- CATÁLOGO DE LA BIBLIOTECA ---\n")
                for i in range(len(titulos)):
                    nombre_titulo = titulos[i]
                    cantidad_ejemplares = ejemplares[i]
                    print(f"-> Título: '{nombre_titulo}' | Stock: {cantidad_ejemplares} ejemplares")
            
            input("\nPRESIONE ENTER PARA VOLVER AL MENÚ...")
            

        case "4": # 4. Consultar disponibilidad → busca un título y muestra cuántos ejemplares hay.

            if os.name == 'nt': _ = os.system('cls')
            else: _ = os.system('clear')

            print("--- OPCIÓN 4 - CONSULTAR DISPONIBILIDAD POR TÍTULO ---")

            if not titulos: # Verificaciones
                print("\nEl catálogo está vacío. Ingrese títulos con la Opción 1 primero.")
            else:
                titulo_buscado = input("\nIngrese el título del libro que desea buscar: ").strip()

                if not titulo_buscado:
                    print("\nERROR! El nombre del título no puede estar vacío.")
                else:
                    encontrado = False
                    for i in range(len(titulos)): # Se recorre la lista para buscar la conicidencia
                        if titulos[i].lower() == titulo_buscado.lower():
                            encontrado = True # Bandera
                            
                            # En este bloque se verificará que el título tenga ejemplares cargados
                            if i < len(ejemplares):
                                print("----- LIBRO ENCONTRADO -----")
                                print(f"\nDISPONIBILIDAD de '{titulos[i]}' = {ejemplares[i]} ejemplares")
                            else:
                                print("----- TÍTULO ENCONTRADO PERO INCOMPLETO -----")
                                print(f"\nEl título '{titulos[i]}' está en el catálogo, pero aún no se han cargado la cantidad de ejemplares")
                                print("Por favor, use la Opción 2 para agregarlos")
                            break
                    
                    if not encontrado:
                        print(f"\nEl libro '{titulo_buscado}' no se encuentra en el catálogo")

            input("\nPRESIONE ENTER PARA VOLVER AL MENÚ...")

            
        case "5": # 5. Listar agotados → muestra los títulos con 0 ejemplares.

            if os.name == 'nt': _ = os.system('cls')
            else: _ = os.system('clear')

            print("--- OPCIÓN 5 - LISTAR LIBROS AGOTADOS ---")

            if not ejemplares: 
                print("\nNo hay información de ejemplares para mostrar")
                print("\nPrimero vaya a la Opción 1 para cargar los títulos y luego la Opción 2 para la cantidad ejemplares")
            else:
                agotados = []
                for i in range(len(ejemplares)):
                    if ejemplares[i] == 0:
                        agotados.append(titulos[i])

                if not agotados: 
                    print("\nNO HAY LIBROS AGOTADOS EN EL CATÁLOGO")
                    
                else: 
                    print("\n --- TÍTULOS CON STOCK 0 ---\n")
                    for titulo in agotados:
                        print(f"{titulo}")
    
            input("\nPRESIONE ENTER PARA VOLVER AL MENÚ...")
        
        case "6": # 6. Agregar título → permite sumar un nuevo libro al catálogo.
        # Se interpreta que en esta opción se podrá cargar un título solo junto con su cantida de ejemplares

            if os.name == 'nt': _ = os.system('cls')
            else: _ = os.system('clear')

            print("OPCIÓN 6 - AGREGAR TITULO") 

            nombre = input("\nINGRESE EL TÍTULO DEL NUEVO LIBRO: ").strip()

            if not nombre:
                print("\nERROR! El título no puede estar vacío")
            else:
                titulos_existentes = [titulo.lower() for titulo in titulos] 
                if nombre.lower() in titulos_existentes:
                    print(f"\nERROR! El título '{nombre}' ya existe en el catálogo")
                else:
                    while True:
                        cantidad_ejemplares = input(f"INGRESE LA CANTIDAD DE EJEMPLARES PARA '{nombre}': ")
                        if cantidad_ejemplares.isdigit() and int(cantidad_ejemplares) >= 0:
                            titulos.append(nombre)
                            ejemplares.append(int(cantidad_ejemplares))
                            print(f"\nSe agregó correctamente el título '{nombre}' con {cantidad_ejemplares} ejemplares al catálogo")
                            break
                        else:
                            print("ERROR! Ingrese un número entero válido (0 o mayor a 0)")
            
            input("\nPRESIONE ENTER PARA VOLVER AL MENÚ...")


        case "7": # 7. Actualizar ejemplares (préstamo/devolución) → modifica el stock.

            if os.name == 'nt': _ = os.system('cls')
            else: _ = os.system('clear')

            print("--- OPCIÓN 7 - ACTUALIZAR EJEMPLARES (PRÉSTAMO / DEVOLUCIÓN) ---")

            if not titulos or len(titulos) != len(ejemplares):
                print("\nEl catálogo está vacío o incompleto, no se pueden realizar operaciones")
                print("\nVaya a la Opción 1 para cargar títulos y luego a la opción 2 para la cantidad de ejemplares")
            else:
                titulo_buscado = input("\nIngrese el título del libro a actualizar: ").strip()
                
                if not titulo_buscado:
                    print("\nERROR! El título no puede estar vacío")
                else:
                    indice_encontrado = -1 # Se inicializa en -1 para que se asuma que no hay ninguan posición válida, que van de 0 en adelante
                    
                    # Busqueda del índice del libro
                    for i in range(len(titulos)):
                        if titulos[i].lower() == titulo_buscado.lower():
                            indice_encontrado = i
                            break
                    
                    if indice_encontrado == -1: 
                        print(f"\nERROR! El libro '{titulo_buscado}' no se encuentra en el catálogo")
                    
                    else:
                        # Si se encuentra el libro se muestra el estado actual
                        print(f"\nLibro seleccionado: '{titulos[indice_encontrado]}' | Stock actual: {ejemplares[indice_encontrado]}")
                        
                        operacion = ""
                        # En est bloque se decide que operación se va a realizar: préstamo o devolución y valida el ingreso
                        while operacion not in ['p', 'd']:
                            operacion = input("\n¿Desea realizar un préstamo o una devolución? Ingrese la opción: (p / d): ").lower().strip()
                            if operacion not in ['p', 'd']:
                                print("\nError! Opción inválida, intente de nuevo ")
                        
                        # Prestamo
                        if operacion == 'p': 
                            if ejemplares[indice_encontrado] == 0:
                                print("\nNo hay ejemplares disponibles para prestar")
                            else:
                                while True:
                                    cantidad_ejemplares = input("Ingrese la cantidad a prestar: ")
                                    if cantidad_ejemplares.isdigit() and int(cantidad_ejemplares) > 0:
                                        cantidad = int(cantidad_ejemplares)
                                        if cantidad <= ejemplares[indice_encontrado]:
                                            ejemplares[indice_encontrado] -= cantidad
                                            print(f"\nPRÉSTAMO EXITOSO")
                                            print(f"\nNuevo stock para {titulos[indice_encontrado]} = {ejemplares[indice_encontrado]}")
                                            break
                                        else:
                                            print(f"\nERROR! No se pueden prestar {cantidad} ejemplares. Solo hay {ejemplares[indice_encontrado]} disponibles")
                                    else:
                                        print("\nERROR! Ingrese un número entero positivo")
                        # Devolución
                        elif operacion == 'd':
                            while True:
                                cantidad_ejemplares = input("\nIngrese la cantidad a devolver: ")
                                if cantidad_ejemplares.isdigit() and int(cantidad_ejemplares) > 0:
                                    cantidad = int(cantidad_ejemplares)
                                    ejemplares[indice_encontrado] += cantidad
                                    print(f"\nDEVOLUCIÓN EXITOSA")
                                    print(f"Nuevo stock para {titulos[indice_encontrado]} = {ejemplares[indice_encontrado]}")
                                    break
                                else:
                                    print("Error: Ingrese un número entero positivo.")
            
            input("\nPRESIONE ENTER PARA VOLVER AL MENÚ...")
            
        case "8": # 8. Salir → termina el programa.

            if os.name == 'nt': _ = os.system('cls')
            else: _ = os.system('clear')
            
            print("FIN DE PROGRAMA\n")
            
        
        case "exit": # exit. Salir → termina el programa.

            if os.name == 'nt': _ = os.system('cls')
            else: _ = os.system('clear')
            
            print("FIN DE PROGRAMA\n")
        
        case "Exit": # Exit. Salir → termina el programa.

            if os.name == 'nt': _ = os.system('cls')
            else: _ = os.system('clear')
            
            print("FIN DE PROGRAMA\n")
        
        case "EXIT": # EXIT. Salir → termina el programa.

            if os.name == 'nt': _ = os.system('cls')
            else: _ = os.system('clear')
            
            print("FIN DE PROGRAMA\n")
        # El case _: o default: es redundante, ya que la condición del while de línea 46 impide cualquier ingreso distinto del rango
            
            
        