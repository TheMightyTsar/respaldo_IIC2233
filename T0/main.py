#imports
import functions
import tablero
import tablero_handler
import ranking
#variables

scene = "main_title.txt" #string indica que menu tenemos abierto

exit_game = False

opcion = ""

jugador = None

medidas = None

#codigo principal

def save_game():
    '''

    :return:

    Crea archivos de texto en las carpetas correspondientes para guardar los datos de los jugadores
    '''

    nombre_archivo = "saved/" + (jugador.user_name).upper() + ".txt"

    guardado_usuario = jugador.save_user_info()

    abrir_archv_txt = open(nombre_archivo, "w")

    escribir_datos_player = abrir_archv_txt.write(guardado_usuario)

    abrir_archv_txt.close()

    ####guardar tablero

    jugador.save_user_tableros()



    ###guardar tablero

    print("")
    print("---juego guardado---")
    print("")


    pass


while exit_game == False:
    '''
    inicia ciclo de juego, termina cuando se escoge la opcion salir
    '''

    functions.load_scene(scene, opcion, jugador)

    if scene == "succes_newgame.txt":
        jugador = functions.Jugador(opcion)

    opcion = input("ingresa tu opcion: \n")


    if opcion == "s":

        exit_game = functions.exit_game()


    elif opcion == "v":

        scene = functions.goback_scene(scene)


    elif scene == "succes_newgame.txt":

        valid_medidas = functions.valid_medidas(opcion)

        if valid_medidas != False:
            jugador.user_tablero = functions.crear_tablero(valid_medidas)
            jugador.user_bestias = functions.numero_de_bestias(valid_medidas)
            jugador.tablero_para_mostrar()
            tablero.print_tablero_con_utf8(jugador.show_tablero)



            scene = "game_title.txt"


    elif scene == "load_title.txt":

        guardado = functions.load_game(opcion)

        if guardado == False:

            scene = "fail-load.txt"

        else:

            jugador = functions.Jugador(guardado[0])
            # loadear tablero
            tableros = None

            jugador.load_points(tableros, int(guardado[1]), int(guardado[2]), int(guardado[3]))

            tableros = tablero_handler.load_tablero(jugador.user_name)
            jugador.user_tablero = tableros[0]
            jugador.show_tablero = tableros[1]

            if jugador.win():
                jugador.actualizar_puntaje()
                save_game()
                ranking.actualizar_rank(jugador)
                tablero.print_tablero_con_utf8(jugador.user_tablero)
                scene = "victory.txt"


            else:
                scene = "game_title.txt"
                tablero.print_tablero_con_utf8(jugador.show_tablero)



    elif scene == "game_title.txt":



        if opcion == "1":
            save_game()
            ranking.actualizar_rank(jugador)
            tablero.print_tablero_con_utf8(jugador.show_tablero)
        elif opcion == "2":
            save_game()
            ranking.actualizar_rank(jugador)
            exit_game = True
        else:
            posicion = tablero_handler.valid_posicion(opcion, jugador.show_tablero)
            if posicion != False:
                jugador.actualizar_tablero(posicion)
                jugador.user_casillas += 1
                tablero.print_tablero_con_utf8(jugador.show_tablero)
                jugador.actualizar_puntaje()


                if jugador.user_tablero[posicion[0]][posicion[1]] == "N":
                    jugador.user_casillas -= 1
                    jugador.actualizar_puntaje()
                    save_game()
                    ranking.actualizar_rank(jugador)
                    scene = "end_game.txt"
                elif jugador.win():
                    jugador.actualizar_puntaje()
                    save_game()
                    ranking.actualizar_rank(jugador)
                    tablero.print_tablero_con_utf8(jugador.user_tablero)
                    scene = "victory.txt"
            else:
                tablero.print_tablero_con_utf8(jugador.show_tablero)


    else:

        scene = functions.change_scene(scene, opcion)

    #close the code


print("\n ...Adios Prograwan... ")  #despedida y cierre del juego
print("Que Pyhton te acompañe")




