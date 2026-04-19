'''
1. Básico: imprime todos los números enteros del 0 al 100.
2. Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
3. ontando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
4. Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
5. Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
6. Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).
'''
# 1. Básico: imprime todos los números enteros del 0 al 100.

for numero in range(101):                        # El rango va de 0 a 100, el 101 no se incluye.
    print(numero)                                # Imprime todos los números enteros del 0 al 100.

# 2. Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500

for numero in range(2, 501, 2):                  # El rango va de 2 a 500, el 501 no se incluye, y el paso es de 2 para obtener solo los múltiplos de 2.
    print(numero)                                # Imprime los números múltiplos de 2 entre 2 y 500.

# 3. Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”

for numero in range(1, 101):                     # El rango va de 1 a 100, el 101 no se incluye.
    if numero % 10 == 0:                         # Primero verificamos si es divisible por 10, porque si es divisible por 10, también es divisible por 5, y queremos imprimir "baby" en ese caso.
        print("baby")
    elif numero % 5 == 0:                        # Si el número es divisible por 5 (y no por 10), imprimimos "ice ice".
        print("ice ice")
    else:
        print(numero)                            # Si el número no es divisible ni por 5 ni por 10, imprimimos el número.

# 4. Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).

suma = 0
for numero in range(0, 500001, 2):               # El rango va de 0 a 500,000, el 500,001 no se incluye, y el paso es de 2 para obtener solo los números pares.
    suma += numero                               # Esto es equivalente a suma = suma + numero, pero es una forma más concisa de escribirlo.
print(suma)                                      # Imprime la suma total de los números pares del 0 al 500,000.

# 5. Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.

for numero in range(2024, 0, -3):                # 2024, es el inicio, 0 es el final (no incluido), -3 es el paso.
    print(numero)                                # Imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.


# 6. Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).

numInicial = 3
numFinal = 10
multiplo = 2
for numero in range(numInicial, numFinal + 1):   # El rango va de numInicial a numFinal, el numFinal + 1 se incluye para que el numFinal también sea considerado en el rango.
    if numero % multiplo == 0:                   # Verificamos si el número es múltiplo de la variable multiplo.
        print(numero)                            # Si el número es múltiplo de multiplo, lo imprimimos.

