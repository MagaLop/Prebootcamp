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

# (1) Hola mundo
print("Hola, Mundo")

# (2a) concatenación con coma
nombre = "MagaLop"
print("Hola,", nombre)

# (2b) concatenación con +
nombre = "MagaLop"
print("Hola, " + nombre)

# (3a) concatenación con coma
numero = 9
print("Hola", numero, "!")

# (3b) ERROR
# print("Hola " + numero + "!")

# BONUS NINJA: conversión
print("Hola " + str(numero) + "!")

# (4a) usando .format()
comida1 = "Ramen"
comida2 = "Dumplings"

print("¡Me encanta comer {} y {}!".format(comida1, comida2))


# (4b) usando f-string
print(f"¡Me encanta comer {comida1} y {comida2}!")

# BONUS NINJA: otros métodos de string

# Método upper() para convertir a mayúsculas
print(nombre.upper())

# Método lower() para convertir a minúsculas
print(nombre.lower())

# Método title() para convertir a formato título
print(nombre.title())

#metodo capitalize() para convertir la primera letra a mayúscula
print(nombre.capitalize())

# Método replace() para reemplazar parte de la cadena
print(nombre.replace("Maga", "Lopa"))

# Método split() para dividir la cadena en una lista
print(nombre.split("a"))

# Método len() para obtener la longitud de la cadena
print(len(nombre))

# Método strip() para eliminar espacios en blanco al inicio y al final
nombre_con_espacios = "  " + nombre + "  "
print(nombre_con_espacios.strip())

# Método find() para encontrar la posición de una subcadena
print(nombre.find("Lop"))

# Método count() para contar cuántas veces aparece una subcadena
print(nombre.count("a"))

# Método in para verificar si una subcadena está presente
print("con" in nombre.lower())

# Método startswith() para verificar si la cadena comienza con una subcadena
print(nombre.startswith("Maga"))

# Método endswith() para verificar si la cadena termina con una subcadena
print(nombre.endswith("Lop"))

# Método isalpha() para verificar si la cadena contiene solo letras
print(nombre.isalpha())

# Método isdigit() para verificar si la cadena contiene solo dígitos
print(nombre.isdigit())

# Método isspace() para verificar si la cadena contiene solo espacios en blanco
print(nombre.isspace())

# Método join() para unir elementos de una lista en una cadena
lista_comidas = ["Ramen", "Dumplings", "Rissoto"]
print(", ".join(lista_comidas))

# Método zfill() para rellenar la cadena con ceros a la izquierda
numero_str = "42"
print(numero_str.zfill(5))

