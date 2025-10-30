"""
Segunda Parcial - Programación 1
La biblioteca escolar necesita modernizar su forma de administrar el catálogo de libros 
y el stock de ejemplares disponibles. Tu tarea es desarrollar una aplicación de consola 
en Python que permita cargar, consultar y actualizar el inventario de manera sencilla, 
manteniendo registros persistentes en un archivo CSV.

"""
import csv
import os

# Validaciones
def normalizar_titulo(t: str) -> str: 
    return " ".join(t.strip().split())

def titulo_valido(t: str) -> bool:
    return bool(normalizar_titulo(t))

def leer_entero_no_negativo(mensaje: str) -> int:
    while True:
        dato = input(mensaje).strip()
        if dato.isdigit():
            return int(dato)
        print("ERROR: Ingrese un número entero mayor o igual a 0")

def leer_entero_positivo(mensaje: str) -> int:
    while True:
        dato = input(mensaje).strip()
        if dato.isdigit() and int(dato) > 0:
            return int(dato)
        print("ERROR: Ingrese un número entero mayor a 0")

# Funciones para consola
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPRESIONE ENTER PARA CONTINUAR")

# Persistencia CSV
def cargar_catalogo_csv(ruta_csv: str): # Esta función carga un catálogo desde CSV, si no existe, devuelve una lista vacía
    catalogo = []
    if not os.path.exists(ruta_csv):
        return catalogo
    with open(ruta_csv, 'r', newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            titulo = normalizar_titulo(fila.get('TITULO', ''))
            cant_txt = fila.get('CANTIDAD', '').strip()
            if not cant_txt.isdigit():
                continue  # se descartan filas inválidas
            cantidad = int(cant_txt)
            if cantidad < 0:
                cantidad = 0
            if titulo:
                catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
    return catalogo

def guardar_catalogo_csv(ruta_csv: str, catalogo): 
    with open(ruta_csv, 'w', newline='', encoding='utf-8') as f:
        campos = ['TITULO', 'CANTIDAD']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for libro in catalogo:
            escritor.writerow({"TITULO": libro["TITULO"], "CANTIDAD": int(libro["CANTIDAD"])})

def crear_csv_si_no_existe(ruta_csv: str):
    if not os.path.exists(ruta_csv):
        with open(ruta_csv, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=['TITULO', 'CANTIDAD'])
            escritor.writeheader()

# Búsqueda
def buscar_indice_por_titulo(catalogo, titulo_busqueda: str) -> int:
    t_norm = normalizar_titulo(titulo_busqueda).lower()
    for i, item in enumerate(catalogo):
        if item["TITULO"].lower() == t_norm:
            return i
    return -1

# OPERACIONES DEL MENÚ
# Opción 1
def ingresar_titulos(catalogo, ruta_csv: str):
    limpiar_pantalla()
    print("--- OPCIÓN 1 - INGRESAR TÍTULOS ---")
    n = leer_entero_no_negativo("\n¿Cuántos libros desea cargar? (0 cancela): ")
    if n == 0:
        print("\nOperación cancelada.")
        return
    agregados = 0
    for i in range(1, n + 1):
        print(f"\nLibro {i}/{n}")
        # Título
        while True:
            titulo_in = input("TÍTULO: ").strip()
            if not titulo_valido(titulo_in):
                print("  -> ERROR: El título no puede estar vacío.")
                continue
            titulo = normalizar_titulo(titulo_in)
            if buscar_indice_por_titulo(catalogo, titulo) != -1:
                print(f"  -> ERROR: '{titulo}' ya existe en el catálogo.")
                continue
            break
        # Cantidad
        cantidad = leer_entero_no_negativo("CANTIDAD (>= 0): ")
        catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
        agregados += 1
        print(f"  -> Agregado: '{titulo}' con {cantidad} ejemplares.")
    guardar_catalogo_csv(ruta_csv, catalogo)
    print(f"\nCarga finalizada. Libros agregados: {agregados}. (Guardado en CSV)")


# Opción 2
def ingresar_ejemplares(catalogo, ruta_csv: str):
    limpiar_pantalla()
    print("--- OPCIÓN 2 - INGRESAR EJEMPLARES ---")
    if not catalogo:
        print("\nNo hay títulos cargados. Use la opción 1 o 6 para agregar libros.")
        return
    titulo_in = input("\nIngrese el TÍTULO al que desea sumar ejemplares: ").strip()
    if not titulo_valido(titulo_in):
        print("ERROR: el título no puede estar vacío.")
        return
    titulo = normalizar_titulo(titulo_in)
    idx = buscar_indice_por_titulo(catalogo, titulo)
    if idx == -1:
        print(f"\nEl libro '{titulo}' no está en el catálogo.")
        return
    sumar = leer_entero_no_negativo("Cantidad a agregar (>= 0): ")
    catalogo[idx]["CANTIDAD"] = int(catalogo[idx]["CANTIDAD"]) + sumar
    guardar_catalogo_csv(ruta_csv, catalogo)
    print(f"\nActualizado: '{catalogo[idx]['TITULO']}' ahora tiene {catalogo[idx]['CANTIDAD']} ejemplares. (Guardado)")

# Opción 3
def mostrar_catalogo(catalogo):
    limpiar_pantalla()
    print("--- OPCIÓN 3 - MOSTRAR CATÁLOGO ---\n")
    if not catalogo:
        print("El catálogo está vacío.")
        return
    print(f"{'TÍTULO':60} | {'CANTIDAD':8}")
    print("-" * 72)
    for item in catalogo:
        print(f"{item['TITULO'][:60]:60} | {int(item['CANTIDAD']):8d}")

# Opción 4
def consultar_disponibilidad(catalogo):
    limpiar_pantalla()
    print("--- OPCIÓN 4 - CONSULTAR DISPONIBILIDAD ---")
    if not catalogo:
        print("\nEl catálogo está vacío.")
        return
    titulo_in = input("\nIngrese el TÍTULO a consultar: ").strip()
    if not titulo_valido(titulo_in):
        print("ERROR: el título no puede estar vacío.")
        return
    titulo = normalizar_titulo(titulo_in)
    idx = buscar_indice_por_titulo(catalogo, titulo)
    if idx == -1:
        print(f"\nEl libro '{titulo}' no está en el catálogo.")
    else:
        cant = int(catalogo[idx]["CANTIDAD"])
        print(f"\nDISPONIBILIDAD de '{catalogo[idx]['TITULO']}': {cant} ejemplar(es).")

# Opción 5
def listar_agotados(catalogo):
    limpiar_pantalla()
    print("--- OPCIÓN 5 - LISTAR AGOTADOS ---\n")
    if not catalogo:
        print("El catálogo está vacío")
        return
    agotados = [item for item in catalogo if int(item["CANTIDAD"]) == 0]
    if not agotados:
        print("No hay libros agotados")
    else:
        print(f"{'TÍTULO':60} | {'CANTIDAD':8}")
        print("-" * 72)
        for item in agotados:
            print(f"{item['TITULO'][:60]:60} | {int(item['CANTIDAD']):8d}")
        print(f"\nTotal de libros agotados: {len(agotados)}")

# Opción 6
def agregar_titulo(catalogo, ruta_csv: str):
    limpiar_pantalla()
    print("OPCIÓN 6 - AGREGAR TÍTULO (UNO)")
    # Título
    while True:
        titulo_in = input("\nTÍTULO: ").strip()
        if not titulo_valido(titulo_in):
            print("ERROR: El título no puede estar vacío, intente nuevamente")
            continue
        titulo = normalizar_titulo(titulo_in)
        if buscar_indice_por_titulo(catalogo, titulo) != -1:
            print(f"ERROR: El título '{titulo}' ya existe, intente con otro título")
            continue
        break
    # Cantidad
    cantidad = leer_entero_no_negativo("CANTIDAD (>= 0): ")
    catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
    guardar_catalogo_csv(ruta_csv, catalogo)
    print(f"\nSe agregó '{titulo}' con {cantidad} ejemplares")

# Opción 7
def prestamo_devolucion(catalogo, ruta_csv: str):
    limpiar_pantalla()
    print("--- OPCIÓN 7 - PRÉSTAMO / DEVOLUCIÓN ---")
    if not catalogo:
        print("\nEl catálogo está vacío")
        return
    titulo_in = input("\nIngrese el TÍTULO: ").strip()
    if not titulo_valido(titulo_in):
        print("ERROR: El título no puede estar vacío")
        return
    titulo = normalizar_titulo(titulo_in)
    idx = buscar_indice_por_titulo(catalogo, titulo)
    if idx == -1:
        print(f"\nEl libro '{titulo}' no está en el catálogo")
        return

    while True:
        print(f"\nSeleccionado: '{catalogo[idx]['TITULO']}' | Stock actual: {catalogo[idx]['CANTIDAD']}")
        operacion = input("¿Préstamo (p) o Devolución (d)? (p/d, otro para salir): ").strip().lower()
        match operacion:
            case 'p':
                # Préstamo: restar 1 solo si CANTIDAD > 0
                if int(catalogo[idx]["CANTIDAD"]) > 0:
                    catalogo[idx]["CANTIDAD"] = int(catalogo[idx]["CANTIDAD"]) - 1
                    guardar_catalogo_csv(ruta_csv, catalogo)
                    print("Préstamo registrado, stock actualizado")
                else:
                    print("No hay ejemplares disponibles para prestar")
            case 'd':
                # Devolución: sumar 1
                catalogo[idx]["CANTIDAD"] = int(catalogo[idx]["CANTIDAD"]) + 1
                guardar_catalogo_csv(ruta_csv, catalogo)
                print("Devolución registrada, stock actualizado")
            case _:
                print("Fin de actualización para este título")
                break

# Función menú 
def mostrar_menu():
    print("----- BIBLIOTECA UTN -----")
    print("    ***** MENÚ *****\n")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título (uno)")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir\n")


# EJECUCIÓN DEL MAIN
ruta_csv = "catalogo.csv"  
crear_csv_si_no_existe(ruta_csv)
catalogo = cargar_catalogo_csv(ruta_csv)

opcion = ""

while opcion not in ("8", "exit", "Exit", "EXIT", "salir", "SALIR"):
    
    limpiar_pantalla()
    mostrar_menu()
    opcion = input("Ingrese una opción: ").strip()
    
    if opcion.lower() in ("exit", "salir"):
        opcion = "8"
    
    match opcion:
        case "1":
            ingresar_titulos(catalogo, ruta_csv)
            pausar()
        case "2":
            ingresar_ejemplares(catalogo, ruta_csv)
            pausar()
        case "3":
            mostrar_catalogo(catalogo)
            pausar()
        case "4":
            consultar_disponibilidad(catalogo)
            pausar()
        case "5":
            listar_agotados(catalogo)
            pausar()
        case "6":
            agregar_titulo(catalogo, ruta_csv)
            pausar()
        case "7":
            prestamo_devolucion(catalogo, ruta_csv)
            pausar()
        case "8":
            limpiar_pantalla()
            print("FIN DE PROGRAMA\n")
        case _:
            print("Opción inválida. Ingrese un número del 1 al 8.")
            pausar()
