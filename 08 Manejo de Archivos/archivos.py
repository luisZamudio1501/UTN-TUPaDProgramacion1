# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

NOMBRE_ARCHIVO = "productos.txt"

lineas = [
    "Lapicera,120.5,30\n",
    "Cuaderno,850.0,12\n",
    "Regla,300.0,20\n",
]

with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
    f.writelines(lineas)

print("Archivo creado con 3 productos")    


# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30

NOMBRE_ARCHIVO = "productos.txt"

with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
    for linea in f:
        partes = linea.strip().split(",")
        if len(partes) != 3:
            continue
        nombre, precio, cantidad = partes
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")



# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

NOMBRE_ARCHIVO = "productos.txt"

def pedir_entero_no_negativo(msg: str) -> int:
    while True:
        dato = input(msg).strip()
        if dato.isdigit():
            return int(dato)
        print("Ingrese un entero no negativo")

def pedir_flotante_no_negativo(msg: str) -> float:
    while True:
        dato = input(msg).strip().replace(",", ".")
        try:
            val = float(dato)
            if val >= 0:
                return val
        except ValueError:
            pass
        print("Ingrese un número real no negativo")

nombre = input("Nombre del producto: ").strip()
precio = pedir_flotante_no_negativo("Precio: $")
cantidad = pedir_entero_no_negativo("Cantidad: ")

with open(NOMBRE_ARCHIVO, "a", encoding="utf-8") as f:
    f.write(f"{nombre},{precio},{cantidad}\n")

print("Producto agregado sin borrar el archivo")



# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.

from typing import List, Dict

NOMBRE_ARCHIVO = "productos.txt"

productos: List[Dict[str, object]] = []

with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
    for linea in f:
        partes = linea.strip().split(",")
        if len(partes) != 3:
            continue
        nombre, precio_str, cant_str = partes
        try:
            precio = float(precio_str)
            cantidad = int(cant_str)
        except ValueError:
            continue
        productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

print("Productos cargados en memoria:")
for p in productos:
    print(p)



# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.

from typing import List, Dict

NOMBRE_ARCHIVO = "productos.txt"

def cargar_productos() -> List[Dict[str, object]]:
    productos = []
    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) != 3:
                continue
            nombre, precio_str, cant_str = partes
            try:
                precio = float(precio_str)
                cantidad = int(cant_str)
            except ValueError:
                continue
            productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    return productos

def normalizar_nombre(n: str) -> str:
    return " ".join(n.strip().split())

productos = cargar_productos()
objetivo = normalizar_nombre(input("Busque un producto por nombre: ")).lower()

encontrado = None
for p in productos:
    if p["nombre"].lower() == objetivo:
        encontrado = p
        break

if encontrado:
    print(f"Nombre: {encontrado['nombre']} | Precio: ${encontrado['precio']} | Cantidad: {encontrado['cantidad']}")
else:
    print("No existe un producto con ese nombre")



# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.

from typing import List, Dict

NOMBRE_ARCHIVO = "productos.txt"

def cargar_productos() -> List[Dict[str, object]]:
    productos = []
    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) != 3:
                continue
            nombre, precio_str, cant_str = partes
            try:
                precio = float(precio_str)
                cantidad = int(cant_str)
            except ValueError:
                continue
            productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    return productos

def guardar_productos(productos: List[Dict[str, object]]):
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("Archivo sobrescrito con los productos actualizados")

def pedir_flotante_no_negativo(msg: str) -> float:
    while True:
        dato = input(msg).strip().replace(",", ".")
        try:
            val = float(dato)
            if val >= 0:
                return val
        except ValueError:
            pass
        print("Ingrese un número real no negativo")

def pedir_entero_no_negativo(msg: str) -> int:
    while True:
        dato = input(msg).strip()
        if dato.isdigit():
            return int(dato)
        print("Ingrese un entero no negativo")

def normalizar_nombre(n: str) -> str:
    return " ".join(n.strip().split())

productos = cargar_productos()

while True:
    nombre_obj = normalizar_nombre(input("Producto a actualizar (Enter para terminar): "))
    if nombre_obj == "":
        break

    idx = None
    for i, p in enumerate(productos):
        if p["nombre"].lower() == nombre_obj.lower():
            idx = i
            break

    if idx is None:
        print("No se encontró ese producto")
        continue

    actual = productos[idx]
    op = input("¿Qué quiere actualizar? (p=precio, c=cantidad, ambos=pc): ").strip().lower()

    if op in ("p", "pc"):
        actual["precio"] = pedir_flotante_no_negativo(f"Nuevo precio (actual {actual['precio']}): $")
    if op in ("c", "pc"):
        actual["cantidad"] = pedir_entero_no_negativo(f"Nueva cantidad (actual {actual['cantidad']}): ")

    print("Actualizado\n")

guardar_productos(productos)

