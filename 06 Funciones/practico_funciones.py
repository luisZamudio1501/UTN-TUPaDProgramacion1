# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
import math

def imprimir_hola_mundo():
    print("Hola Mundo")

imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

while True:
    nombre = input("Ingrese su nombre: ").strip()
    if nombre == "" or any(i.isdigit() for i in nombre): # Recorre cada posición de nombre y detecta si hay digitos
        print("Ingrese un nombre válido")
        continue
    break

saludar_usuario(nombre)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados

def informacion_personal(nombre, apellido, edad, residencia):
    return(f"Soy {nombre} {apellido}, tengo {edad} años y vivvo en {residencia}")


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como 
# parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
# que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)
    
def calcular_perimetro_circulo(radio):
    return math.pi * 2 * radio

while True:
    aux = input("Ingrese el radio: ").strip()
    if not aux.isdigit():
        print("Ingrese un valor valido")
        continue
    num = int(aux)
    if num <= 0:
        print("El radio debe ser mayor que 0")
        continue
    
    print(f"El área de un circulo de radio {num} es: {calcular_area_circulo(num):.2f}")
    print(f"El área de un circulo de radio {num} es: {calcular_perimetro_circulo(num):.2f}")
    
    break


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

while True: 
    aux = (input("Ingrese cantidad de segundos: "))
    if not aux.isdigit():
        print("Ingrese un dato válido")
        continue
    else:
        seg = int(aux)
        break

cant = segundos_a_horas(seg)
if seg < 3600:
    print("La cantidad de segundos es menor a 1 hora")
    print(f"Corresponden a {int(seg / 60)} minutos")
else:     
    print(f"{seg} segundos corresponden a horas: {int(cant) }")


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):

    for i in range(10):
        producto = ((i+1) * numero)
        print(f"{numero} x {i+1} = {producto}")


while True: 
    aux = (input("Ingrese un valor: "))
    if not aux.isdigit():
        print("Ingrese un dato válido")
        continue
    else:
        num = int(aux)
        break

print(f"TABLA DEL {num}")
print("----------")
tabla_multiplicar(num)


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    resultados = (suma, resta, multiplicacion, division)
    return resultados

while True: 
    aux1 = input("Ingrese el primer valor: ")
    aux2 = input("Ingrese el segundo valor: ")
    if not aux1.isdigit() or not aux2.isdigit():
        print("Ingrese datos válidos")
        continue
    else:
        num1 = int(aux1)
        num2 = int(aux2)
        break

r = operaciones_basicas(num1, num2)
print("RESULATADOS DE LAS OPERACIONES")
print("------------------------------")
print(f"Suma de {num1} + {num2} = {r[0]}")
print(f"Resta de {num1} + {num2} = {r[1]}")
print(f"Multiplicación de {num1} + {num2} = {r[2]}")
print(f"División de {num1} + {num2} = {r[3]}")


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función 
# para mostrar el resultado con dos decimales.

def calcular_imc(peso,altura):
    imc = peso / (altura * altura)
    return imc

def es_float(cadena):
    if cadena.startswith(('-', '+')):
        cadena = cadena[1:]
    return cadena not in ('', '.') and cadena.replace('.', '', 1).isdigit()


while True: 
        aux = input("Ingrese su peso: ")
        if not aux.isdigit():
            print("Error, ingrese un dato correcto")
            continue
        else:
            peso = int(aux)
            break

while True:
    cadena_ingresada = input("Ingresá tu altura en metros (con el siguiente formato = 1.75): ")
    cadena_corregida = cadena_ingresada.replace(',', '.')

    if '.' in cadena_corregida and es_float(cadena_corregida):
        altura = float(cadena_corregida)
        if 0.5 < altura < 2.5:
             break
        else:
             print("ERROR! La altura parece no ser válida ¿Estás seguro?")
    else:
        print("ERROR! Formato incorrecto")

print(f"\nSu peso es = {peso}")
print(f"Su altura es = {altura}")
imc = calcular_imc(peso, altura)
print(f"Su Indice de Masa Corporarl IMC es: {imc:.2f}")


# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_farenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit



while True: 
    num = input("Ingrese la temperatura en grados Celsius (sin puntos ni comas): ")
    
    # Se crea una copia de num para poder modificarla y verificar que admita rangos de temperaturas negativas y positivas
    aux = num
    
    if aux.startswith('-'):
        aux = aux[1:] # Si existe se quita el primer caracter ('-')

    if aux.isdigit():
        grados = float(num) 
        break 
    else:
        print("ERROR! Ingrese un número válido")

resultado = celsius_a_farenheit(grados)
print(f"La temperatura en grados Fahrenheit es: {resultado}")


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

notas = []
for i in range(3):
    while True: 
        aux = input(f"Ingrese nota {i+1}: ")
        if not aux.isdigit():
            print("Error, ingrese un dato correcto")
            continue
        else:
            nota_ingresada = int(aux)
            notas.append(nota_ingresada)
            break

nota_1 = notas[0]    
nota_2 = notas[1]
nota_3 = notas[2]

promedio_final = calcular_promedio(nota_1, nota_2, nota_3)

print(f"El promedio final es {promedio_final}")











