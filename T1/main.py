# imports
import clases

# codigo que ejecuta el juego

juego = clases.MainGame()

while not juego.terminar_juego:

    juego.imprimir_escena()
    entrada = input("ingrese su opcion: ")
    juego.accion_escena(entrada)

    if juego.reiniciar:
        juego = clases.MainGame()