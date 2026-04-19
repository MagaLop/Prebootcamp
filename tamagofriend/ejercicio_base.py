'''
Clase Persona:
    Atributos
        Nombre
        Apellido
        Tamagotchi
    Métodos
        jugar_con_tamagotchi()
        darle_comida()
        curarlo()

class Persona:
    #__init__(nombre, apellido, tamagotchi)

    #Métodos:
        #jugar_con_tamagotchi(): juega e invoca el método de tamagotchi jugar()
        #darle_comida(): le da de comer su tamagotchi invocando al método de tamagotchi comer()
        #curarlo(): sana las heridas de su tamagotchi invocando al método de tamagotchi curar()


Clase Tamagotchi:
    Atributos
        Nombre
        Color
        Salud
        Felicidad
        Energia

    Métodos
        jugar()
        comer()
        curar()

class Tamagotchi:
    #__init__(nombre, color). Puedes colocar valores default para salud, felicidad y energía

    #Métodos:
        #jugar(): incrementa la felicidad el 10, disminuye la salud en 5
        #comer(): incrementa la felicidad en 5, aumenta la salud en 10
        #curar(): incrementa la saludo en 20, disminuye la felicidad en 5


Crea la clase Persona con los atributos mencionados
Crea la clase Tamagotchi con los atributos mencionados
Desarrolla los métodos de jugar_con_tamagotchi(), darle_comida() y curarlo() para la clase Persona
Desarrolla los métodos de jugar(), comer() y curar() para la clase Tamagotchi
Crea una instancia de Persona y asígnale una instancia de Tamagotchi al atributo tamagotchi
Haz que la persona le de comer, cure y juegue con su tamagotchi
BONUS NINJA: Modulariza tus clases, colocándolas en distintos archivos
BONUS SENSEI: Usa la herencia para crear subclases de Tamagotchi con sus personajes. Hecha un vistazo aquí. 
'''


# crear la clase Tamagotchi con los atributos y métodos mencionados en el enunciado.
class Tamagotchi:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.salud = 100
        self.felicidad = 100
        self.energia = 100

# desarrollar los métodos de jugar(), comer() y curar() para la clase Tamagotchi, asegurando que los valores de salud, felicidad y energía se mantengan entre 0 y 100 con min() y max().
    def jugar(self):
        self.felicidad = min(100, self.felicidad + 10)
        self.salud = max(0, self.salud - 5)
        self.energia = max(0, self.energia - 10)
        print(f"{self.nombre} jugó! - Felicidad: {self.felicidad} | Salud: {self.salud} | Energía: {self.energia}")          #esto es una función de impresión para mostrar el resultado de jugar con el Tamagotchi, incluyendo su felicidad, salud y energía después de jugar.

    def comer(self):
        self.felicidad = min(100, self.felicidad + 5)
        self.salud = min(100, self.salud + 10)
        print(f"{self.nombre} comió! - Felicidad: {self.felicidad} | Salud: {self.salud}")

    def curar(self):
        self.salud = min(100, self.salud + 20)
        self.felicidad = max(0, self.felicidad - 5)
        print(f"{self.nombre} fue curado! - Salud: {self.salud} | Felicidad: {self.felicidad}")

# crear la clase Persona con los atributos y métodos mencionados en el enunciado.
class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

# desarrollar los métodos de jugar_con_tamagotchi(), darle_comida() y curarlo() para la clase Persona, asegurando que cada método invoque el método correspondiente del Tamagotchi asociado a la Persona.
    def jugar_con_tamagotchi(self):
        print(f"{self.nombre} juega con {self.tamagotchi.nombre}!")
        self.tamagotchi.jugar()

    def darle_comida(self):
        print(f"{self.nombre} le da comida a {self.tamagotchi.nombre}!")
        self.tamagotchi.comer()

    def curarlo(self):
        print(f"{self.nombre} cura a {self.tamagotchi.nombre}!")
        self.tamagotchi.curar()


# Crear instancias de Tamagotchi y Persona, y realizar interacciones entre ellos para demostrar el funcionamiento de los métodos desarrollados.
tamagotchi1 = Tamagotchi("Tama", "Rojo")
persona1 = Persona("Juan", "Perez", tamagotchi1)

# Interacciones entre la Persona y su Tamagotchi para demostrar el funcionamiento de los métodos desarrollados, incluyendo darle comida, curar y jugar con el Tamagotchi.
persona1.darle_comida()
persona1.curarlo()
persona1.jugar_con_tamagotchi()

# Estado final del Tamagotchi después de las interacciones con la Persona, mostrando su salud, felicidad y energía.
print(f"\n--- Estado final de {tamagotchi1.nombre} ---")
print(f"Salud:     {tamagotchi1.salud}")
print(f"Felicidad: {tamagotchi1.felicidad}")
print(f"Energía:   {tamagotchi1.energia}")

# BONUS NINJA: Modulariza tus clases, colocándolas en distintos archivos (echo, ir a la carpeta tamagofriend)
# Para modularizar las clases, crear dos archivos: persona.py y tamagotchi.py, ubicados en la carpeta tamagofriend
