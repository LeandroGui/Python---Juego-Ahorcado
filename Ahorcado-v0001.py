# Juego del Ahorcado

import random

IMAGENES_AHORCADO = ['''

   +---+
   |   |
       |
       |
       |
       |

=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre toro sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()


def Obtener_palabra_al_azar(listaDePalabras):
    # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.
    indice_De_Palabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indice_De_Palabras]


def mostrar_Tablero(IMAGENES_AHORCADO, letras_Incorrectas, letras_Correctas, palabra_Secreta):
    print(IMAGENES_AHORCADO[len(letras_Incorrectas)])
    print()

    print('Letras incorrectas:', end=' ')
    for letra in letras_Incorrectas:
        print(letra, end=' ')
    print()

    espacios_Vacíos = '_' * len(palabra_Secreta)

    for i in range(len(palabra_Secreta)):  # completar los espacios vacíos con las letras adivinadas
        if palabra_Secreta[i] in letras_Correctas:
            espacios_Vacíos = espacios_Vacíos[:i] + palabra_Secreta[i] + espacios_Vacíos[i + 1:]

    for letra in espacios_Vacíos:  # mostrar la palabra secreta con espacios entre cada letra
        print(letra, end=' ')
    print()


def obtener_Intento(letras_Probadas):
    # Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letras_Probadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return intento


def jugar_De_Nuevo():
    # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')


print("""¦¦+¦¦¦¦+¦¦¦¦¦¦+¦¦¦¦+¦¦¦¦+¦¦¦¦¦¦¦+¦¦¦¦+¦¦¦¦¦¦+¦¦¦¦¦¦+¦¦¦¦+¦¦¦¦+
¦¦¦¦¦¦¦¦¦¦+--¦¦+¦¦¦¦+¦¦¦¦¦¦+----+¦¦¦¦¦+¦¦¦¦¦¦¦¦+--¦¦+¦¦¦¦+¦¦¦¦
¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦+¦¦+¦¦¦¦¦¦¦¦¦¦+¦¦¦+¦¦¦¦+¦¦¦¦¦¦¦¦¦¦¦¦¦+¦¦+¦¦¦
¦¦+--¦¦¦¦¦+--¦¦¦¦¦¦+¦¦¦¦¦¦¦¦¦¦+¦¦+¦¦¦+¦¦++¦¦¦¦¦+--¦¦¦¦¦¦+¦¦¦¦¦
¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦+¦¦¦¦+¦¦¦¦¦¦++¦¦¦¦+-+¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦+¦¦¦¦
+-+¦¦+-++-+¦¦+-++-+¦¦+--+¦+-----+¦+-+¦¦¦¦¦+-++-+¦¦+-++-+¦¦+--+
                    by Leandro Guiñazú""")
letras_Incorrectas = ''
letras_Correctas = ''
palabra_Secreta = Obtener_palabra_al_azar(words)
juego_Terminado = False

while True:
    mostrar_Tablero(IMAGENES_AHORCADO, letras_Incorrectas, letras_Correctas, palabra_Secreta)

    # Permite al jugador escribir una letra.
    intento = obtener_Intento(letras_Incorrectas + letras_Correctas)

    if intento in palabra_Secreta:
        letras_Correctas = letras_Correctas + intento

        # Verifica si el jugador ha ganado.
        encontrado_Todas_Las_Letras = True
        for i in range(len(palabra_Secreta)):
            if palabra_Secreta[i] not in letras_Correctas:
                encontrado_Todas_Las_Letras = False
                break
        if encontrado_Todas_Las_Letras:
            print('¡Sí! ¡La palabra secreta es "' + palabra_Secreta + '"! ¡Has ganado!')
            juego_Terminado = True
    else:
        letras_Incorrectas = letras_Incorrectas + intento

        # Comprobar si el jugador ha agotado sus intentos y ha perdido.
        if len(letras_Incorrectas) == len(IMAGENES_AHORCADO) - 1:
            mostrar_Tablero(IMAGENES_AHORCADO, letras_Incorrectas, letras_Correctas, palabra_Secreta)
            print('¡Te has quedado sin intentos!\nDespués de ' + str(
                len(letras_Incorrectas)) + ' intentos fallidos y ' + str(
                len(letras_Correctas)) + ' aciertos, la palabra era "' + palabra_Secreta + '"')
            juego_Terminado = True

    # Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).
    if juego_Terminado:
        if jugar_De_Nuevo():
            letras_Incorrectas = ''
            letras_Correctas = ''
            juego_Terminado = False
            palabra_Secreta = Obtener_palabra_al_azar(words)
        else:
            break

#proxima actualizacion elegir nivel de dificultad