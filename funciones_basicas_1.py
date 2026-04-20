'''
Revisa los siguientes fragmentos de código e intenta predecir la salida (lo que se verá impreso en la terminal). 
Teniendo tu predicción lista, verifica que sea correcta ejecutando el fragmento de código.
'''
#1
def cantidad_de_vocales():
    return 5
print(cantidad_de_vocales())
# retorna 5

#2
def cantidad_de_glaciares_argentina():
    return 16968
print(cantidad_de_dias_o_meses_o_semanas_en_anio() + cantidad_de_glaciares_argentina())
# ERROR, la funcion cant...() no esta definida

#3
def anio_independencia_chile():
    return 1810
    return 1851
print(anio_independencia_chile())
# deberia llegar hasta el primer return...

#4
def cantidad_de_departamentos_colombia():
    return(32)
    print(33)
print(cantidad_de_departamentos_colombia())
#El print(33) nunca se ejecuta porque está después del return.

#5
def altura_machu_picchu():
    print(2438)
x = altura_machu_picchu()
print(x)
# Debería imprimir 2438, pero x es igual a nada... la altura no sale por ningun lado

#6
def suma(a, b):
    print(a+b)
print(suma(10, 5) + suma(4, 3))
# segun yo es 15 + 7, pero creo que es incorrecto, porque me da error, creo que es debido a la suma + 
'''
15
7
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType''''

#7
def concatenar(a, b):
    return str(b) + str(a)
print(concatenar(7, 15))
# 157, y los numeros se convierten en cadenas, al concatenar, 15 + 7 = 157

#8
def paises_latinoamerica_o_lenguas_indigenas():
    a = 560
    print(a)
    if a < 180:
        return 33
    else:
        return 46
    return 21
print(paises_latinoamerica_o_lenguas_indigenas())
# imprime a
#como no sabemos a sigue hasta el else y retorna 46.

#9
def cantidad_de_dias_o_meses_o_semanas_en_anio(a, b):
    if a < b:
        return 365
    else:
        return 12
    return 52
print(cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4))
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4) + cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))
'''
entonces segun veo hay que convertir a y b en los nmeros de abajo:
1 < 3 = 365
7 < 4 = 12
12 + 365 = 377
'''

#10
def sumatoria(a, b):
    return a + b
    return 157
print(sumatoria(3, 4))
# 7, el primer retun es a + b entonces 3 + 4 =7


#11
a = 150             # a global
print(a)            #imprime 150
def funcion():      # se define funcion pero no se ejecuta
    a = 350
    print(a)        # todavia no
print(a)            #imprime 150
funcion()           #ejecuto funcion, imprime 350
print(a)            #imprime 150

#12
a = 150
print(a)
def funcion():
    a = 350
    print(a)
    return a
print(a)
funcion()
print(a)
# 150, 150, 350, 150, el return no se guarda en ninguna variable

#13
a = 150             # variable global
print(a)            # 150
def funcion():      #se define funcion, el valor de a es 350. imprime 350 y retorna 350
    a = 350
    print(a)
    return a
print(a)            #150
a = funcion()       #ejecuta funcion, imprime 350, retorna 350, se guarda en la variable global a
print(a)            # la variable a ahora es 350, por tanto imprime 350
# 150, 150, 350, 350

#14
def funcion1():
    print(3)
    funcion2()
    print(2)
def funcion2():
    print(1)
funcion1()
'''
Se definen las funciones 1 y 2 
llama a ella en funcion1():
imprime: 3
llama a funcion2()
dentro de la funcion imprime: 1 
termina funcion2 y vuelvo a funcion1
imprimo: 2
resultado: 3, 1, 2.
'''

#15
def funcion1():
    print(3)
    a = funcion2()
    print(a)
    return 4
def funcion2():
    print(1)
    return 0

b = funcion1()
print(b)
'''
defino funciones 1 y 2
llamado: b que es la funcion1
imprimo 3
a llama a funcion2
imprimo 1
retorno 0
ahora a es igual a 0
vuelvo a funcion1
imprimo 0
retorno 4
y b es igual a 4
imprimo 4
resultado: 3, 1, 0, 4
'''