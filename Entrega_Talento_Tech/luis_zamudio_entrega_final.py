
import sqlite3
import os
import sys

try:
    from colorama import init as colorama_init, Fore, Style
    colorama_init(autoreset=True)
    C_TITLE = Fore.CYAN + Style.BRIGHT
    C_OK = Fore.GREEN
    C_WARN = Fore.YELLOW
    C_ERR = Fore.RED
    C_RESET = Style.RESET_ALL
except Exception:
    C_TITLE = C_OK = C_WARN = C_ERR = C_RESET = ""

DB_FILE = "inventario.db"

# FUNCIONES BASICAS

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def pedir_texto(prompt, obligatorio=True):
    while True:
        valor = input(prompt).strip()
        if obligatorio and valor == "":
            print(f"{C_ERR}ERROR: no puede estar vacío.{C_RESET}")
        else:
            return valor

def pedir_entero(prompt, minimo=None, permitir_cero=True):
    while True:
        valor = input(prompt).strip()
        if valor == "":
            print(f"{C_ERR}ERROR: no puede estar vacío.{C_RESET}")
            continue
        if (valor.lstrip("-").isdigit()):
            n = int(valor)
            if minimo is not None and n < minimo:
                print(f"{C_ERR}ERROR: el número debe ser >= {minimo}.{C_RESET}")
                continue
            if not permitir_cero and n == 0:
                print(f"{C_ERR}ERROR: el valor no puede ser 0.{C_RESET}")
                continue
            return n
        else:
            print(f"{C_ERR}ERROR: ingrese un número entero válido.{C_RESET}")

def pedir_precio_entero(prompt):
    return pedir_entero(prompt, minimo=0, permitir_cero=True)

# BASE DE DATOS

def obtener_conexion():
    conn = sqlite3.connect(DB_FILE)
    return conn

def inicializar_db():
    conn = obtener_conexion()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT)
    """)
    conn.commit()
    conn.close()

# OPERACIONES CRUD

def agregar_producto_db(nombre, descripcion, cantidad, precio, categoria):
    conn = obtener_conexion()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
        """, (nombre, descripcion, cantidad, precio, categoria))
    conn.commit()
    last_id = cur.lastrowid
    conn.close()
    return last_id

def listar_productos_db():
    conn = obtener_conexion()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return rows

def buscar_producto_por_id_db(pid):
    conn = obtener_conexion()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos WHERE id = ?", (pid,))
    row = cur.fetchone()
    conn.close()
    return row

def buscar_productos_por_texto_db(texto):
    like = f"%{texto}%"
    conn = obtener_conexion()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, nombre, descripcion, cantidad, precio, categoria
        FROM productos
        WHERE nombre LIKE ? OR categoria LIKE ?
        ORDER BY id
        """, (like, like))
    rows = cur.fetchall()
    conn.close()
    return rows

def actualizar_producto_db(pid, nombre, descripcion, cantidad, precio, categoria):
    conn = obtener_conexion()
    cur = conn.cursor()
    cur.execute("""
        UPDATE productos
        SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
        WHERE id = ?
        """, (nombre, descripcion, cantidad, precio, categoria, pid))
    conn.commit()
    updated = cur.rowcount
    conn.close()
    return updated > 0

def eliminar_producto_db(pid):
    conn = obtener_conexion()
    cur = conn.cursor()
    cur.execute("DELETE FROM productos WHERE id = ?", (pid,))
    conn.commit()
    deleted = cur.rowcount
    conn.close()
    return deleted > 0

def reporte_bajo_stock_db(limite):
    conn = obtener_conexion()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, nombre, descripcion, cantidad, precio, categoria
        FROM productos
        WHERE cantidad <= ?
        ORDER BY cantidad ASC, id
        """, (limite,))
    rows = cur.fetchall()
    conn.close()
    return rows

# FUNCIONES DE INTERFAZ DE USUARIO

def accion_agregar_producto():
    limpiar_pantalla()
    print(f"{C_TITLE}AGREGAR PRODUCTO{C_RESET}\n")
    while True:
        nombre = pedir_texto("Nombre: ")
        descripcion = pedir_texto("Descripción (opcional): ", obligatorio=False)
        cantidad = pedir_entero("Cantidad (entero): ", minimo=0)
        precio = pedir_precio_entero("Precio (sin centavos, entero): ")
        categoria = pedir_texto("Categoría (opcional): ", obligatorio=False)

        existentes = buscar_productos_por_texto_db(nombre)
        repetido = False
        i = 0
        while i < len(existentes):
            row = existentes[i]
            if row[1].strip().lower() == nombre.strip().lower() and (row[5] or "").strip().lower() == (categoria or "").strip().lower():
                repetido = True
                break
            i += 1

        if repetido:
            print(f"{C_WARN}ADVERTENCIA: ese producto ya existe con la misma categoría.{C_RESET}")
        else:
            pid = agregar_producto_db(nombre, descripcion, cantidad, precio, categoria)
            print(f"{C_OK}Producto agregado con ID {pid}: {nombre} | {categoria} | Cant: {cantidad} | ${precio}{C_RESET}")

        otra = input("\n¿Agregar otro? (s/n): ").strip().lower()
        while otra not in ("s", "n"):
            otra = input("Ingrese s/n: ").strip().lower()
        if otra == "n":
            break

    input("\nPRESIONE ENTER PARA VOLVER...")

def accion_mostrar_productos():
    limpiar_pantalla()
    print(f"{C_TITLE}MOSTRAR PRODUCTOS{C_RESET}\n")
    rows = listar_productos_db()
    if not rows:
        print("No hay productos cargados.")
    else:
        idx = 0
        while idx < len(rows):
            r = rows[idx]
            print(f"ID {r[0]} | Nombre: {r[1]} | Cat: {r[5] or '-'} | Cant: {r[3]} | Precio: ${int(r[4])} | Desc: {r[2] or '-'}")
            idx += 1
    input("\nPRESIONE ENTER PARA VOLVER...")

def accion_buscar_producto():
    limpiar_pantalla()
    print(f"{C_TITLE}BUSCAR PRODUCTO{C_RESET}\n")
    print("1) Buscar por ID")
    print("2) Buscar por nombre o categoría")
    opcion = input("Seleccione (1-2, otra para volver): ").strip()
    if opcion == "1":
        pid = pedir_entero("Ingrese ID del producto: ", minimo=1)
        row = buscar_producto_por_id_db(pid)
        if row:
            print(f"\nID {row[0]} | Nombre: {row[1]} | Cat: {row[5] or '-'} | Cant: {row[3]} | Precio: ${int(row[4])} | Desc: {row[2] or '-'}")
        else:
            print(f"{C_WARN}No existe producto con ID {pid}.{C_RESET}")
    elif opcion == "2":
        termino = pedir_texto("Ingrese nombre o categoría (o parte): ")
        rows = buscar_productos_por_texto_db(termino)
        if rows:
            i = 0
            print("\nResultados:")
            while i < len(rows):
                r = rows[i]
                print(f"ID {r[0]} | Nombre: {r[1]} | Cat: {r[5] or '-'} | Cant: {r[3]} | Precio: ${int(r[4])} | Desc: {r[2] or '-'}")
                i += 1
        else:
            print("No se encontraron resultados.")
    else:
        return

    input("\nPRESIONE ENTER PARA VOLVER...")

def accion_actualizar_producto():
    limpiar_pantalla()
    print(f"{C_TITLE}ACTUALIZAR PRODUCTO{C_RESET}\n")
    pid = pedir_entero("Ingrese ID del producto a actualizar: ", minimo=1)
    current = buscar_producto_por_id_db(pid)
    if not current:
        print(f"{C_WARN}No existe producto con ID {pid}.{C_RESET}")
        input("\nPRESIONE ENTER PARA VOLVER...")
        return

    print(f"\nActual: ID {current[0]} | Nombre: {current[1]} | Cat: {current[5] or '-'} | Cant: {current[3]} | Precio: ${int(current[4])} | Desc: {current[2] or '-'}\n")

    nombre = input("Nombre (ENTER para mantener): ").strip()
    if nombre == "":
        nombre = current[1]
    descripcion = input("Descripción (ENTER para mantener): ").strip()
    if descripcion == "":
        descripcion = current[2] or ""

    while True:
        cant_in = input("Cantidad (ENTER para mantener): ").strip()
        if cant_in == "":
            cantidad = current[3]
            break
        if cant_in.lstrip("-").isdigit():
            cantidad = int(cant_in)
            if cantidad < 0:
                print("ERROR: la cantidad no puede ser negativa.")
                continue
            break
        else:
            print("ERROR: ingrese un número entero válido.")

    while True:
        prec_in = input("Precio (sin centavos) (ENTER para mantener): ").strip()
        if prec_in == "":
            precio = int(current[4])
            break
        if prec_in.lstrip("-").isdigit():
            precio = int(prec_in)
            if precio < 0:
                print("ERROR: el precio no puede ser negativo.")
                continue
            break
        else:
            print("ERROR: ingrese un número entero válido.")
    categoria = input("Categoría (ENTER para mantener): ").strip()
    if categoria == "":
        categoria = current[5] or ""

    ok = actualizar_producto_db(pid, nombre, descripcion, cantidad, precio, categoria)
    if ok:
        print(f"{C_OK}Producto ID {pid} actualizado.{C_RESET}")
    else:
        print(f"{C_ERR}Error al actualizar producto ID {pid}.{C_RESET}")

    input("\nPRESIONE ENTER PARA VOLVER...")

def accion_eliminar_producto():
    limpiar_pantalla()
    print(f"{C_TITLE}ELIMINAR PRODUCTO{C_RESET}\n")
    pid = pedir_entero("Ingrese ID del producto a eliminar: ", minimo=1)
    row = buscar_producto_por_id_db(pid)
    if not row:
        print(f"{C_WARN}No existe producto con ID {pid}.{C_RESET}")
        input("\nPRESIONE ENTER PARA VOLVER...")
        return

    print(f"\nID {row[0]} | Nombre: {row[1]} | Cat: {row[5] or '-'} | Cant: {row[3]} | Precio: ${int(row[4])} | Desc: {row[2] or '-'}")
    confirmar = input("\n¿Eliminar este producto? (s/n): ").strip().lower()
    while confirmar not in ("s", "n"):
        confirmar = input("Ingrese s/n: ").strip().lower()
    if confirmar == "s":
        ok = eliminar_producto_db(pid)
        if ok:
            print(f"{C_OK}Producto eliminado.{C_RESET}")
        else:
            print(f"{C_ERR}No se pudo eliminar el producto.{C_RESET}")
    else:
        print("Operación cancelada.")

    input("\nPRESIONE ENTER PARA VOLVER...")

def accion_reporte_bajo_stock():
    limpiar_pantalla()
    print(f"{C_TITLE}REPORTE: PRODUCTOS CON STOCK BAJO{C_RESET}\n")
    limite = pedir_entero("Mostrar productos con cantidad menor o igual a: ", minimo=0)
    rows = reporte_bajo_stock_db(limite)
    if not rows:
        print("No hay productos con cantidad igual o inferior a ese límite.")
    else:
        i = 0
        while i < len(rows):
            r = rows[i]
            print(f"ID {r[0]} | Nombre: {r[1]} | Cat: {r[5] or '-'} | Cant: {r[3]} | Precio: ${int(r[4])}")
            i += 1
    input("\nPRESIONE ENTER PARA VOLVER...")

# MENU PRINCIPAL

def mostrar_menu():
    limpiar_pantalla()
    print(f"{C_TITLE}Sistema de Gestión de Inventario{C_RESET}\n")
    print("1) Agregar producto")
    print("2) Mostrar productos")
    print("3) Buscar producto")
    print("4) Actualizar producto (por ID)")
    print("5) Eliminar producto (por ID)")
    print("6) Reporte: stock bajo")
    print("7) Salir\n")

def main():
    inicializar_db()

    opcion = ""
    while opcion != "7":
        mostrar_menu()
        opcion = input("Seleccione opción (1-7): ").strip()
        while opcion not in ("1","2","3","4","5","6","7"):
            opcion = input("Opción inválida. Ingrese 1-7: ").strip()

        match opcion:
            case "1":
                accion_agregar_producto()
            case "2":
                accion_mostrar_productos()
            case "3":
                accion_buscar_producto()
            case "4":
                accion_actualizar_producto()
            case "5":
                accion_eliminar_producto()
            case "6":
                accion_reporte_bajo_stock()
            case "7":
                limpiar_pantalla()
                print("FIN DEL PROGRAMA")
            case _:
                pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por usuario.")
        sys.exit(0)


