# 1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

agenda = {}

for i in range(5):
    nombre = input(f"Ingrese nombre del contacto #{i+1}: ").strip()
    numero = input(f"Ingrese número de {nombre}: ").strip()
    agenda[nombre] = numero

consulta = input("Ingrese un nombre para consultar su número: ").strip()
if consulta in agenda:
    print(f"Número de {consulta}: {agenda[consulta]}")
else:
    print("No hay un contacto con ese nombre.")

# 5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra

frase = input("Ingrese una frase: ").lower()

for signo in ".,;:!¿?¡()\"'":
    frase = frase.replace(signo, "")

palabras = frase.split()

unicas = set(palabras)
print("Palabras únicas:", unicas)

conteo = {p: palabras.count(p) for p in unicas}
print("Frecuencia de palabras:", conteo)



# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre = input(f"Nombre del alumno #{i+1}: ").strip()
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    alumnos[nombre] = (n1, n2, n3)

for nombre, notas in alumnos.items():
    prom = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {prom:.2f}")


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

aprobados_p1 = {a0, a1, a2, a3, a4}
aprobados_p2 = {a5, a6, a7, a8, a9}

ambos = aprobados_p1 & aprobados_p2
solo_uno = (aprobados_p1 ^ aprobados_p2)
al_menos_uno = aprobados_p1 | aprobados_p2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

stock = {}

while True:
    producto = input("Ingrese producto (o 'salir'): ").strip().lower()
    if producto == "salir":
        break

    if producto not in stock:
        stock[producto] = 0
        print(f"Producto '{producto}' agregado con stock inicial 0.")

    print(f"Stock actual de {producto}: {stock[producto]}")

    agregar = input("¿Desea agregar unidades? (s/n): ").strip().lower()
    if agregar == "s":
        cantidad = input("Ingrese cantidad a agregar: ").strip()
        if cantidad.isdigit():
            stock[producto] += int(cantidad)
            print(f"Nuevo stock de {producto}: {stock[producto]}")
        else:
            print("Debe ingresar un número válido.")

print("\nStock final:", stock)


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

agenda = {}

while True:
    accion = input("¿Desea (a)gregar, (c)onsultar o (s)alir?: ").strip().lower()
    if accion == 's':
        break
    elif accion == 'a':
        dia = input("Día (ej: 'Lunes'): ").strip()
        hora = input("Hora (ej: '10:00'): ").strip()
        evento = input("Evento: ").strip()
        agenda[(dia, hora)] = evento
        print("Evento guardado.")
    elif accion == 'c':
        dia = input("Día a consultar: ").strip()
        hora = input("Hora a consultar: ").strip()
        evento = agenda.get((dia, hora))
        if evento:
            print(f"En {dia} a las {hora}: {evento}")
        else:
            print("No hay actividad registrada en ese día y hora.")
    else:
        print("Opción inválida.")

print("Agenda completa:", agenda)


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
}

capitales_pais = {}
for pais, capital in paises_capitales.items():
    capitales_pais[capital] = pais

print(capitales_pais)



