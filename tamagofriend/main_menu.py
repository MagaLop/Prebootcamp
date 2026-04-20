from tamagotchi import Mametchi, Kuchipatchi, Weeptchi, Milktchi
from persona import Persona

print("🐣 Bienvenida a Tamagotchi 🐣")

# Elegir personaje
print("Elige tu personaje:")
print("1. Mametchi ✨")
print("2. Kuchipatchi 🍔")
print("3. Weeptchi 🥰")
print("4. Milktchi 🍼")

opcion = input("Ingresa tu elección: ")

# Crear el Tamagotchi basado en la elección del usuario, asignando el nombre y color correspondientes a cada personaje. Si la opción ingresada no es válida, se asigna por defecto a Mametchi.
if opcion == "1":
    tama = Mametchi("Mame", "Amarillo")
elif opcion == "2":
    tama = Kuchipatchi("Kuchi", "Verde")
elif opcion == "3":
    tama = Weeptchi("Weepie", "Azul")
elif opcion == "4":
    tama = Milktchi("Milky", "Blanco")
else:
    print("Opción inválida, se asigna Mametchi 🐣")
    tama = Mametchi("Mame", "Amarillo")

persona = Persona("Sofía", "López", tama)

# Estado inicial
tama.mostrar_estado()

#  Loop del juego, donde se muestra un menú de opciones para que el usuario pueda interactuar con su Tamagotchi. El usuario puede elegir jugar, alimentar, curar, ignorar, ver el estado o salir del juego. El loop continúa hasta que el usuario decide salir.
while True:
    print("\n¿Qué quieres hacer?")                          # \n se utiliza para agregar una nueva línea antes de mostrar el menú de opciones, mejorando la legibilidad del texto en la consola.
    print("1. Jugar 🎮")
    print("2. Comer 🍎")
    print("3. Curar 💊")
    print("4. Ignorar 😢")
    print("5. Ver estado 📊")
    print("6. Salir ❌")

    accion = input("Elige una opción: ")

# Dependiendo de la opción elegida por el usuario, se llama al método correspondiente de la clase Persona para interactuar con el Tamagotchi. Si la opción es inválida, se muestra un mensaje de advertencia. El loop se repetirá hasta que el usuario elija salir (opción 6).
    if accion == "1":
        persona.jugar_con_tamagotchi()
    elif accion == "2":
        persona.darle_comida()
    elif accion == "3":
        persona.curarlo()
    elif accion == "4":
        persona.ignorarlo()
    elif accion == "5":
        tama.mostrar_estado()
    elif accion == "6":
        print("👋 ¡Adiós!")
        break
    else:
        print("⚠️ Opción inválida")