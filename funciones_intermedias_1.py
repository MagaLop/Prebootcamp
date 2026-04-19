'''
1. Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
En ciudades, cambia “Cancún” por “Monterrey”
En las coordenadas, cambia el valor de “latitud” por 9.9355431
'''
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambia el valor de 3 en matriz por 6
matriz[1][0] = 6                                                        # Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]

# Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes[0]["nombre"] = "Enrique Martin Morales"

# En ciudades, cambia “Cancún” por “Monterrey”
ciudades["México"][2] = "Monterrey"

# En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas[0]["latitud"] = 9.9355431                                   # Coordenadas es una lista de diccionarios, por lo que accedemos al primer diccionario con [0] y luego a la clave "latitud" para cambiar su valor.

print(matriz)
print(cantantes)
print(ciudades)
print(coordenadas)


'''
2. Iterar a través de una lista de diccionarios

Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente. Por ejemplo:

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)
#Imprime "nombre": "Ricky Martin", "pais": "Puerto Rico" (está bien si lo imprime en líneas separadas)

#BONUS: Que aparezcan en este formato:
nombre - Ricky Martin, pais - Puerto Rico
nombre - Chayanne, pais - Puerto Rico
nombre - José José, pais - México
nombre - Juan Luis Guerra, pais - República Dominicana
'''

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},  
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

'''
def iterarDiccionario(lista):                                           # creando la función iterarDiccionario que recibe una lista de diccionarios como argumento
    for diccionario in lista:
        for clave, valor in diccionario.items():                        # recorriendo cada diccionario en la lista y luego cada clave-valor en el diccionario
            print(f"{clave}: {valor}")                                  # imprimiendo cada clave y su valor correspondiente en el formato "clave: valor"    

'''
            
def iterarDiccionario(lista):                                           # creando la función iterarDiccionario que recibe una lista de diccionarios como argumento
    for diccionario in lista:
        texto = ""                                                      # creando una variable texto para almacenar la cadena formateada
        for clave, valor in diccionario.items():                        # recorriendo cada diccionario en la lista y luego cada clave-valor en el diccionario
            texto += f"{clave} - {valor}, "                             # concatenando cada clave y su valor correspondiente en el formato "clave - valor, " a la variable texto
        print(texto.rstrip(", "))                                       # imprimiendo la variable texto y eliminando la última coma y espacio con rstrip(", ") para que el formato sea correcto, no olvidar que rstrip elimina combinacion de caracteres al final de la cadena

iterarDiccionario(cantantes)


'''
3. Obtener valores de una lista de diccionarios

Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios. La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista. Por ejemplo, iterarDiccionario2(“nombre”, cantantes) debe de imprimir:

Ricky Martin
Chayanne
José José
Juan Luis Guerra
Otro ejemplo: iterarDiccionario2(“pais”, cantantes) debe de imprimir:

Puerto Rico
Puerto Rico
México
República Dominicana
'''

def iterarDiccionario2(llave, lista):                                    # creando la función iterarDiccionario2 que recibe una cadena con el nombre de una llave y una lista de diccionarios como argumentos
    for diccionario in lista:                                            # recorriendo cada diccionario en la lista
        if llave in diccionario:                                         # verificando si la llave existe en el diccionario
            print(diccionario[llave])                                    # imprimiendo el valor almacenado para esa clave del diccionario
iterarDiccionario2("nombre", cantantes)                                  # llamando a la función iterarDiccionario2 con la llave "nombre" y la lista de cantantes para imprimir los nombres de los cantantes
iterarDiccionario2("pais", cantantes)                                    # llamando a la función iterarDiccionario2 con la llave "pais" y la lista de cantantes para imprimir los países de origen de los cantantes


'''
4. Iterar a través de un diccionario con valores de lista

Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas. La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave. Por ejemplo:

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

#imprime:
4 CIUDADES
San José
Limón
Cartago
Puntarenas

5 COMIDAS
gallo pinto
casado
tamales
chifrijo
olla de carne
'''

costa_rica = {
    "pais": "Costa Rica",
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
chile = {
    "pais": "Chile",
    "ciudades": ["Puerto Montt", "Santiago", "Puerto Varas", "Concepción", "Viña del Mar", "Valparaíso", "Chiloé"],
    "comidas": ["empanadas de pino", "humitas", "cazuela", "ensalada chilena", "pastel de choclo"]
}

def imprimirInformacion(diccionario):                                    # creando la función imprimirInformacion que recibe un diccionario como argumento
    print(f"{diccionario['pais'].upper()}")                              # imprimiendo el valor de la clave "pais" en mayúsculas para mostrar el país al que corresponde la información
    print()                                                              # imprimiendo una línea en blanco para separar la información del país
    for clave, valores in diccionario.items():                           # recorriendo cada clave y su lista de valores en el diccionario
        if clave == "pais":                                              # verificando si la clave es "pais" para evitar imprimirla nuevamente, ya que ya se imprimió al inicio de la función
            continue                                                     # si la clave es "pais", se omite el resto del código en el ciclo para esa iteración y se pasa a la siguiente clave
        
        print(f"{len(valores)} {clave.upper()}")                         # imprimiendo el tamaño de la lista de valores y la clave en mayúsculas
        for valor in valores:                                            # recorriendo cada valor en la lista de valores para la clave actual
            print(f"- {valor}")                                          # imprimiendo cada valor de la lista con un guion y espacio para formato
        print()                                                          # imprimiendo una línea en blanco para separar la información de cada clave

imprimirInformacion(costa_rica)                                          # llamando a la función imprimirInformacion con el diccionario costa_rica para imprimir la información de ciudades y comidas de Costa Rica

imprimirInformacion(chile)                                               # llamando a la función imprimirInformacion con el diccionario chile para imprimir la información de ciudades y comidas de Chile
