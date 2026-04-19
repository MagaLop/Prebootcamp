'''
1.Multiplica por 2: crea una función que reciba un número y devuelva una lista que contenga los números enteros multiplicados por dos, desde el 0 hasta el número proporcionado como entrada.
Ejemplo: multiplica_por_2(5) debe regresar [0, 2, 4, 6, 7, 10]
2. Suma y resta: crea una función que reciba una lista con dos números. Imprime la suma de los dos números y regresa la resta de los dos números.
Ejemplo: suma_y_resta([5, 4]) debe de imprimir 9 y regresar 1
3. Sumatoria menos longitud: crea una función que reciba una lista de números y regresa la sumatoria de estos menos la longitud de la lista.
Ejemplo: sumatoria_menos_longitud([1, 2, 3, 4]) debe devolver 6 (sumatoria de números: 10 – longitud: 4)
Valores multiplicados por el segundo: escribe una función que reciba una lista y crea una nueva lista con todos los valores multiplicados por el segundo número. Imprime la longitud de la lista y regresa la nueva lista. Si la lista tiene menos de 2 elementos, haz que la función regrese una lista vacía.
Ejemplo: valores_multiplicados_segundo([1, 3, 5, 7]) debe imprimir 4 y devolver [3, 9, 15, 21]
Ejemplo: valores_multiplicados_segundo([1]) debe imprimir 1 y devolver [ ]
5. Valor multiplado y longitud: escribe una función que reciba dos números enteros: valor y longitud. La función debe crear y regresar una lista cuyo tamaño sea igual a la longitud recibida y los valores sean igual a la longitud multiplicada por el valor dado.
Ejemplo: valor_multiplicado_longitud(5, 2) regresa [10, 10]
Ejemplo: valor_multiplicado_longitud(7, 5) regresa [35, 35, 35, 35, 35]
'''
# 1. Multiplica por 2: crea una función que reciba un número y devuelva una lista que contenga los números enteros multiplicados por dos, desde el 0 hasta el número proporcionado como entrada.

def multiplica_por_2(numero):                               # La función recibe un número como argumento
    return [i * 2 for i in range(numero + 1)]               # Utiliza una comprensión de lista para generar una lista de números enteros multiplicados por dos, desde 0 hasta el número proporcionado (inclusive)

# 2. Suma y resta: crea una función que reciba una lista con dos números. Imprime la suma de los dos números y regresa la resta de los dos números.

def suma_y_resta(lista):                                    # La función recibe una lista con dos números como argumento
    suma = sum(lista)                                       # Calcula la suma de los dos números utilizando la función sum() y la almacena en la variable 'suma'
    print(suma)                                             # Imprime la suma de los dos números
    return lista[0] - lista[1]                              # Regresa la resta de los dos números accediendo a ellos por su índice en la lista (lista[0] - lista[1])

# 3. Sumatoria menos longitud: crea una función que reciba una lista de números y regresa la sumatoria de estos menos la longitud de la lista.

def sumatoria_menos_longitud(lista):                        # La función recibe una lista de números como argumento
    return sum(lista) - len(lista)                          # Calcula la sumatoria de los números utilizando la función sum() y luego resta la longitud de la lista utilizando la función len(), regresando el resultado final

# 4. Valores multiplicados por el segundo: escribe una función que reciba una lista y crea una nueva lista con todos los valores multiplicados por el segundo número. Imprime la longitud de la lista y regresa la nueva lista. Si la lista tiene menos de 2 elementos, haz que la función regrese una lista vacía.

def valores_multiplicados_segundo(lista):                    # La función recibe una lista como argumento
    if len(lista) < 2:                                       # Verifica si la longitud de la lista es menor a 2
        print(len(lista))                                    # Imprime la longitud de la lista (que será menor a 2)
        return []                                            # Regresa una lista vacía si la longitud de la lista es menor a 2
    segundo = lista[1]                                       # Almacena el segundo número de la lista en la variable 'segundo'
    nueva_lista = [i * segundo for i in lista]               # Utiliza una comprensión de lista para generar una nueva lista con todos los valores multiplicados por el segundo número
    print(len(nueva_lista))                                  # Imprime la longitud de la nueva lista
    return nueva_lista                                       # Regresa la nueva lista con los valores multiplicados por el segundo número

# 5. Valor multiplicado y longitud: escribe una función que reciba dos números enteros: valor y longitud. La función debe crear y regresar una lista cuyo tamaño sea igual a la longitud recibida y los valores sean igual a la longitud multiplicada por el valor dado.

def valor_multiplicado_longitud(valor, longitud):            # La función recibe dos números enteros, 'valor' y 'longitud', como argumentos
    return [valor * longitud] * longitud                     # Crea una lista utilizando la multiplicación de listas, donde el valor multiplicado por la longitud se repite 'longitud' veces, y regresa esta lista resultante
