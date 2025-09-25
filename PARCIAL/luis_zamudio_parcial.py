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

print("------ BIBLIOTECA UTN ------")
while select != "8":
    # Limpiar pantalla
    if os.name == 'nt': 
        _ = os.system('cls')
    else: 
        _ = os.system('clear')

    print("***** MENU *****")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")
    
    # Ingreso de opción
    select = input("Ingrese que opción desea realizar: ")
    
    # Validación de datos de ingreso
    while select not in ["1","2","3","4","5","6","7","8"]:
        select = input("Opción incorrecta, ingrese nuevamente: ")
    
    #print(f"Usted ha ingresado la oción {select}")

    match select:
        case "1":
            # Limpiar pantalla
            if os.name == 'nt': _ = os.system('cls')
            else: _ = os.system('clear')

            print("OPCIÓN 1 - INGRESAR TÍTULOS")
            
            while True:
                nombre = input("Ingrese título: ")
                titulos.append(nombre)

                while True: 
                    opcion = input("¿Desea agregar otro título? (s/n): ")
                    if opcion.lower() in ["s", "n"]:
                        break
                    else: 
                        print("Error, ingrese solo 's' o 'n' para continuar:  ")
                    
                if opcion.lower() == "n":
                        break

            print("\nSe terminaron de agregar títulos.")
            input("PRESIONE ENTER PARA VOLVER AL MENÚ...")

        case "2":
            print("OPCIÓN 2 - INGRESAR EJEMPLARES")
            

        case "3":
            print("OPCIÓN 3 - MOSTRAR CATÁLOGO")
            

        case "4":
            print("OPCIÓN 4 - CONSULTAR DISPONIBILIDAD")
            

        case "5":
            print("OPCIÓN 5 - LISTAR AGOTADOS")
            

        case "6":
            print("OPCIÓN 6 - AGREGAR TÍTULO")
            

        case "7":
            print("OPCIÓN 7 - ACTUALIZAR EJEMPLARES (Préstamo / Devolución)")
            
            
        case "8":
            print("OPCIÓN 8 - Salir")
    
            
        case _:
            input("Opción incorrecta: ingrese nuevamente: ")
            
            
        