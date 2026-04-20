class Tamagotchi:                                                         # Define la clase Tamagotchi, que representa a una mascota virtual con atributos y métodos para interactuar con ella
    def __init__(self, nombre, color):                                    # Constructor para inicializar el Tamagotchi con un nombre, color y atributos de salud, felicidad y energía con valores predeterminados de 100
        self.nombre = nombre
        self.color = color
        self.salud = 100
        self.felicidad = 100
        self.energia = 100

    def ajustar_valor(self, valor, cambio):                               # Método auxiliar para ajustar un valor (salud, felicidad o energía) asegurando que se mantenga entre 0 y 100
        return max(0, min(100, valor + cambio))                           # Devuelve el valor ajustado, asegurando que no sea menor a 0 ni mayor a 100

# Implementa el método mostrar_estado para mostrar el estado actual del Tamagotchi, incluyendo su salud, felicidad y energía
    def mostrar_estado(self):
        print(f"""
    🐣 {self.nombre} ({self.color})
    ❤️ Salud: {self.salud}
    😊 Felicidad: {self.felicidad}
    ⚡ Energía: {self.energia}
    """)
        
    def jugar(self):
        if self.energia < 20:
            self.felicidad = self.ajustar_valor(self.felicidad, -5)
            print(f"{self.nombre} está muy cansado 😴")
            self.mostrar_estado()
            return

        self.felicidad = self.ajustar_valor(self.felicidad, +10)
        self.salud = self.ajustar_valor(self.salud, -5)
        self.energia = self.ajustar_valor(self.energia, -10)
        print(f"{self.nombre} jugó 🎮")
        self.mostrar_estado()

    def comer(self):
        self.felicidad = self.ajustar_valor(self.felicidad, +5)
        self.salud = self.ajustar_valor(self.salud, +10)
        self.energia = self.ajustar_valor(self.energia, +15)
        print(f"{self.nombre} comió 🍎")
        self.mostrar_estado()

    def curar(self):
        self.salud = self.ajustar_valor(self.salud, +20)
        self.felicidad = self.ajustar_valor(self.felicidad, -5)
        print(f"{self.nombre} fue curado 💊")
        self.mostrar_estado()

    def ignorar(self):
        self.felicidad = self.ajustar_valor(self.felicidad, -15)
        self.salud = self.ajustar_valor(self.salud, -5)
        print(f"{self.nombre} se siente ignorado 😢")
        self.mostrar_estado()

            
# Los emoticonos son opcionales, pero pueden hacer que la experiencia de interactuar con el Tamagotchi sea más divertida y visualmente atractiva.
# Los emoticones fueron aagregados directamente como caracteres Unicode dentro de los strings de Python


# BONUS SENSEI: Usa la herencia para crear subclases de Tamagotchi con sus personajes. Hecha un vistazo aquí.
class Mametchi(Tamagotchi):
    def jugar(self):
        super().jugar()  
        self.felicidad = self.ajustar_valor(self.felicidad, +5)
        print("✨ Mametchi inventó algo nuevo!")

class Kuchipatchi(Tamagotchi):
    def comer(self):
        super().comer()
        self.salud = self.ajustar_valor(self.salud, +5)
        print("🍔 Kuchipatchi está feliz comiendo! ¡Es tan delicioso! 🍔")

class Weeptchi(Tamagotchi):
    def ignorar(self):
        super().ignorar()
        self.felicidad = self.ajustar_valor(self.felicidad, -5)
        print("😭 Weeptchi llora aún más...💔")

class Milktchi(Tamagotchi):
    def curar(self):
        super().curar()
        self.energia = self.ajustar_valor(self.energia, +10)
        print("⚡ Milktchi se siente mejor!")



