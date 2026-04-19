'''
1. Crea la clase TarjetaCredito con los atributos de saldo_pagar, limite_credito, intereses
2. Crea el método compra para la clase TarjetaCredito
3. Crea el método pago para la clase TarjetaCredito
4. Crea el método mostrar_info_tarjeta para la clase TarjetaCredito
5. Crea el método cobrar_interes para la clase TarjetaCredito
6. Crea 3 tarjetas

7. Para la primera tarjeta, haz 2 compras y un pago. Luego cobra los intereses y muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
8. Para la segunda tarjeta, haz 3 compras y 2 pagos. Luego cobra los intereses y muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
9. Para la tercera tarjeta, haz 5 compras y excede su límite de crédito. Luego muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
10. BONUS: crea un método de clase para imprimir todas las instancias de la información de las tarjetas creadas.
'''
# 1. Creación de la clase TarjetaCredito con los atributos de saldo_pagar, limite_credito, intereses

class TarjetaCredito:                                                                           # Atributo de clase para almacenar todas las tarjetas creadas (BONUS)
    tarjetas = []                                                                               # Lista para almacenar las tarjetas creadas (BONUS)

    def __init__(self, limite_credito, intereses, saldo_pagar=0):                               # Constructor con parámetros para inicializar los atributos de la tarjeta
        self.saldo_pagar = saldo_pagar                                                          # Saldo a pagar, inicializado en 0 por defecto
        self.limite_credito = limite_credito                                                    # Límite de crédito, pasado como argumento al crear la tarjeta
        self.intereses = intereses                                                              # Tasa de intereses, pasada como argumento al crear la tarjeta

        TarjetaCredito.tarjetas.append(self)                                                    # Agregar la tarjeta creada a la lista de tarjetas (BONUS)

# 2. Método compra para la clase TarjetaCredito

    def compra(self, monto):                                                                    # Método para realizar una compra, recibe el monto de la compra como argumento
        if self.saldo_pagar + monto <= self.limite_credito:                                     # Verificar si la compra no excede el límite de crédito
            self.saldo_pagar += monto                                                           # Si la compra es válida, se suma el monto al saldo a pagar
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")                      # Si la compra excede el límite, se muestra un mensaje de rechazo
        return self                                                                             # Retornar self para permitir la encadenación de métodos

# 3. Método pago para la clase TarjetaCredito

    def pago(self, monto):                                                                      # Método para realizar un pago, recibe el monto del pago como argumento
        if monto > self.saldo_pagar:                                                               # Verificar si el monto del pago es mayor al saldo a pagar
            print("Pago Excedido, el monto del pago es mayor al saldo a pagar")                     # Si el pago excede el saldo, se muestra un mensaje de error
        else:
            self.saldo_pagar -= monto                                                               # Si el pago es válido, se resta el monto del pago al saldo a pagar
        return self                                                                                # Retornar self para permitir la encadenación de métodos

# 4. Método mostrar_info_tarjeta para la clase TarjetaCredito

    def mostrar_info_tarjeta(self):                                                             # Método para mostrar la información de la tarjeta
        print(f"Saldo a Pagar: ${self.saldo_pagar}")                                            # Imprimir el saldo a pagar
        return self                                                                             # Retornar self para permitir la encadenación de métodos
    
# 5. Método cobrar_interes para la clase TarjetaCredito

    def cobrar_interes(self):                                                                   # Método para cobrar intereses sobre el saldo a pagar
        if self.saldo_pagar > 0:                                                                # Verificar si hay saldo a pagar para cobrar intereses
            self.saldo_pagar += self.saldo_pagar * self.intereses                               # Si hay saldo, se calcula el interés y se suma al saldo a pagar
        return self                                                                             # Retornar self para permitir la encadenación de métodos


# 10. BONUS: Método de clase para imprimir todas las instancias de la información de las tarjetas creadas
    @classmethod                                                                                         # Decorador (@classmethod) para indicar que este método es un método de clase, lo que permite acceder a los atributos de clase
    def mostrar_todas(cls):                                                                              # Método de clase para mostrar la información de todas las tarjetas creadas, recibe cls como argumento para acceder a los atributos de clase
        print("=== TODAS LAS TARJETAS ===")                                                              # Imprimir un encabezado para indicar que se mostrarán todas las tarjetas
        for i, tarjeta in enumerate(cls.tarjetas, 1):                                                    # Iterar sobre la lista de tarjetas creadas, usando enumerate para obtener el índice y la tarjeta
            print(f"Tarjeta {i}: Saldo = ${tarjeta.saldo_pagar}, Límite = ${tarjeta.limite_credito}")    # Imprimir la información de cada tarjeta, incluyendo el saldo a pagar y el límite de crédito


#6. ----------- CREACIÓN DE TARJETAS -----------
# Crear 3 tarjetas con diferentes límites de crédito e intereses

tarjeta1 = TarjetaCredito(1000, 0.02)
tarjeta2 = TarjetaCredito(1500, 0.03)
tarjeta3 = TarjetaCredito(500, 0.01)

# 7, 8 y 9----------- OPERACIONES ENCADENADAS -----------
# Realizar operaciones encadenadas para cada tarjeta según las instrucciones

# Tarjeta 1: 2 compras, 1 pago, interés y mostrar
tarjeta1.compra(200).compra(300).pago(100).cobrar_interes().mostrar_info_tarjeta()

# Tarjeta 2: 3 compras, 2 pagos, interés y mostrar
tarjeta2.compra(400).compra(200).compra(300).pago(150).pago(100).cobrar_interes().mostrar_info_tarjeta()

# Tarjeta 3: 5 compras (excediendo límite), mostrar
tarjeta3.compra(100).compra(150).compra(200).compra(100).compra(200).mostrar_info_tarjeta()

# BONUS: mostrar todas
TarjetaCredito.mostrar_todas()


# El código define la clase TarjetaCredito con métodos para realizar compras, pagos, cobrar intereses y mostrar información de la tarjeta. 
# Además, se crea un método de clase para mostrar todas las tarjetas creadas.
# Luego, se crean tres tarjetas y se realizan operaciones encadenadas según las instrucciones. 
# Finalmente, se muestra la información de todas las tarjetas creadas.

