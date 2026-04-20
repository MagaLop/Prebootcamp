numero1 = 70                                # Variable de tipo entero
numero2 = 3.14                              # Variable de tipo flotante
booleano = False                            # Variable de tipo booleano
cadena = 'Hola Mundo'                       # Variable de tipo cadena de texto
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate']    # Variable de tipo lista
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} # Variable de tipo diccionario
frutas = ('guayaba', 'fresa', 'papaya')     # Variable de tipo tupla
print(type(frutas))                         # Imprime el tipo de dato de la variable frutas
print(ingredientes_pastel[2])               # Imprime el tercer elemento de la lista ingredientes_pastel
ingredientes_pastel.append('Mantequilla')   # Agrega un nuevo elemento al final de la lista ingredientes_pastel
print(persona['nombre'])                    # Imprime el valor asociado a la clave 'nombre' en el diccionario persona
persona['nombre'] = 'Kevin'                 # Modifica el valor asociado a la clave 'nombre' en el diccionario persona
persona['color_ojos'] = 'cafe'              # Agrega una nueva clave-valor al diccionario persona
print(frutas[2])                            # Imprime el tercer elemento de la tupla frutas

if numero1 > 45:                            # Condicional para verificar si numero1 es mayor que 45
    print("Numero mayor")                   # Imprime "Numero mayor" si la condición es verdadera
else:                                       # Si la condición es falsa, se ejecuta esta parte
    print("Numero menor")                   # Imprime "Numero menor" si la condición es falsa

if len(cadena) < 5:                         # Condicional para verificar si la longitud de la cadena es menor que 5
    print("Cadena corta")                   # Imprime "Cadena corta" si la condición es verdadera
elif len(cadena) > 15:                      # Condicional para verificar si la longitud de la cadena es mayor que 15
    print("Cadena larga")                   # Imprime "Cadena larga" si la condición es verdadera
else:                                       # Si ninguna de las condiciones anteriores es verdadera, se ejecuta esta parte
    print("Cadena perfecta")                # Imprime "Cadena perfecta" si ninguna de las condiciones anteriores es verdadera

for x in range(8):                          # Bucle for que itera desde 0 hasta 7
    print(x)                                # Imprime el valor de x en cada iteración
for x in range(2,8):                        # Bucle for que itera desde 2 hasta 7
    print(x)                                # Imprime el valor de x en cada iteración
for x in range(2,8,2):                      # Bucle for que itera desde 2 hasta 7 con un paso de 2 (2, 4, 6)
    print(x)                                # Imprime el valor de x en cada iteración
x = 0                                       # Variable de control para el bucle while
while(x < 8):                               # Bucle while que se ejecuta mientras x sea menor que 8
    print(x)                                # Imprime el valor de x en cada iteración
    x += 1                                  # Incrementa el valor de x en 1 en cada iteración

ingredientes_pastel.pop()                   # Elimina el último elemento de la lista ingredientes_pastel
ingredientes_pastel.pop(1)                  # Elimina el elemento en la posición 1 (segundo elemento) de la lista ingredientes_pastel

print(persona)                              # Elimina la clave 'color_ojos' y su valor asociado del diccionario persona, luego imprime el diccionario actualizado
persona.pop('color_ojos')                   # Elimina la clave 'color_ojos' y su valor asociado del diccionario persona
print(persona)                              # Imprime el diccionario persona después de eliminar la clave 'color_ojos'

for ingrediente in ingredientes_pastel:     # Bucle for que itera sobre cada elemento en la lista ingredientes_pastel
    if ingrediente == 'Harina':             # Si el ingrediente es 'Harina', se ejecuta esta parte
        continue                            # La sentencia continue hace que el bucle salte a la siguiente iteración, omitiendo el resto del código dentro del bucle para esta iteración
    print('Después de la primera sentencia')# Imprime 'Después de la primera sentencia' para cada ingrediente, excepto cuando el ingrediente es 'Harina', en cuyo caso se omite esta impresión
    if ingrediente == 'Chocolate':          # Si el ingrediente es 'Chocolate', se ejecuta esta parte
        break                               # La sentencia break hace que el bucle se detenga completamente, saliendo del bucle incluso si hay más elementos por iterar

def imprime_hola_10_veces():                # Función que imprime 'Hola' 10 veces
    for numero in range(10):                # Bucle for que itera desde 0 hasta 9
        print('Hola')                       # Imprime 'Hola' en cada iteración del bucle

imprime_hola_10_veces()                     # Llama a la función imprime_hola_10_veces para ejecutar su código y imprimir 'Hola' 10 veces

def imprime_hola_n_veces(n):                # Función que imprime 'Hola' n veces, donde n es un parámetro que se le pasa a la función
    for numero in range(n):                 # Bucle for que itera desde 0 hasta n-1
        print('Hola')                       # Imprime 'Hola' en cada iteración del bucle

imprime_hola_n_veces(5)                     # Llama a la función imprime_hola_n_veces con el argumento 5, lo que hace que se imprima 'Hola' 5 veces

def imprime_hola_n_o_diez_veces(n = 10):    # Función que imprime 'Hola' n veces, donde n es un parámetro opcional que por defecto es 10
    for numero in range(n):                 # Bucle for que itera desde 0 hasta n-1
        print('Hola')                       # Imprime 'Hola' en cada iteración del bucle

imprime_hola_n_o_diez_veces()               # Llama a la función imprime_hola_n_o_diez_veces sin argumentos, lo que hace que se imprima 'Hola' 10 veces debido al valor por defecto de n
imprime_hola_n_o_diez_veces(5)              # Llama a la función imprime_hola_n_o_diez_veces con el argumento 5, lo que hace que se imprima 'Hola' 5 veces


"""
Sección BONUS
"""

# print(numero3)                            # Imprime el valor de la variable numero3, pero esta variable no ha sido definida previamente, lo que resultará en un error de NameError
# numero3 = 86                              # Define la variable numero3 con el valor 86, pero esta línea de código no se ejecutará debido al error en la línea anterior
# frutas[0] = 'naranja'                     # Intenta modificar el primer elemento de la tupla frutas, pero las tuplas son inmutables, lo que resultará en un error de TypeError
# print(persona['hobbies'])                 # Intenta acceder a la clave 'hobbies' en el diccionario persona, pero esta clave no existe, lo que resultará en un error de KeyError
# print(ingredientes_pastel[11])            # Intenta acceder al elemento en la posición 11 de la lista ingredientes_pastel, pero esta posición no existe (la lista tiene menos de 12 elementos), lo que resultará en un error de IndexError
#   print(booleano)                         # Intenta imprimir el valor de la variable booleano, pero esta línea de código tiene una indentación incorrecta (espacio adicional al inicio), lo que resultará en un error de IndentationError
# frutas.append('manzana')                  # Intenta agregar un nuevo elemento a la tupla frutas utilizando el método append, pero las tuplas no tienen este método, lo que resultará en un error de AttributeError
# frutas.pop(1)                             # Intenta eliminar el elemento en la posición 1 de la tupla frutas utilizando el método pop, pero las tuplas no tienen este método, lo que resultará en un error de AttributeError