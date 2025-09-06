#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(100):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int(input("Ingrese un valor: "))
i = 0

while(num > 0):
    result = num // 10
    num = result
    i += 1

print(f"El valor ingresado tiene {i} dígitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

n1 = int(input("Igrese primer valor: "))
n2 = int(input("Ingrese segundo valor: "))

for i in range(n1+1,n2):
    print(i)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

n = int(input("Ingrese el primer valor: "))
suma = n
while(n != 0):
    aux = int(input("Ingrese valor: "))
    n = aux
    suma = suma + n
print(f"La suma de todos los valores es: {suma}")


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero = random.randint(0, 9)
print(numero)
intentos = 1
valor = int(input("Adivina el número: "))
if(numero == valor):
    print(f"CORRECTO, adivinó en {intentos} intentos")
else:
    print("Número incorrecto, siga itentando: ")
    while(valor != numero):
        intentos += 1
        aux = int(input("Adivina el número: "))
        valor = aux
        if(numero == valor):
            print(f"CORRECTO, adivinó en {intentos} intentos")
        else:
                print("Número incorreto, siga itentando: ")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

n = int(input("Ingrese un valor: "))
suma = n
for i in range(0, n):
    suma = suma + i
print(f"La suma de todos los valores de 0 a {n} es: {suma}")


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
positivos = 0
negativos = 0
n = 100

for i in range(n):
    num = int(input("Ingrese valor: "))
    if(num % 2 == 0):
        pares += 1
    else:
        impares += 1
    if(num >= 0):
        positivos += 1
    else: 
        negativos += 1
        
print("------------------")
print("INFORME")
print("------------------")
print(f"Cantidad de pares {pares} ")
print(f"Cantidad de impares {impares} ")
print(f"Cantidad de positivos {positivos} ")
print(f"Cantidad de negativos {negativos} ")


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

media = 0
suma = 0
n = int(input("Cuántos valores quiere promediar?: "))
for i in range(n):
    num = int(input("Ingrese valor: "))
    suma = suma + num
    
media = suma / n
        
print("------------------")
print("INFORME")
print("------------------")
print(f"La media de todos los valores ingresados es {media} ")


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un valor: "))
aux = num
invertido = 0

while num > 0:
    invertido = invertido * 10 + (num % 10)
    num = num // 10

print(f"El número {aux} invertido es {invertido}")