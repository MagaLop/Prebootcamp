numero1 = 70
numero2 = 3.14
booleano = False
cadena = 'Hola Mundo'
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate']
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False}
frutas = ('guayaba', 'fresa', 'papaya')
print(type(frutas))
print(ingredientes_pastel[2])
ingredientes_pastel.append('Mantequilla')
print(persona['nombre'])
persona['nombre'] = 'Kevin'
persona['color_ojos'] = 'cafe'
print(frutas[2])

if numero1 > 45:
    print("Numero mayor")
else:
    print("Numero menor")

if len(cadena) < 5:
    print("Cadena corta")
elif len(cadena) > 15:
    print("Cadena larga")
else:
    print("Cadena perfecta")

for x in range(8):
    print(x)
for x in range(2,8):
    print(x)
for x in range(2,8,2):
    print(x)
x = 0
while(x < 8):
    print(x)
    x += 1

ingredientes_pastel.pop()
ingredientes_pastel.pop(1)

print(persona)
persona.pop('color_ojos')
print(persona)

for ingrediente in ingredientes_pastel:
    if ingrediente == 'Harina':
        continue
    print('Después de la primera sentencia')
    if ingrediente == 'Chocolate':
        break

def imprime_hola_10_veces():
    for numero in range(10):
        print('Hola')

imprime_hola_10_veces()

def imprime_hola_n_veces(n):
    for numero in range(n):
        print('Hola')

imprime_hola_n_veces(5)

def imprime_hola_n_o_diez_veces(n = 10):
    for numero in range(n):
        print('Hola')

imprime_hola_n_o_diez_veces()
imprime_hola_n_o_diez_veces(5)


"""
Sección BONUS
"""

# print(numero3)
# numero3 = 86
# frutas[0] = 'naranja'
# print(persona['hobbies'])
# print(ingredientes_pastel[11])
#   print(booleano)
# frutas.append('manzana')
# frutas.pop(1)


#

lista_vacia = []
gatos = ["Garfield", "Silvestre", "Hello Kitty"]
print(gatos[2]) #Imprime: Silvestre
gatos[1] = "Tom"
gatos.append("Felix")
print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty', 'Felix']
gatos.pop()
print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty']
gatos.pop(1)
print(gatos) #Imprime: ['Garfield', 'Hello Kitty']


#

# 1. Imprime "Hola, mundo"
print("Hola, mundo") # Imprime "Hola, mundo" en la consola

# 2. Imprime "Hola, Valeria" con el nombre en una variable
nombre = "Valeria"
print( tu código aquí ) # con una coma
print( tu código aquí ) # con un +

# 3. Imprimir "Hola 156!" con el número en una variable
numero = 156
print( tu código aquí ) # con una coma
print( tu código aquí ) # con un + -- este debería arrojar un error!, corrígelo con conversión

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables
comida1 = "tacos"
comida2 = "arepas"
print( tu código aquí ) # con .format()
print( tu código aquí ) # con una cadena f

#
'''Crea un nuevo archivo y nómbralo hola_mundo.py
Escribe el código para que se imprima la cadena “Hola, mundo” (1)
Ejecuta el archivo
Reemplaza el texto que aparece en la variable nombre con tu nombre y usa la variable para imprimir la cadena “Hola, {{tu nombre}}” utilizando la concatenación con coma (2a)
Ejecuta el archivo
Reemplaza el texto que aparece en la variable nombre con tu nombre y usa la variable para imprimir la cadena “Hola, {{tu nombre}}” utilizando la concatenación con + (2b)
Ejecuta el archivo
Almacena tu número de la suerte en la variable numero y usa la variable para imprimir la cadena “Hola {{número}} !” utilizando la concatenación con coma (3a)
Almacena tu número de la suerte en la variable numero y usa la variable para imprimir la cadena “Hola {{número}}!” utilizando la concatenación con + (3b)
Ejecuta el archivo
BONUS NINJA: resuelve el error de arriba utilizando conversión
Guarda dos de tus comidas favoritas en las variables comida1 y comida2 y úsalas para imprimir la cadena “¡Me encanta comer {{comida1}} y {{comida2}}!” con el método format (4a)
Ejecuta el archivo
Guarda dos de tus comidas favoritas en las variables comida1 y comida2 y úsalas para imprimir la cadena “¡Me encanta comer {{comida1}} y {{comida2}}!” con cadena “f” (4b)
Ejecuta el archivo
BONUS NINJA: Busca otros métodos de cadena y utilízalos en el archivo. ¡Existen muchísimas opciones para esto!
'''

#

# Lista de temperaturas diarias
temperaturas = [22.5, 21.0, 23.3, 25.2, 24.5]
media_temperatura = sum(temperaturas) / len(temperaturas)
print("Temperatura media:", media_temperatura)

#

# Coordenadas geográficas de una ubicación
coordenadas = (19.4326, -99.1332)  # Latitud y longitud de Ciudad de México

def calcular_distancia(coord1, coord2):
    # Implementación ficticia para calcular la distancia
    distancia = 10  # Solo un valor de ejemplo
    return distancia

distancia = calcular_distancia(coordenadas, (34.0522, -118.2437))
print("Distancia:", distancia)

#

# Diccionario con información sobre un conjunto de datos
dataset_info = {
    "nombre": "Datos de ventas",
    "columnas": ["fecha", "producto", "cantidad", "precio"],
    "filas": 1000,
    "fuente": "Sistema de ventas interno"
}

print("Nombre del conjunto de datos:", dataset_info["nombre"])
print("Número de filas:", dataset_info["filas"])

#


