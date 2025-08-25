#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
print(f"Hola  {nombre}")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
edad = input("Ingrese edad: ")
pais = input("Ingrese pais: ")
print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {pais}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
import math
radio = input("Ingrese radio: ")
perimetro = math.pi * radio * 2
print(f"El perimetro del circulo es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

cantSeg = float(input("Ingrese cantidad de segundos: "))
horas = cantSeg / 3600
print(f"{cantSeg} segundos corresponden a {horas} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

num = int(input("Ingrese un numero entero: "))
print(f"Tabla de multiplicar de {num}")
for i in range(1, 10):
    print(f"{num} x {i} = {num * i}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("CALCULADORA")
print("Ingrese dos valores distintos de cero:")
print("--------------------------------------")
num1 = int(input("Ingrese primer valor: "))
num2 = int(input("Ingrese segundo valor: "))
suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = float(num1 / num2)
print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {mult}")
print(f"{num1} / {num2} = {div}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:
#𝐼𝑀𝐶 =
#𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
#(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)elevado 2

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
imc = peso / (altura * altura)
print(f"Su indice de masa corporal es: {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

celsius = int(input("Ingrese temperatura en grados Celsius: "))
fahrentheit = 9/5 * celsius + 32
print(f"Su equivalente en grados Fahrenheit es: {fahrentheit}")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
print("Promedio de tres numeros")
num1 = float(input("Ingrese primer valor: "))
num2 = float(input("Ingrese segundo valor: "))
num3 = float(input("Ingrese tercer valor: "))
promedio = (num1 + num2 + num3)/3
print(f"El promedio de los tres valores es: {promedio}")