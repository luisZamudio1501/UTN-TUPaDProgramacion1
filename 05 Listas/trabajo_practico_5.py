#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.

notas = [7.3, 8.4, 9.0, 10.0, 9.5, 9.8, 6.8, 8.9, 8.5, 8.4]
suma = 0
nota_max = 0
nota_min = 0

for i in range(10):
    print(f"Nota {i+1} = {notas[i]}")
    suma = suma + notas[i]
    if(i == 0):
        nota_max = notas[i]
        nota_min = notas[i]
    else:
        if(notas[i] > nota_max):
            nota_max = notas[i]
        elif(notas[i] < nota_min):
            nota_min = notas[i]

promedio = suma / 10

print("***** INFORMES *****")
print(f"Promedio de notas: {promedio}")
print(f"Nota mayor: {nota_max}")
print(f"Nota menor: {nota_min}")


#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for i in range(5):
    productos.append(input(f"Ingrese producto {i+1}: "))

lista_ordenada = sorted(productos)

print(lista_ordenada)

eliminado = input("¿Qué elemento desea eliminar?")
productos.remove(eliminado)

print(f"El producto {eliminado} ha sido eliminado")
print(productos)

#4) Dada una lista con valores repetidos:
#  datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# •Crear una nueva lista sin elementos repetidos.
# •Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
print("Lista original")
print(datos)
nueva_lista = list(set(datos))
print("Lista actualizada sin elementos repetidos")
print(nueva_lista)


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

estudiantes = ["Abel", "Aldo", "Antonio", "Beatriz", "Baltazar", "Juan", "Jose", "Jorge"]
print(estudiantes)

opcion = input("Quiere elimnar o agregar un estudiante? 1 = eliminar, 2 = agregar: ")

while(not(opcion == "1" or opcion == "2")):
        opcion = input("opcion incorrecta, ingrese nuevamente: ")
        
if(opcion == "1"):
    eliminado = input("Ingrese el estudiantes a eliminar: ")
    while(not(eliminado in estudiantes)):
        eliminado = input("El estudiante no está en la lista, ingrese nuevamente: ")
    
    estudiantes.remove(eliminado)
    print("Lista actualizada")
    print(estudiantes)
    
elif(opcion == "2"):
    agregado = input("Ingrese el elemento a agregar: ")
    estudiantes.append(agregado)
    print("Lista actualizada")
    print(estudiantes)


#6) Dada una lista con 7 números, rotar todos los elementos una posición 
# hacia la derecha (el último pasa a ser el primero).

numeros = [1, 2, 3, 4, 5, 6, 7]
print(numeros)
numeros = [numeros[-1]] + numeros[:-1]
print(numeros)


#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas
# de una semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [10, 20], #domingo
    [9, 18], #lunes
    [11, 19], #martes
    [8, 22], #miercoles
    [10, 23], #jueves
    [11, 24], #viernes
    [10, 25], #sabado
    ]
    
suma_min = 0
suma_max = 0
 
for i in range(len(temperaturas)):
    suma_min += temperaturas[i][0]
    suma_max += temperaturas[i][1]

promedio_min = suma_min / 7
promedio_max = suma_max / 7

dias_semana = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]
amplitud_max = 0 
dia_amp_max = ""

for i in range(len(temperaturas)):
    aux = temperaturas[i][1] - temperaturas[i][0]
    if aux > amplitud_max:
        amplitud_max = aux
        dia_amp_max = dias_semana[i]

print(f"El promedio de temperaturas mínimas es {promedio_min:.2f}° C")
print(f"El promedio de temperaturas máximas es {promedio_max:.2f}° C")

print(f"La mayor amplitud térmica se resgistró el día {dia_amp_max} con {amplitud_max}° C")

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

alumnos = []
promedio_estudiantes = []
promedio_notas = []

suma_notas = 0

for i in range(5):
    nombre = input(f"Ingrese nombre de alumno {i+1}: ")
    datos_alumno = [nombre]
    suma_aux = 0
    for j in range(3):
        nota = float(input(f"Ingrese nota {j+1}: "))
        datos_alumno.append(nota)
        suma_aux += nota
        suma_notas += nota
    alumnos.append(datos_alumno)
    promedio = suma_aux / 3
    promedio_estudiantes.append([nombre, promedio])
    promedio_estudiantes.append(promedio)
    
promedio_notas = suma_notas / 15
print("Listado de alumnos")
for i in alumnos:
    print(i)

print("Listado de promedios")
for i in promedio_estudiantes:
    print(i)
    
print(f"Promedio de notas: {promedio_notas}")

# 9 Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada


tablero = [[" - " for _ in range(3)] for _ in range(3)]


jugador = "X"
jugadas = 0
ganador = None

while True:
    print("\n   --- Tablero ---")
    for fila_tablero in tablero:
        print(*fila_tablero, sep="")
    print("   ---------------")

    if ganador:
        print(f"¡Felicitaciones! El jugador '{ganador}' ha ganado")
        break

    if jugadas == 9 and not ganador:
        print("Empate")
        break

    print(f"\nTurno del jugador '{jugador}'")

    fila_aux = input("Ingrese la fila (0, 1, 2): ")
    columna_aux = input("Ingrese la columna (0, 1, 2): ")

    if not (fila_aux.isdigit() and columna_aux.isdigit()):
        print("Error,ingrese solo números.")
        continue

    fila = int(fila_aux)
    columna = int(columna_aux)

    if not (0 <= fila <= 2 and 0 <= columna <= 2):
        print("Posición fuera de rango, ingrese números entre 0 y 2.")
        continue

    if tablero[fila][columna] != " - ":
        print("Casilla ocupada, intente de nuevo.")
        continue

    tablero[fila][columna] = f" {jugador} "
    jugadas += 1

    # Revisar filas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != " - ":
            ganador = jugador

    # Revisar columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != " - ":
            ganador = jugador

    # Revisar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " - ":
        ganador = jugador
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " - ":
        ganador = jugador

    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

productos = ["producto_1", "producto_2", "producto_3", "producto_4"]
precios = [1250.50, 980.00, 850.75, 1500.00]

print("--- Carga de Ventas de la Semana ---")
ventas = [] 

for i in range(len(productos)):
    ventas_producto = [] 
    print(f"\n--- Cargando ventas para '{productos[i]}' ---")
    
    for j in range(7):
        while True:
            venta_entrada = input(f"  - Cantidad vendida el Día {j + 1}: ")
            if venta_entrada.isdigit():
                ventas_producto.append(int(venta_entrada))
                break
            else:
                print("  Error: Por favor, ingrese un número entero válido.")
    
    ventas.append(ventas_producto)

print("\n--- Matriz de Cantidades Vendidas (Producto x Día) ---")
for i in range(len(productos)):
    print(f"{productos[i]:<8}: {ventas[i]}")
print("-" * 50)

print("\n--- Ingreso Total por Producto (en Pesos) ---")
total_unidades_por_producto = []
total_ingresos_por_producto = []

for i in range(len(productos)):
    unidades_vendidas = sum(ventas[i])
    ingreso_producto = unidades_vendidas * precios[i]
    
    total_unidades_por_producto.append(unidades_vendidas)
    total_ingresos_por_producto.append(ingreso_producto)
    
    print(f"Producto '{productos[i]}': Ingreso total de ${ingreso_producto:.2f}")

ingreso_maximo = max(total_ingresos_por_producto)
producto_mas_rentable = total_ingresos_por_producto.index(ingreso_maximo)
print(f"\n-> El producto con mayor ingreso fue '{productos[producto_mas_rentable]}' con ${ingreso_maximo:.2f}")

unidades_maximas = max(total_unidades_por_producto)
producto_mas_vendido = total_unidades_por_producto.index(unidades_maximas)
print(f"-> El producto más vendido fue '{productos[producto_mas_vendido]}' con {unidades_maximas} unidades.")
print("-" * 50)

print("\n--- Día con Mayores Ingresos Totales ---")
ingresos_por_dia = []
for i in range(7):
    ingreso_del_dia = 0
    for j in range(len(productos)):
        cantidad = ventas[j][i]
        precio = precios[j]
        ingreso_del_dia += cantidad * precio
    ingresos_por_dia.append(ingreso_del_dia)

ingreso_maximo_dia = max(ingresos_por_dia)
dia_max_ingreso = ingresos_por_dia.index(ingreso_maximo_dia)

print(f"-> El día con mayores ingresos fue el Día {dia_max_ingreso + 1} con un total de ${ingreso_maximo_dia:.2f}")
print("-" * 50)
