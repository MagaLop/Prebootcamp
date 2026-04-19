'''
pagar_tarjeta(self, monto): crea un método que pague un monto de la tarjeta de crédito, haciendo que se reduzca el saldo_pagar.
mostrar_saldo_usuario(self): crea un método que imprima el nombre completo del usuario y el saldo a pagar de su tarjeta.Ejemplo: “Usuario: Nariyoshi Miyagi, Saldo a Pagar: $50”
BONUS: transferir_deuda(self, otro_usuario, monto): crea un método que reduzca la deuda (saldo_pagar) del usuario por el monto, y agrega esa cantidad al saldo_pagar de otro_usuario
Crea el archivo un Python con la clase Usuario, con la base que te proporcionamos
Agrega el método pagar_tarjeta a la clase Usuario
Agrega el método mostrar_saldo_usuario a la clase Usuario
Crea 3 instancias de la clase Usuario
Haz que el primer usuario haga 2 compras y luego pague su tarjeta. Muestra su saldo
Haz que el segundo usuario haga 1 compra y luego pague 2 veces su tarjeta. Muestra su saldo
Haz que el tercer usuario haga 3 compras y luego pague su tarjeta 4 veces. Muestra su saldo
'''

'''
class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

    def pagar_tarjeta(self, monto):
        if monto > self.saldo_pagar:
        print("Estás pagando más de lo que debes")
        self.saldo_pagar = 0    
            else:
                self.saldo_pagar -= monto

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo a Pagar: ${self.saldo_pagar}")
    def transferir_deuda(self, otro_usuario, monto):
        self.saldo_pagar -= monto
        otro_usuario.saldo_pagar += monto


# Crear instancias de la clase Usuario
usuario1 = Usuario("Nariyoshi", "Miyagi", "nariyoshi.miyagi@example.com")
usuario2 = Usuario("Ryo", "Kaneko", "ryo.kaneko@example.com")
usuario3 = Usuario("Tsunetaro", "Kaneko", "tsunetaro.kaneko@example.com")

# Usuario 1 hace 2 compras y luego paga su tarjeta
usuario1.hacer_compra(10000)
usuario1.hacer_compra(5000)
usuario1.pagar_tarjeta(12000)
usuario1.mostrar_saldo_usuario()

# Usuario 2 hace 1 compra y luego paga 2 veces su tarjeta
usuario2.hacer_compra(15000)
usuario2.pagar_tarjeta(7000)
usuario2.pagar_tarjeta(3000)
usuario2.mostrar_saldo_usuario()

# Usuario 3 hace 3 compras y luego paga su tarjeta 4 veces
usuario3.hacer_compra(8000)
usuario3.hacer_compra(6000)
usuario3.hacer_compra(4000)
usuario3.pagar_tarjeta(5000)
usuario3.pagar_tarjeta(3000)
usuario3.pagar_tarjeta(2000)
usuario3.pagar_tarjeta(1000)
usuario3.mostrar_saldo_usuario()

'''
class Usuario:                                                                                  # Definición de la clase Usuario
    def __init__(self, nombre, apellido, email):                                                # Método constructor para inicializar los atributos del usuario
        self.nombre = nombre                                                                    # Atributo para el nombre del usuario
        self.apellido = apellido                                                                # Atributo para el apellido del usuario
        self.email = email                                                                      # Atributo para el correo electrónico del usuario
        self.limite_credito = 30000                                                             # Atributo para el límite de crédito del usuario
        self.saldo_pagar = 0                                                                    # Atributo para el saldo a pagar del usuario

    def hacer_compra(self, monto):                                                              # Método para realizar una compra, recibe el monto de la compra como argumento
        if self.saldo_pagar + monto > self.limite_credito:                                      # Verifica si la compra excede el límite de crédito
            print("Compra rechazada: excede el límite de crédito")                              # Si la compra excede el límite, se muestra un mensaje de rechazo
        else:
            self.saldo_pagar += monto                                                           # Si la compra es válida, se suma el monto al saldo a pagar
        return self                                                                             # Retorna la instancia para permitir encadenar métodos

    def pagar_tarjeta(self, monto):                                                             # Método para pagar la tarjeta, recibe el monto a pagar como argumento
        if monto > self.saldo_pagar:                                                            # Verifica si el monto a pagar es mayor que el saldo a pagar
            print("Estás pagando más de lo que debes")                                          # Si el monto a pagar es mayor, se muestra un mensaje de advertencia
            self.saldo_pagar = 0                                                                # Si el monto a pagar es mayor, se establece el saldo a pagar en 0
        else:
            self.saldo_pagar -= monto                                                           # Si el monto a pagar es válido, se resta del saldo a pagar
        return self                                                                             # Retorna la instancia para permitir encadenar métodos

    def mostrar_saldo_usuario(self):                                                            # Método para mostrar el saldo del usuario
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo a Pagar: ${self.saldo_pagar}")    # Imprime el nombre completo del usuario y el saldo a pagar
        return self                                                                             # Retorna la instancia para permitir encadenar métodos

    def transferir_deuda(self, otro_usuario, monto):                                            # Método para transferir deuda a otro usuario, recibe el otro usuario y el monto a transferir como argumentos
        if monto > self.saldo_pagar:                                                            # Verifica si el monto a transferir es mayor que el saldo a pagar
            print("No tienes suficiente deuda para transferir")                                 # Si el monto a transferir es mayor, se muestra un mensaje de advertencia
        else:
            self.saldo_pagar -= monto                                                           # Si el monto a transferir es válido, se resta del saldo a pagar del usuario actual
            otro_usuario.saldo_pagar += monto                                                   # Si el monto a transferir es válido, se suma al saldo a pagar del otro usuario
        return self                                                                             # Retorna la instancia para permitir encadenar métodos


# Crear instancias                                                                              # Creación de instancias de la clase Usuario
usuario1 = Usuario("Nariyoshi", "Miyagi", "nariyoshi.miyagi@example.com")
usuario2 = Usuario("Ryo", "Kaneko", "ryo.kaneko@example.com")
usuario3 = Usuario("Tsunetaro", "Kaneko", "tsunetaro.kaneko@example.com")


# Usuario 1: 2 compras y paga, muestra saldo, utilizando encadenamiento de métodos, lo que permite llamar a varios métodos en una sola línea de código
usuario1.hacer_compra(10000).hacer_compra(5000).pagar_tarjeta(12000).mostrar_saldo_usuario()


# Usuario 2: 1 compra y paga 2 veces, muestra saldo, utilizando encadenamiento de métodos, lo que permite llamar a varios métodos en una sola línea de código
usuario2.hacer_compra(15000).pagar_tarjeta(7000).pagar_tarjeta(3000).mostrar_saldo_usuario()


# Usuario 3: 3 compras y paga 4 veces, muestra saldo, utilizando encadenamiento de métodos, lo que permite llamar a varios métodos en una sola línea de código
usuario3.hacer_compra(8000).hacer_compra(6000).hacer_compra(4000)\
        .pagar_tarjeta(5000).pagar_tarjeta(3000).pagar_tarjeta(2000).pagar_tarjeta(1000)\
        .mostrar_saldo_usuario()

# Transferencia de deuda entre usuarios, utilizando encadenamiento de métodos, lo que permite llamar a varios métodos en una sola línea de código
usuario1.transferir_deuda(usuario2, 2000).mostrar_saldo_usuario()                                # Transfiere $2000 de la deuda de usuario1 a usuario2 y muestra el saldo de usuario1
usuario2.mostrar_saldo_usuario()                                                                 # Muestra el saldo de usuario2 después de la transferencia de deuda

# Usuario 1 intenta transferir más deuda de la que tiene, utilizando encadenamiento de métodos, lo que permite llamar a varios métodos en una sola línea de código
usuario1.transferir_deuda(usuario3, 5000).mostrar_saldo_usuario()                                # Intenta transferir $5000 de la deuda de usuario1 a usuario3, pero usuario1 no tiene suficiente deuda para transferir, muestra un mensaje de advertencia y el saldo de usuario1 permanece sin cambios
usuario3.mostrar_saldo_usuario()                                                                 # Muestra el saldo de usuario3 después del intento de transferencia de deuda, el saldo de usuario3 permanece sin cambios debido a que la transferencia no fue exitosa

# Usuario 2 intenta pagar más de lo que debe, utilizando encadenamiento de métodos, lo que permite llamar a varios métodos en una sola línea de código
usuario2.pagar_tarjeta(20000).mostrar_saldo_usuario()                                            # Intenta pagar $20000 en la tarjeta de usuario2, pero el monto a pagar es mayor que el saldo a pagar, muestra un mensaje de advertencia y el saldo de usuario2 se establece en 0

# Usuario 3 intenta hacer una compra que excede su límite de crédito, utilizando encadenamiento de métodos, lo que permite llamar a varios métodos en una sola línea de código
usuario3.hacer_compra(25000).mostrar_saldo_usuario()                                             # Intenta hacer una compra de $25000 para usuario3, pero la compra excede el límite de crédito, muestra un mensaje de rechazo y el saldo a pagar de usuario3 permanece sin cambios

# Usuario 3 hace una compra válida, utilizando encadenamiento de métodos, lo que permite llamar a varios métodos en una sola línea de código
usuario3.hacer_compra(20000).mostrar_saldo_usuario()                                             # Hace una compra de $20000 para usuario3, que es válida y no excede el límite de crédito, muestra el nuevo saldo a pagar de usuario3 después de la compra

# Usuario 3 paga su tarjeta con un monto válido, utilizando encadenamiento de métodos, lo que permite llamar a varios métodos en una sola línea de código
usuario3.pagar_tarjeta(15000).mostrar_saldo_usuario()                                            # Paga $15000 en la tarjeta de usuario3, que es un monto válido y no excede el saldo a pagar, muestra el nuevo saldo a pagar de usuario3 después del pago

# Usuario 3 paga su tarjeta con un monto que excede el saldo a pagar, utilizando encadenamiento de métodos, lo que permite llamar a varios métodos en una sola línea de código
usuario3.pagar_tarjeta(10000).mostrar_saldo_usuario()                                            # Intenta pagar $10000 en la tarjeta de usuario3, pero el monto a pagar es mayor que el saldo a pagar, muestra un mensaje de advertencia y el saldo de usuario3 se establece en 0

# Usuario 1 muestra su saldo final, utilizando encadenamiento de métodos, lo que permite llamar a varios métodos en una sola línea de código
usuario1.mostrar_saldo_usuario()                                                                 # Muestra el saldo final de usuario1 después de todas las operaciones realizadas, incluyendo compras, pagos y transferencias de deuda

# Usuario 2 muestra su saldo final, utilizando encadenamiento de métodos, lo que permite llamar a varios métodos en una sola línea de código
usuario2.mostrar_saldo_usuario()                                                                 # Muestra el saldo final de usuario2 después de todas las operaciones realizadas, incluyendo compras, pagos y transferencias de deuda

# Usuario 3 muestra su saldo final, utilizando encadenamiento de métodos, lo que permite llamar a varios métodos en una sola línea de código
usuario3.mostrar_saldo_usuario()                                                                 # Muestra el saldo final de usuario3 después de todas las operaciones realizadas, incluyendo compras, pagos y transferencias de deuda

'''
Actualiza el método __init__ de la clase Usuario
Actualiza el método hacer_compra de la clase Usuario
Actualiza el método pagar_tarjeta de la clase Usuario
Actualiza el método mostrar_saldo_usuario de la clase Usuario
BONUS: permite que un usuario tenga varias tarjetas de crédito.
Actualiza los métodos para que el usuario pueda especificar en qué cuenta está realizando una compra o a qué tarjeta está pagando.

Te dejamos un fragmento de código ejemplo para que veas cómo acceder a los métodos de la clase TarjetaCredito:

def metodo_ejemplo(self):
    #Llamar a los métodos de tarjeta
    self.tarjeta.compra(100)
    #Acceder a sus atributos
    print(self.tarjeta.saldo_pagar)
'''

# La clase TarjetaCredito representa una tarjeta de crédito con un límite de crédito y un saldo a pagar
class TarjetaCredito:
    def __init__(self, limite_credito):
        self.limite_credito = limite_credito  # Límite de crédito de la tarjeta
        self.saldo_pagar = 0                  # Saldo a pagar en la tarjeta

    def compra(self, monto):
        if self.saldo_pagar + monto > self.limite_credito:  # Verifica si la compra excede el límite de crédito
            print("Compra rechazada: excede el límite de crédito")  # Si la compra excede el límite, se muestra un mensaje de rechazo
        else:
            self.saldo_pagar += monto  # Si la compra es válida, se suma el monto al saldo a pagar

    def pagar(self, monto):
        if monto > self.saldo_pagar:  # Verifica si el monto a pagar es mayor que el saldo a pagar
            print("Estás pagando más de lo que debes")  # Si el monto a pagar es mayor, se muestra un mensaje de advertencia
            self.saldo_pagar = 0  # Si el monto a pagar es mayor, se establece el saldo a pagar en 0
        else:
            self.saldo_pagar -= monto  # Si el monto a pagar es válido, se resta del saldo a pagar


# La clase Usuario representa a un usuario con un nombre, apellido, email y una lista de tarjetas de crédito
class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre  # Nombre del usuario
        self.apellido = apellido  # Apellido del usuario
        self.email = email  # Correo electrónico del usuario
        self.tarjetas = []  # Lista de tarjetas de crédito del usuario

    def agregar_tarjeta(self, tarjeta):
        self.tarjetas.append(tarjeta)  # Agrega una tarjeta de crédito a la lista de tarjetas del usuario

    def hacer_compra(self, monto, tarjeta_index=0):
        if tarjeta_index < len(self.tarjetas):  # Verifica si el índice de la tarjeta es válido
            self.tarjetas[tarjeta_index].compra(monto)  # Realiza la compra en la tarjeta especificada
        else:
            print("Índice de tarjeta no válido")  # Si el índice no es válido, se muestra un mensaje de error

    def pagar_tarjeta(self, monto, tarjeta_index=0):
        if tarjeta_index < len(self.tarjetas):  # Verifica si el índice de la tarjeta es válido
            self.tarjetas[tarjeta_index].pagar(monto)  # Realiza el pago en la tarjeta especificada
        else:
            print("Índice de tarjeta no válido")  # Si el índice no es válido, se muestra un mensaje de error

    def mostrar_saldo_usuario(self):
        for i, tarjeta in enumerate(self.tarjetas):  # Itera sobre las tarjetas del usuario
            print(f"Usuario: {self.nombre} {self.apellido}, Tarjeta {i+1}, Saldo a Pagar: ${tarjeta.saldo_pagar}")  # Imprime el saldo a pagar para cada tarjeta

            # Aquí podrías agregar lógica adicional para mostrar el saldo total a pagar sumando los saldos de todas las tarjetas, si lo deseas

# Crear instancias de la clase Usuario y TarjetaCredito
usuario1 = Usuario("Nariyoshi", "Miyagi", "nariyoshi.miyagi@example.com")
tarjeta1 = TarjetaCredito(1000)
tarjeta2 = TarjetaCredito(2000)

# Agregar tarjetas al usuario
usuario1.agregar_tarjeta(tarjeta1)
usuario1.agregar_tarjeta(tarjeta2)

# Usuario 1 hace compras y paga en diferentes tarjetas
usuario1.hacer_compra(500, tarjeta_index=0)  # Compra de $500 en la tarjeta 1
usuario1.hacer_compra(1500, tarjeta_index=1)  # Compra de $1500 en la tarjeta 2
usuario1.pagar_tarjeta(200, tarjeta_index=0)  # Pago de $200 en la tarjeta 1
usuario1.pagar_tarjeta(500, tarjeta_index=1)  # Pago de $500 en la tarjeta 2
usuario1.mostrar_saldo_usuario()  # Muestra el saldo a pagar para cada tarjeta

# Aquí podrías agregar más usuarios, tarjetas y realizar más operaciones para probar la funcionalidad de la clase Usuario con múltiples tarjetas de crédito.
usuario2 = Usuario("Ryo", "Kaneko", "ryo.kaneko@example.com")
tarjeta3 = TarjetaCredito(1500)
tarjeta4 = TarjetaCredito(2500)

# Agregar tarjetas al usuario 2
usuario2.agregar_tarjeta(tarjeta3)
usuario2.agregar_tarjeta(tarjeta4)

# Usuario 2 hace compras y paga en diferentes tarjetas
usuario2.hacer_compra(300, tarjeta_index=0)  # Compra de $300 en la tarjeta 1
usuario2.hacer_compra(800, tarjeta_index=1)  # Compra de $800 en la tarjeta 2
usuario2.pagar_tarjeta(100, tarjeta_index=0)  # Pago de $100 en la tarjeta 1
usuario2.pagar_tarjeta(300, tarjeta_index=1)  # Pago de $300 en la tarjeta 2
usuario2.mostrar_saldo_usuario()  # Muestra el saldo a pagar para cada tarjeta
