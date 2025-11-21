
# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario


def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * factorial_recursivo(n - 1)
    else:
        raise ValueError("El factorial solo está definido para números enteros no negativos.")

def mostrar_factoriales():
    print("\n--- EJERCICIO 1: Factoriales Múltiples ---")
    while True:
        entrada = input("Ingrese un n entero positivo para calcular factoriales hasta n: ").strip()
        if entrada.isdigit():
            limite = int(entrada)
            if limite < 1:
                print("Por favor, ingrese un número entero positivo (mayor o igual a 1).")
                continue
            break
        else:
            print("Entrada no válida. Por favor, ingrese un número entero.")

    print(f"\nFactoriales de 1 hasta {limite}:")
    for i in range(1, limite + 1):
        resultado = factorial_recursivo(i)
        print(f"{i}! es: {resultado}")


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def fibonacci_recursivo(posicion):
    """Calcula el valor de Fibonacci en la posición indicada de forma recursiva (F(1)=1, F(2)=1...)."""
    if posicion <= 0:
        return 0 # Si se pide F(0)
    elif posicion == 1 or posicion == 2:
        return 1
    else:
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

def mostrar_serie_fibonacci():
    print("\n--- EJERCICIO 2: Serie de Fibonacci ---")
    while True:
        entrada = input("Ingrese la posición límite para la serie de Fibonacci (>= 1): ").strip()
        if entrada.isdigit():
            limite = int(entrada)
            if limite < 1:
                print("Por favor, ingrese una posición entera positiva.")
                continue
            break
        else:
            print("Entrada no válida. Por favor, ingrese un número entero.")

    print(f"\nSerie de Fibonacci hasta la posición {limite}:")
    serie = []
    for i in range(1, limite + 1):
        valor = fibonacci_recursivo(i)
        serie.append(str(valor))

    print(", ".join(serie))


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1). Prueba esta función en un algoritmo general.

def potencia_recursiva(base, exponente):
 
    if exponente == 0:
        return 1
    
    elif exponente == 1:
        return base
        
    elif exponente > 1:
        return base * potencia_recursiva(base, exponente - 1)
        
    elif exponente < 0:
        return 1 / potencia_recursiva(base, abs(exponente))

def probar_potencia():
    print("\n--- EJERCICIO 3: Potencia de un Número ---")
    
    print(f"2 elevado a 3: {potencia_recursiva(2, 3)}")     
    print(f"5 elevado a 0: {potencia_recursiva(5, 0)}")     
    print(f"10 elevado a 4: {potencia_recursiva(10, 4)}")   
    print(f"2 elevado a -2: {potencia_recursiva(2, -2)}")    


# Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
# procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
# Convertir el número 10 a binario:
# 10 ÷ 2 = 5 resto: 0
# 5 ÷ 2 = 2 resto: 1
# 2 ÷ 2 = 1 resto: 0
# 1 ÷ 2 = 0 resto: 1
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".

def decimal_a_binario_recursivo(n):
    
    if n == 0:
        return "0"
        
    def _conversion(num):
        if num == 0:
            return ""
        
        resto = num % 2
        
        return _conversion(num // 2) + str(resto)

    return _conversion(n)

def probar_conversion_binaria():
    print("\n--- EJERCICIO 4: Decimal a Binario ---")
    
    print(f"10 en binario es: {decimal_a_binario_recursivo(10)}") 
    print(f"13 en binario es: {decimal_a_binario_recursivo(13)}") 
    print(f"0 en binario es: {decimal_a_binario_recursivo(0)}")   
    print(f"1 en binario es: {decimal_a_binario_recursivo(1)}")   


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos: La solución debe ser recursiva. No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    
    if len(palabra) <= 1:
        return True
    
    primer_caracter = palabra[0]
    ultimo_caracter = palabra[-1]
    
    if primer_caracter == ultimo_caracter:
        return es_palindromo(palabra[1:-1])
    else:
        return False

def probar_palindromo():
    print("\n--- EJERCICIO 5: Palíndromo ---")
    
    print(f"¿'reconocer' es palíndromo? {es_palindromo('reconocer')}") 
    print(f"¿'oso' es palíndromo? {es_palindromo('oso')}")             
    print(f"¿'programacion' es palíndromo? {es_palindromo('programacion')}") 
    print(f"¿'radar' es palíndromo? {es_palindromo('radar')}")         


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)


def suma_digitos(n):

    if n < 10:
        return n
    
    ultimo_digito = n % 10
    resto_del_numero = n // 10
    
    return ultimo_digito + suma_digitos(resto_del_numero)

def probar_suma_digitos():
    print("\n--- EJERCICIO 6: Suma de Dígitos ---")
    
    print(f"Suma de dígitos de 1234: {suma_digitos(1234)}")  
    print(f"Suma de dígitos de 9: {suma_digitos(9)}")       
    print(f"Suma de dígitos de 305: {suma_digitos(305)}")    


# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):

    if n == 1:
        return 1
    
    elif n > 1:
        return n + contar_bloques(n - 1)
    else:
        # Para n <= 0
        return 0

def probar_conteo_bloques():
 
    print("\n--- EJERCICIO 7: Conteo de Bloques de Pirámide ---")
    
    print(f"Bloques para n=1: {contar_bloques(1)}") 
    print(f"Bloques para n=2: {contar_bloques(2)}")  
    print(f"Bloques para n=4: {contar_bloques(4)}") 


# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4 
# contar_digito(123456, 7) → 0 

def contar_digito(numero, digito):
   
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10
    
    es_igual = 1 if ultimo_digito == digito else 0
    
    resto_del_numero = numero // 10
    return es_igual + contar_digito(resto_del_numero, digito)

def probar_conteo_digito():

    print("\n--- EJERCICIO 8: Conteo de Dígito Específico ---")
    
    print(f"Conteo de '2' en 12233421: {contar_digito(12233421, 2)}")  
    print(f"Conteo de '5' en 5555: {contar_digito(5555, 5)}")         
    print(f"Conteo de '7' en 123456: {contar_digito(123456, 7)}")     
    print(f"Conteo de '0' en 102030: {contar_digito(102030, 0)}")     
    print(f"Conteo de '0' en 0: {contar_digito(0, 0)}")              


# MAIN PARA EJECUTAR TODAS LAS PRUEBAS

def main():
    
    print("=============================================")
    print(" INICIO DE PRUEBAS DE FUNCIONES RECURSIVAS ")
    print("=============================================")
    
    mostrar_factoriales()
    mostrar_serie_fibonacci()
    probar_potencia()
    probar_conversion_binaria()
    probar_palindromo()
    probar_suma_digitos()
    probar_conteo_bloques()
    probar_conteo_digito()
    
    print("\n=============================================")
    print("              FIN DE PRUEBAS ")
    print("===============================================")


if __name__ == "__main__":
    main()
