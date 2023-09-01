import functions
import os
import ranking

def cadenas_escenas(escena, opcion):

    '''
    :param escena -> string
    :param opcion: -> string
    :return: nueva_escena -> string

    esta función revisa en que escena se encuentra el juego y la opcion/respuesta
    ingresada por el usuario, ocupa estos datos para definir la siguiente escena
    '''



    nueva_escena = "main_title.txt"
    #escenas iniciales
    if escena == "main_title.txt":

        if opcion == "1":
            nueva_escena = "new-game.txt"

        elif opcion == "2":
            nueva_escena = "load_title.txt"

        elif opcion == "3":
            ranking.ordenar_rank()
            nueva_escena = "puntajes.txt"

    elif escena == "new-game.txt":
        valid = True
        for file in os.listdir("saved"):

            if str(file[:len(file) - 4]).upper() == opcion.upper():
                nueva_escena = "fail_new_game.txt"
                valid = False

        if ("tablero_save" in opcion) or (".txt" in opcion) or (";;;" in opcion) or ("/" in opcion):
            nueva_escena = "fail_new_game.txt"
        ###añadir caso que ya hay jugador con ese nombre

        elif valid:

            nueva_escena = "succes_newgame.txt"

    elif escena == "load_title.txt":
        guardado = functions.load_game(opcion)
        if guardado == False:
            nueva_escena = "fail-load.txt"



    return nueva_escena
