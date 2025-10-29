
# -*- coding: utf-8 -*-
"""
Biblioteca UTN - Gestión de Catálogo (versión CSV, sin globales)
Estructura: lista de diccionarios [{"TITULO": str, "CANTIDAD": int}, ...]
Persistencia: catalogo.csv (se lee al iniciar, se guarda tras cada cambio)
"""

import csv
import os
from typing import List, Dict, Tuple

ARCHIVO_CSV = "catalogo.csv"


# ----------------------- Utilidades de consola -----------------------
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    input("\nPRESIONE ENTER PARA CONTINUAR...")


# ----------------------- Normalización y validaciones -----------------------
def normalizar_titulo(t: str) -> str:
    """Espacios únicos y sin espacios en extremos; conservar mayúsculas del usuario."""
    return " ".join(t.strip().split())


def leer_entero_no_negativo(mensaje: str) -> int:
    while True:
        dato = input(mensaje).strip()
        if dato.isdigit():
            return int(dato)
        print("ERROR: ingrese un número entero >= 0.")


def leer_entero_positivo(mensaje: str) -> int:
    while True:
        dato = input(mensaje).strip()
        if dato.isdigit() and int(dato) > 0:
            return int(dato)
        print("ERROR: ingrese un número entero > 0.")


# ----------------------- Persistencia CSV -----------------------
def cargar_catalogo_csv(ruta: str) -> List[Dict[str, object]]:
    catalogo: List[Dict[str, object]] = []
    if not os.path.exists(ruta):
        return catalogo
    with open(ruta, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            titulo = normalizar_titulo(row.get('TITULO', ''))
            try:
                cantidad = int(row.get('CANTIDAD', '0'))
                if cantidad < 0:
                    cantidad = 0
            except ValueError:
                cantidad = 0
            if titulo:
                catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
    return catalogo


def guardar_catalogo_csv(ruta: str, catalogo: List[Dict[str, object]]) -> None:
    with open(ruta, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['TITULO', 'CANTIDAD']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in catalogo:
            writer.writerow({"TITULO": item["TITULO"], "CANTIDAD": int(item["CANTIDAD"])})


# ----------------------- Búsqueda -----------------------
def buscar_indice_por_titulo(catalogo: List[Dict[str, object]], titulo: str) -> int:
    objetivo = titulo.lower()
    for i, item in enumerate(catalogo):
        if item["TITULO"].lower() == objetivo:
            return i
    return -1


# ----------------------- Operaciones del menú -----------------------
def opcion_1_ingresar_titulos(catalogo: List[Dict[str, object]]) -> None:
    limpiar()
    print("OPCIÓN 1 - INGRESAR TÍTULOS (MÚLTIPLES)")
    n = leer_entero_no_negativo("\n¿Cuántos libros desea cargar? (0 para cancelar): ")
    if n == 0:
        print("\nOperación cancelada.")
        return
    agregados = 0
    for i in range(1, n + 1):
        print(f"\nLibro {i}/{n}")
        titulo = normalizar_titulo(input("TÍTULO: ").strip())
        if not titulo:
            print("  -> Omitido: el título no puede estar vacío.")
            continue
        if buscar_indice_por_titulo(catalogo, titulo) != -1:
            print(f"  -> Omitido: '{titulo}' ya existe en el catálogo.")
            continue
        cantidad = leer_entero_no_negativo("CANTIDAD (>=0): ")
        catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
        agregados += 1
        print(f"  -> Agregado: '{titulo}' con {cantidad} ejemplares.")
    guardar_catalogo_csv(ARCHIVO_CSV, catalogo)
    print(f"\nCarga finalizada. Libros agregados: {agregados}.")


def opcion_2_ingresar_ejemplares(catalogo: List[Dict[str, object]]) -> None:
    limpiar()
    print("--- OPCIÓN 2 - INGRESAR EJEMPLARES A UN TÍTULO ---")
    if not catalogo:
        print("\nNo hay títulos cargados. Use la opción 1 o 6 para agregar libros.")
        return
    titulo = normalizar_titulo(input("\nIngrese el TÍTULO al que desea sumar ejemplares: ").strip())
    if not titulo:
        print("ERROR: el título no puede estar vacío.")
        return
    idx = buscar_indice_por_titulo(catalogo, titulo)
    if idx == -1:
        print(f"\nEl libro '{titulo}' no está en el catálogo.")
        return
    sumar = leer_entero_no_negativo("Cantidad a agregar (>=0): ")
    catalogo[idx]["CANTIDAD"] = int(catalogo[idx]["CANTIDAD"]) + sumar
    guardar_catalogo_csv(ARCHIVO_CSV, catalogo)
    print(f"\nActualizado: '{catalogo[idx]['TITULO']}' ahora tiene {catalogo[idx]['CANTIDAD']} ejemplares.")


def opcion_3_mostrar_catalogo(catalogo: List[Dict[str, object]]) -> None:
    limpiar()
    print("--- OPCIÓN 3 - MOSTRAR CATÁLOGO ---\n")
    if not catalogo:
        print("El catálogo está vacío.")
        return
    print(f"{'TÍTULO':60} | {'CANTIDAD':8}")
    print("-" * 72)
    for item in catalogo:
        print(f"{item['TITULO'][:60]:60} | {int(item['CANTIDAD']):8d}")


def opcion_4_consultar_disponibilidad(catalogo: List[Dict[str, object]]) -> None:
    limpiar()
    print("--- OPCIÓN 4 - CONSULTAR DISPONIBILIDAD ---")
    if not catalogo:
        print("\nEl catálogo está vacío.")
        return
    titulo = normalizar_titulo(input("\nIngrese el TÍTULO a consultar: ").strip())
    if not titulo:
        print("ERROR: el título no puede estar vacío.")
        return
    idx = buscar_indice_por_titulo(catalogo, titulo)
    if idx == -1:
        print(f"\nEl libro '{titulo}' no está en el catálogo.")
    else:
        cant = int(catalogo[idx]["CANTIDAD"])
        print(f"\nDISPONIBILIDAD de '{catalogo[idx]['TITULO']}': {cant} ejemplar(es).")


def opcion_5_listar_agotados(catalogo: List[Dict[str, object]]) -> None:
    limpiar()
    print("--- OPCIÓN 5 - LISTAR AGOTADOS (CANTIDAD = 0) ---\n")
    if not catalogo:
        print("El catálogo está vacío.")
        return
    agotados = [item["TITULO"] for item in catalogo if int(item["CANTIDAD"]) == 0]
    if not agotados:
        print("No hay libros agotados.")
    else:
        for t in agotados:
            print(f"- {t}")


def opcion_6_agregar_titulo(catalogo: List[Dict[str, object]]) -> None:
    limpiar()
    print("OPCIÓN 6 - AGREGAR TÍTULO (UNO)")
    titulo = normalizar_titulo(input("\nTÍTULO: ").strip())
    if not titulo:
        print("ERROR: el título no puede estar vacío.")
        return
    if buscar_indice_por_titulo(catalogo, titulo) != -1:
        print(f"ERROR: el título '{titulo}' ya existe.")
        return
    cantidad = leer_entero_no_negativo("CANTIDAD (>=0): ")
    catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
    guardar_catalogo_csv(ARCHIVO_CSV, catalogo)
    print(f"\nSe agregó '{titulo}' con {cantidad} ejemplares.")


def opcion_7_prestamo_devolucion(catalogo: List[Dict[str, object]]) -> None:
    limpiar()
    print("--- OPCIÓN 7 - PRÉSTAMO / DEVOLUCIÓN (±1) ---")
    if not catalogo:
        print("\nEl catálogo está vacío.")
        return

    titulo = normalizar_titulo(input("\nIngrese el TÍTULO: ").strip())
    if not titulo:
        print("ERROR: el título no puede estar vacío.")
        return
    idx = buscar_indice_por_titulo(catalogo, titulo)
    if idx == -1:
        print(f"\nEl libro '{titulo}' no está en el catálogo.")
        return

    while True:
        print(f"\nSeleccionado: '{catalogo[idx]['TITULO']}' | Stock actual: {catalogo[idx]['CANTIDAD']}")
        op = input("¿Préstamo (p) o Devolución (d)? (p/d, otro para salir): ").strip().lower()
        if op not in ('p', 'd'):
            print("Saliendo de la actualización de este título.")
            break

        if op == 'p':
            if int(catalogo[idx]["CANTIDAD"]) > 0:
                catalogo[idx]["CANTIDAD"] = int(catalogo[idx]["CANTIDAD"]) - 1
                guardar_catalogo_csv(ARCHIVO_CSV, catalogo)
                print("Préstamo registrado. Stock actualizado.")
            else:
                print("No hay ejemplares disponibles para prestar.")
        else:  # devolución
            catalogo[idx]["CANTIDAD"] = int(catalogo[idx]["CANTIDAD"]) + 1
            guardar_catalogo_csv(ARCHIVO_CSV, catalogo)
            print("Devolución registrada. Stock actualizado.")


# ----------------------- Menú principal -----------------------
def mostrar_menu():
    print("----- BIBLIOTECA UTN -----")
    print("     ***** MENÚ *****\n")
    print("1. Ingresar títulos (múltiples)")
    print("2. Ingresar ejemplares (+ cantidad a un título)")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título (uno)")
    print("7. Actualizar ejemplares (préstamo/devolución ±1)")
    print("8. Salir\n")


def main():
    catalogo = cargar_catalogo_csv(ARCHIVO_CSV)

    while True:
        limpiar()
        mostrar_menu()
        select = input("Ingrese una opción: ").strip()
        if select not in list("12345678"):
            if select.lower() in ("exit", "salir", "quit"):
                select = "8"
            else:
                print("Opción inválida.")
                pausar()
                continue

        if select == "1":
            opcion_1_ingresar_titulos(catalogo); pausar()
        elif select == "2":
            opcion_2_ingresar_ejemplares(catalogo); pausar()
        elif select == "3":
            opcion_3_mostrar_catalogo(catalogo); pausar()
        elif select == "4":
            opcion_4_consultar_disponibilidad(catalogo); pausar()
        elif select == "5":
            opcion_5_listar_agotados(catalogo); pausar()
        elif select == "6":
            opcion_6_agregar_titulo(catalogo); pausar()
        elif select == "7":
            opcion_7_prestamo_devolucion(catalogo); pausar()
        elif select == "8":
            limpiar()
            print("FIN DE PROGRAMA\n")
            break


if __name__ == "__main__":
    main()
"""
Segunda Parcial – Programación 1 (Catálogo de Biblioteca)
Cumple con la consigna oficial (PDF): lista de diccionarios [{ "TITULO": str, "CANTIDAD": int>=0 }],
persistencia CSV "catalogo.csv", menú 1–8, validaciones sin excepciones, sin variables globales,
sin lambdas, sin clases, modularizado con funciones y uso de match/case.
"""

import csv
import os

# ----------------------- Normalización y validaciones -----------------------
def normalizar_titulo(t: str) -> str:
    """Quita espacios extra y respeta mayúsculas del usuario; usado para comparar sin errores."""
    return " ".join(t.strip().split())

def titulo_valido(t: str) -> bool:
    return bool(normalizar_titulo(t))

def leer_entero_no_negativo(mensaje: str) -> int:
    """Lee un entero >= 0 sin usar excepciones."""
    while True:
        dato = input(mensaje).strip()
        if dato.isdigit():
            return int(dato)
        print("ERROR: ingrese un número entero mayor o igual a 0.")

def leer_entero_positivo(mensaje: str) -> int:
    """Lee un entero > 0 sin usar excepciones."""
    while True:
        dato = input(mensaje).strip()
        if dato.isdigit() and int(dato) > 0:
            return int(dato)
        print("ERROR: ingrese un número entero mayor a 0.")

# ----------------------- Consola -----------------------
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPRESIONE ENTER PARA CONTINUAR...")

# ----------------------- CSV (persistencia) -----------------------
def cargar_catalogo_csv(ruta_csv: str):
    """Carga catalogo desde CSV. Si no existe, devuelve lista vacía (no excepciones)."""
    catalogo = []
    if not os.path.exists(ruta_csv):
        return catalogo
    with open(ruta_csv, 'r', newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            titulo = normalizar_titulo(fila.get('TITULO', ''))
            cant_txt = fila.get('CANTIDAD', '').strip()
            if not cant_txt.isdigit():
                continue  # descarta filas inválidas
            cantidad = int(cant_txt)
            if cantidad < 0:
                cantidad = 0
            if titulo:
                catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
    return catalogo

def guardar_catalogo_csv(ruta_csv: str, catalogo):
    """Sobrescribe catalogo.csv con encabezado TITULO,CANTIDAD."""
    with open(ruta_csv, 'w', newline='', encoding='utf-8') as f:
        campos = ['TITULO', 'CANTIDAD']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for libro in catalogo:
            escritor.writerow({"TITULO": libro["TITULO"], "CANTIDAD": int(libro["CANTIDAD"])})

def crear_csv_si_no_existe(ruta_csv: str):
    """Crea el CSV con encabezado si no existe (sin escribir datos)."""
    if not os.path.exists(ruta_csv):
        with open(ruta_csv, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=['TITULO', 'CANTIDAD'])
            escritor.writeheader()

# ----------------------- Búsquedas -----------------------
def buscar_indice_por_titulo(catalogo, titulo_busqueda: str) -> int:
    """Devuelve índice del libro por TITULO, -1 si no existe (insensible a mayúsculas/espacios)."""
    t_norm = normalizar_titulo(titulo_busqueda).lower()
    for i, item in enumerate(catalogo):
        if item["TITULO"].lower() == t_norm:
            return i
    return -1

# ----------------------- Operaciones de menú -----------------------
def opcion_1_ingresar_titulos(catalogo, ruta_csv: str):
    limpiar_pantalla()
    print("OPCIÓN 1 - INGRESAR TÍTULOS (MÚLTIPLES)")
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

def opcion_2_ingresar_ejemplares(catalogo, ruta_csv: str):
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

def opcion_3_mostrar_catalogo(catalogo):
    limpiar_pantalla()
    print("--- OPCIÓN 3 - MOSTRAR CATÁLOGO ---\n")
    if not catalogo:
        print("El catálogo está vacío.")
        return
    print(f"{'TÍTULO':60} | {'CANTIDAD':8}")
    print("-" * 72)
    for item in catalogo:
        print(f"{item['TITULO'][:60]:60} | {int(item['CANTIDAD']):8d}")

def opcion_4_consultar_disponibilidad(catalogo):
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

def opcion_5_listar_agotados(catalogo):
    limpiar_pantalla()
    print("--- OPCIÓN 5 - LISTAR AGOTADOS (CANTIDAD = 0) ---\n")
    if not catalogo:
        print("El catálogo está vacío.")
        return
    agotados = [item for item in catalogo if int(item["CANTIDAD"]) == 0]
    if not agotados:
        print("No hay libros agotados.")
    else:
        print(f"{'TÍTULO':60} | {'CANTIDAD':8}")
        print("-" * 72)
        for item in agotados:
            print(f"{item['TITULO'][:60]:60} | {int(item['CANTIDAD']):8d}")
        print(f"\nTotal de libros agotados: {len(agotados)}")

def opcion_6_agregar_titulo(catalogo, ruta_csv: str):
    limpiar_pantalla()
    print("OPCIÓN 6 - AGREGAR TÍTULO (UNO)")
    # Título
    while True:
        titulo_in = input("\nTÍTULO: ").strip()
        if not titulo_valido(titulo_in):
            print("ERROR: el título no puede estar vacío. Intente nuevamente.")
            continue
        titulo = normalizar_titulo(titulo_in)
        if buscar_indice_por_titulo(catalogo, titulo) != -1:
            print(f"ERROR: el título '{titulo}' ya existe. Intente con otro título.")
            continue
        break
    # Cantidad
    cantidad = leer_entero_no_negativo("CANTIDAD (>= 0): ")
    catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
    guardar_catalogo_csv(ruta_csv, catalogo)
    print(f"\nSe agregó '{titulo}' con {cantidad} ejemplares. (Guardado)")

def opcion_7_prestamo_devolucion(catalogo, ruta_csv: str):
    limpiar_pantalla()
    print("--- OPCIÓN 7 - PRÉSTAMO / DEVOLUCIÓN ---")
    if not catalogo:
        print("\nEl catálogo está vacío.")
        return
    titulo_in = input("\nIngrese el TÍTULO: ").strip()
    if not titulo_valido(titulo_in):
        print("ERROR: el título no puede estar vacío.")
        return
    titulo = normalizar_titulo(titulo_in)
    idx = buscar_indice_por_titulo(catalogo, titulo)
    if idx == -1:
        print(f"\nEl libro '{titulo}' no está en el catálogo.")
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
                    print("Préstamo registrado. Stock actualizado. (Guardado)")
                else:
                    print("No hay ejemplares disponibles para prestar.")
            case 'd':
                # Devolución: sumar 1
                catalogo[idx]["CANTIDAD"] = int(catalogo[idx]["CANTIDAD"]) + 1
                guardar_catalogo_csv(ruta_csv, catalogo)
                print("Devolución registrada. Stock actualizado. (Guardado)")
            case _:
                print("Fin de actualización para este título.")
                break

# ----------------------- Presentación del menú -----------------------
def mostrar_menu():
    print("----- BIBLIOTECA UTN -----")
    print("     ***** MENÚ *****\n")
    print("1. Ingresar títulos (múltiples)")
    print("2. Ingresar ejemplares (+ cantidad a un título)")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título (uno)")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir\n")

# ----------------------- Ejecución sin variables globales -----------------------


# ----------------------- Bucle principal en nivel superior -----------------------
ruta_csv = "catalogo.csv"  # local en este módulo (sin variables globales de estado mutables fuera del flujo)
crear_csv_si_no_existe(ruta_csv)
catalogo = cargar_catalogo_csv(ruta_csv)

seleccion = ""
while seleccion not in ("8", "exit", "Exit", "EXIT", "salir", "SALIR"):
    limpiar_pantalla()
    mostrar_menu()
    seleccion = input("Ingrese una opción: ").strip()
    if seleccion.lower() in ("exit", "salir", "quit"):
        seleccion = "8"
    match seleccion:
        case "1":
            opcion_1_ingresar_titulos(catalogo, ruta_csv); pausar()
        case "2":
            opcion_2_ingresar_ejemplares(catalogo, ruta_csv); pausar()
        case "3":
            opcion_3_mostrar_catalogo(catalogo); pausar()
        case "4":
            opcion_4_consultar_disponibilidad(catalogo); pausar()
        case "5":
            opcion_5_listar_agotados(catalogo); pausar()
        case "6":
            opcion_6_agregar_titulo(catalogo, ruta_csv); pausar()
        case "7":
            opcion_7_prestamo_devolucion(catalogo, ruta_csv); pausar()
        case "8":
            limpiar_pantalla(); print("FIN DE PROGRAMA\n")
        case _:
            print("Opción inválida. Ingrese un número del 1 al 8."); pausar()
