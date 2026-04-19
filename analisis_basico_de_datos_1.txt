'''
Carga de Datos:
Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta. Cada venta debe incluir las siguientes claves:
«fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2024-01-01»).
«producto»: una cadena de texto que represente el nombre del producto vendido.
«cantidad»: un número entero que represente la cantidad de productos vendidos.
«precio»: un número flotante que represente el precio unitario del producto.
Cálculo de Ingresos Totales:
Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales generados por todas las ventas. Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados.
Análisis del Producto Más Vendido:
Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y los valores sean la cantidad total vendida de cada producto.
Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.
Promedio de Precio por Producto:
Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas. Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.
Ventas por Día:
Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.
Representación de Datos:
Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados. Cada diccionario anidado debe contener:
«cantidad_total»: la cantidad total vendida del producto.
«ingresos_totales»: los ingresos totales generados por la venta del producto.
«precio_promedio»: el precio promedio de venta del producto.
'''
#1. Carga de Datos 
    #Una lista → contiene varias ventas, cada venta → es un diccionario, cada diccionario es una fila de una tabla, cada clave del diccionario → es una columna de la tabla

ventas = [                                                                                    # Lista de diccionarios representando las ventas
    {"fecha": "2024-01-01", "producto": "Producto A", "cantidad": 10, "precio": 5.0},         # Venta del Producto A el 2024-01-01, cantidad 10, precio unitario 5.0
    {"fecha": "2024-01-01", "producto": "Producto B", "cantidad": 5, "precio": 10.0},         # Venta del Producto B el 2024-01-01, cantidad 5, precio unitario 10.0
    {"fecha": "2024-01-02", "producto": "Producto A", "cantidad": 20, "precio": 5.0},         # Venta del Producto A el 2024-01-02, cantidad 20, precio unitario 5.0
    {"fecha": "2024-01-02", "producto": "Producto C", "cantidad": 15, "precio": 7.5},         # Venta del Producto C el 2024-01-02, cantidad 15, precio unitario 7.5
    {"fecha": "2024-01-03", "producto": "Producto B", "cantidad": 10, "precio": 10.0},        # Venta del Producto B el 2024-01-03, cantidad 10, precio unitario 10.0
]

#2.Cálculo de Ingresos Totales
    # Para cada venta en la lista de ventas, multiplicamos la cantidad por el precio y sumamos ese valor a una variable que acumula los ingresos totales.

ingresos_totales = 0                                                                          # Variable para almacenar los ingresos totales
for venta in ventas:                                                                          # Itera sobre cada venta en la lista de ventas
    ingresos_totales += venta["cantidad"] * venta["precio"]                                   # Calcula los ingresos de cada venta y los suma a los ingresos totales
print(f"Ingresos Totales: {ingresos_totales}")                                                # Imprime los ingresos totales

#3. Análisis del Producto Más Vendido
''' Para cada venta, se extrae el nombre del producto y la cantidad vendida. Se utiliza un diccionario para acumular la cantidad total vendida de cada producto. 
Luego, se identifica el producto con la mayor cantidad total vendida utilizando la función max().
'''
ventas_por_producto = {}                                                                      # se crea un diccionario vacío para almacenar la cantidad total vendida de cada producto
for venta in ventas:                                                                          # Itera sobre cada venta en la lista de ventas
    producto = venta["producto"]                                                              # Extrae el nombre del producto de la venta actual
    cantidad = venta["cantidad"]                                                              # Extrae la cantidad vendida de la venta actual
    if producto in ventas_por_producto:                                                       # Verifica si el producto ya está en el diccionario. ventas_por_producto
        ventas_por_producto[producto] += cantidad                                             # Si el producto ya está en el diccionario, suma la cantidad vendida a la cantidad total existente
    else:                                                                                     # Si el producto no está en el diccionario, agrega una nueva entrada con la cantidad vendida
        ventas_por_producto[producto] = cantidad                                              # Agrega el producto al diccionario con la cantidad vendida
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)                  # Utiliza la función max() para encontrar el producto con la mayor cantidad total vendida, utilizando el método get para obtener los valores del diccionario. O tambien significa: “dame la clave cuyo valor es el más grande”
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]                              # Obtiene la cantidad total vendida del producto más vendido desde el diccionario ventas_por_producto
print(f"Producto más vendido: {producto_mas_vendido} ({cantidad_mas_vendida})")               # Imprime el producto más vendido y la cantidad total vendida de ese producto


#4. Promedio de Precio por Producto
'''Para calcular el precio promedio de venta para cada producto, se crea un diccionario donde las claves son los nombres de los productos y los valores son tuplas 
que contienen la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas. Luego, se calcula el precio promedio dividiendo
la suma total de los precios por la cantidad total de unidades vendidas para cada producto. 
'''

precios_por_producto = {}                                                                     # se crea un diccionario vacío para almacenar la suma de los precios y la cantidad total de unidades vendidas de cada producto
for venta in ventas:                                                                          # Itera sobre cada venta en la lista de ventas
    producto = venta["producto"]                                                              # Extrae el nombre del producto de la venta actual
    cantidad = venta["cantidad"]                                                              # Extrae la cantidad vendida de la venta actual
    precio = venta["precio"]                                                                  # Extrae el precio unitario de la venta actual
    if producto in precios_por_producto:                                                      # Verifica si el producto ya está en el diccionario. precios_por_producto
        precios_por_producto[producto] = (                                                    # Si el producto ya está en el diccionario, actualiza la tupla sumando el precio total de la venta actual y la cantidad vendida a los valores existentes
            precios_por_producto[producto][0] + precio * cantidad,                            # Suma el precio total de la venta actual al primer elemento de la tupla (suma de los precios)
            precios_por_producto[producto][1] + cantidad,                                     # Suma la cantidad vendida de la venta actual al segundo elemento de la tupla (cantidad total de unidades vendidas)
        )
    else:
        precios_por_producto[producto] = (precio * cantidad, cantidad)                        # Si el producto no está en el diccionario, agrega una nueva entrada con la tupla que contiene el precio total de las ventas generadas y la cantidad total de unidades vendidas.
precio_promedio_por_producto = {                                                              # Se crea un nuevo diccionario para almacenar el precio promedio de cada producto, calculando el precio promedio dividiendo la suma total de los precios por la cantidad total de unidades vendidas para cada producto.
    producto: precios_por_producto[producto][0] / precios_por_producto[producto][1]           # Calcula el precio promedio dividiendo la suma total de los precios (primer elemento de la tupla) por la cantidad total de unidades vendidas (segundo elemento de la tupla) para cada producto
    for producto in precios_por_producto                                                      # Itera sobre cada producto en el diccionario precios_por_producto para calcular el precio promedio de cada producto
}
print("Precio Promedio por Producto:")                                                        # Imprime el título para la sección de precios promedio por producto
for producto, precio_promedio in precio_promedio_por_producto.items():                        # Itera sobre cada producto y su precio promedio en el diccionario precio_promedio_por_producto para imprimir el precio promedio de cada producto
    print(f"{producto}: {precio_promedio}")                                                   # Imprime el nombre del producto y su precio promedio
    
#5. Ventas por Día
'''Para calcular los ingresos totales por día, se crea un diccionario donde las claves son las fechas y los valores son los ingresos totales generados en cada día.
Luego, se itera sobre la lista de ventas, calculando los ingresos de cada venta (cantidad multiplicada por el precio) y sumándolos al valor correspondiente en el diccionario ingresos_por_dia.
'''

ingresos_por_dia = {}                                                                         # se crea un diccionario vacío para almacenar los ingresos totales generados en cada día
for venta in ventas:                                                                          # Itera sobre cada venta en la lista de ventas
    fecha = venta["fecha"]                                                                    # Extrae la fecha de la venta actual
    ingresos = venta["cantidad"] * venta["precio"]                                            # Calcula los ingresos de la venta actual multiplicando la cantidad por el precio
    if fecha in ingresos_por_dia:                                                             # Verifica si la fecha ya está en el diccionario. ingresos_por_dia
        ingresos_por_dia[fecha] += ingresos                                                   # Si la fecha ya está en el diccionario, suma los ingresos de la venta actual a los ingresos totales existentes para esa fecha
    else:
        ingresos_por_dia[fecha] = ingresos                                                    # Si la fecha no está en el diccionario, agrega una nueva entrada con los ingresos de la venta actual
print("Ingresos por Día:")                                                                    # Imprime el título para la sección de ingresos por día
for fecha, ingresos in ingresos_por_dia.items():                                              # Itera sobre cada fecha y sus ingresos totales en el diccionario ingresos_por_dia para imprimir los ingresos por día
    print(f"{fecha}: {ingresos}")                                                             # Imprime la fecha y los ingresos totales generados en esa fecha

#6. Representación de Datos
'''Para crear un resumen de ventas, se utiliza un diccionario donde las claves son los nombres de los productos y los valores son diccionarios anidados que contienen la cantidad total vendida, los ingresos totales generados por la venta del producto y el precio promedio de venta del producto.
Luego, se itera sobre el diccionario ventas_por_producto para llenar el diccionario resumen_ventas con la información correspondiente de cada producto.
'''
resumen_ventas = {}                                                                           # se crea un diccionario vacío para almacenar el resumen de ventas de cada producto
for producto in ventas_por_producto:                                                          # Itera sobre cada producto en el diccionario ventas_por_producto para llenar el diccionario resumen_ventas con la información correspondiente de cada producto
    cantidad_total = ventas_por_producto[producto]                                            # Obtiene la cantidad total vendida del producto desde el diccionario ventas_por_producto
    ingresos_totales = precios_por_producto[producto][0]                                      # Obtiene los ingresos totales generados por la venta del producto desde el primer elemento de la tupla en el diccionario precios_por_producto
    precio_promedio = precio_promedio_por_producto[producto]                                  # Obtiene el precio promedio de venta del producto desde el diccionario precio_promedio_por_producto
    resumen_ventas[producto] = {                                                              # Agrega una nueva entrada al diccionario resumen_ventas con el nombre del producto como clave y un diccionario anidado como valor que contiene la cantidad total vendida, los ingresos totales y el precio promedio de venta del producto
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos_totales,
        "precio_promedio": precio_promedio,
    }
print("Resumen de Ventas:")                                                                   # Imprime el título para la sección de resumen de ventas
for producto, resumen in resumen_ventas.items():                                              # Itera sobre cada producto y su resumen de ventas en el diccionario resumen_ventas para imprimir el resumen de ventas de cada producto
    print(f"{producto}: {resumen}")                                                           # Imprime el nombre del producto y su resumen de ventas (cantidad total vendida, ingresos totales y precio promedio de venta)


'''
Análisis de ventas

En este ejercicio trabajé con una lista de diccionarios que representan ventas, donde cada una contiene fecha, producto, cantidad y precio.

Primero calculé los ingresos totales recorriendo la lista y acumulando el resultado de multiplicar cantidad por precio en cada venta.

Luego, utilicé un diccionario para agrupar la cantidad vendida por producto, lo que me permitió identificar el producto más vendido y su cantidad total.

Después, calculé el precio promedio por producto considerando el total de ingresos y la cantidad total vendida, obteniendo un promedio más preciso.

También agrupé los ingresos por día usando un diccionario con las fechas como claves.

Finalmente, construí un resumen por producto que incluye cantidad total, ingresos totales y precio promedio.

Este ejercicio me permitió practicar el manejo de estructuras de datos como listas y diccionarios, así como la iteración y el cálculo de métricas clave 
en un contexto de análisis de ventas.
'''