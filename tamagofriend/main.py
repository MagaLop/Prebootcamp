from tamagotchi import Mametchi                 # Importa la clase Mametchi desde el archivo tamagotchi.py, que es una subclase de Tamagotchi con características específicas.
from persona import Persona

tama = Mametchi("Mame", "Amarillo")             # Crea una instancia de Mametchi con el nombre "Mame" y el color "Amarillo". Esta instancia representa a un Tamagotchi específico con sus propios atributos y comportamientos.
persona = Persona("Juan", "Perez", tama)        # Crea una instancia de Persona con el nombre "Juan", apellido "Perez" y asigna la instancia de Mametchi creada anteriormente al atributo tamagotchi de la Persona. Esto establece una relación entre la Persona y su Tamagotchi, permitiendo que la Persona interactúe con su Tamagotchi a través de los métodos definidos en la clase Persona.

persona.darle_comida()                          # Llama al método darle_comida() de la instancia de Persona, lo que hace que la Persona alimente a su Tamagotchi (Mame), incrementando su salud, felicidad y energía.
persona.curarlo()                               # Llama al método curarlo() de la instancia de Persona, lo que hace que la Persona cure a su Tamagotchi (Mame), incrementando su salud pero disminuyendo su felicidad.
persona.jugar_con_tamagotchi()                  # Llama al método jugar_con_tamagotchi() de la instancia de Persona, lo que hace que la Persona juegue con su Tamagotchi (Mame), incrementando su felicidad pero disminuyendo su salud y energía.

print("\nEstado final:")                        # Imprime un mensaje indicando que se mostrará el estado final del Tamagotchi después de las interacciones realizadas por la Persona.
tama.mostrar_estado()                           # Llama al método mostrar_estado() de la instancia de Mametchi (Mame) para mostrar su estado actual, incluyendo su salud, felicidad y energía después de las interacciones realizadas por la Persona.