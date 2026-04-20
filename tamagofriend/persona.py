from tamagotchi import Tamagotchi                           # Importa la clase Tamagotchi desde el archivo tamagotchi.py

class Persona:
    def __init__(self, nombre, apellido, tamagotchi):       # Constructor para inicializar la Persona con un nombre, apellido y un Tamagotchi
        self.nombre = nombre                                # El nombre de la Persona
        self.apellido = apellido                            # El apellido de la Persona
        self.tamagotchi = tamagotchi                        # El Tamagotchi asociado a la Persona

    def jugar_con_tamagotchi(self):                                        # Método para jugar con el Tamagotchi, lo que hace que el Tamagotchi juegue y aumente su felicidad pero disminuya su salud y energía
        print(f"{self.nombre} juega con {self.tamagotchi.nombre}!")
        self.tamagotchi.jugar()                                            # Llama al método jugar del Tamagotchi para que juegue y actualice sus atributos de felicidad, salud y energía

    def darle_comida(self):                                                # Método para alimentar al Tamagotchi, lo que hace que el Tamagotchi coma y aumente su salud, felicidad y energía
        print(f"{self.nombre} le da comida a {self.tamagotchi.nombre}!")
        self.tamagotchi.comer()                                            # Llama al método comer del Tamagotchi para que coma y actualice sus atributos de salud, felicidad y energía

    def curarlo(self):                                                     # Método para curar al Tamagotchi, lo que hace que el Tamagotchi sea curado y aumente su salud pero disminuya su felicidad
        print(f"{self.nombre} cura a {self.tamagotchi.nombre}!")
        self.tamagotchi.curar()                                            # Llama al método curar del Tamagotchi para que sea curado y actualice sus atributos de salud y felicidad

    def ignorarlo(self):                                                   # Método para ignorar al Tamagotchi, lo que hace que el Tamagotchi sea ignorado y disminuya su felicidad y energía
        print(f"{self.nombre} ignora a {self.tamagotchi.nombre}")          # Imprime un mensaje indicando que la Persona está ignorando a su Tamagotchi
        self.tamagotchi.ignorar()                                          # Llama al método ignorar del Tamagotchi para que sea ignorado y actualice sus atributos de felicidad y energía 