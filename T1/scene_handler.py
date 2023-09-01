# imports
import CSV_extractor

# codigo
import parametros


def imprimir_la_escena(jugador):
    txt_imprimir = ""
    path = parametros.PATH + jugador.scene
    open_txt = open(path, "r", encoding="utf-8")

    if jugador.scene == "main_scene.txt":
        # elementos iniciales
        lista_jugadores = CSV_extractor.extraer_entrenadores()

        # armar el txt
        txt_imprimir += open_txt.readline() + open_txt.readline() + open_txt.readline()
        i = 0
        for elem in lista_jugadores:
            txt_imprimir += f"[{str(i)}] {elem[0]}: {elem[1]} \n"
            i += 1
        txt_imprimir += "[s] Salir"

    elif jugador.scene == "trainer_scene.txt":

        lineas_txt = open_txt.readlines()
        i = 0
        for elem in lineas_txt:
            if i == 2:
                txt_imprimir += f"**{jugador.jugador.nombre}**\n"
            txt_imprimir += elem
            i += 1

    elif jugador.scene == "training_scene.txt":
        # armar el txt
        txt_imprimir += open_txt.readline() + open_txt.readline()

        i = 0
        for elem in jugador.jugador.programones:
            txt_imprimir += f"[{str(i)}] {elem.nombre} \n"
            i += 1
        txt_imprimir += open_txt.readline() + open_txt.readline()

    elif jugador.scene == "choose_figther.txt":
        open_txt = open(path, "r", encoding="utf-8")
        txt_imprimir = ""

        # armar el txt
        txt_imprimir += open_txt.readline() + open_txt.readline()
        i = 0
        for elem in jugador.jugador.programones:
            txt_imprimir += f"[{str(i)}] {elem.nombre} \n"
            i += 1
        txt_imprimir += open_txt.readline() + open_txt.readline()

    elif jugador.scene == "object_creator.txt":
        lineas_txt = open_txt.readlines()
        for elem in lineas_txt:
            txt_imprimir += elem

    elif jugador.scene == "use_object.txt":
        txt_imprimir = open_txt.readline() + open_txt.readline()
        i = 0
        for elem in jugador.jugador.objetos:
            txt_imprimir += f"[{i}] {elem.nombre} \n"
            i += 1
        txt_imprimir += "\n" + open_txt.readline() + open_txt.readline()

    elif jugador.scene == "trainer_status.txt":
        txt_imprimir = open_txt.readline() + open_txt.readline() + f"* ***{jugador.jugador.nombre}*** *\n" \
                                                                   f"Energia: {jugador.jugador.energia} \n" \
                                                                   f"Objetos: "
        for elem in jugador.jugador.objetos:
            txt_imprimir += f" {elem.nombre},"
        txt_imprimir = txt_imprimir[:len(txt_imprimir) - 1] + "\n"
        txt_imprimir += open_txt.readline() + open_txt.readline() + open_txt.readline() + \
                        open_txt.readline() + open_txt.readline()
        for elem in jugador.jugador.programones:
            txt_imprimir += f" {elem.nombre}  |  {elem.tipo}  |  {elem._nivel}  |  {elem._vida} \n"
        txt_imprimir += open_txt.readline() + open_txt.readline()

    elif jugador.scene == "resumen_ronda.txt":

        txt_imprimir = open_txt.readline() + open_txt.readline() + f"Participantes:"
        for elem in jugador.DCCampeonato.particpantes:
            txt_imprimir += f" {elem.nombre},"
        txt_imprimir = txt_imprimir[:len(txt_imprimir) - 1] + "\n"
        txt_imprimir += f"Ronda: {jugador.DCCampeonato._ronda} \n Siguen en la competencia: "
        for elem in jugador.DCCampeonato.restantes:
            txt_imprimir += f" {elem.nombre},"
        txt_imprimir = txt_imprimir[:len(txt_imprimir) - 1] + "\n"
        txt_imprimir += open_txt.readline() + open_txt.readline()

    elif jugador.scene == "objectUser.txt":
        # armar el txt
        txt_imprimir += open_txt.readline() + open_txt.readline()

        i = 0
        for elem in jugador.jugador.programones:
            txt_imprimir += f"[{str(i)}] {elem.nombre} \n"
            i += 1
        txt_imprimir += open_txt.readline()

    open_txt.close()
    print(txt_imprimir)


def check_input(game, entrada):
    """

    este metodo revisa si lo ingresado por el usuario es valido segun la game
    donde nos encontremos

    :param game:
    :param entrada:
    :return: valid: Bool

    """
    valid = False
    if (entrada == "v") and ((game.scene in parametros.ESCENAS_VOLVER) or (game.scene == "trainer_scene.txt")):
        valid = True

    elif game.scene == "main_scene.txt":
        if len(entrada) == 1:
            if entrada in parametros.NUMBER_LEN1:
                valid = True
        elif len(entrada) == 2:
            for elem in parametros.NUMBER_LEN2:
                if entrada == elem:
                    valid = True

    if game.scene == "trainer_scene.txt":
        if entrada in parametros.OPCIONES_ENTRENADOR:
            valid = True
        else:
            valid = False

    elif (game.scene == "training_scene.txt") or (game.scene == "objectUser.txt") or (game.scene == "choose_figther.txt"):
        cantidad_programones = len(game.jugador.programones) - 1
        if len(entrada) == 1:
            if entrada in parametros.NUMBER_LEN1:
                if (0 <= int(entrada) <= cantidad_programones):
                    valid = True
    elif game.scene == "use_object.txt":
        cantidad_objetos = len(game.jugador.objetos) - 1
        numero = True
        for elem in str(entrada):
            if elem not in parametros.NUMBER_LEN1:
                numero = False
        if numero:
            if (0 <= int(entrada) <= cantidad_objetos):
                valid = True
    elif game.scene == "object_creator.txt":
        if len(str(entrada)) == 1:
            if str(entrada) in parametros.OBJETOS_CREABLES:
                valid = True

    return valid


def accion_en_escena(juego, entrada):
    retornar = {"game": None,
                "reiniciar": False
                }

    if (entrada == "v") and (juego.scene in parametros.ESCENAS_VOLVER):
        retornar["game"] = "trainer_scene.txt"

    if juego.scene == "main_scene.txt":
        retornar["game"] = "trainer_scene.txt"

    elif juego.scene == "trainer_scene.txt":
        retornar["game"] = parametros.TRAINER_SCENE[str(entrada)]
        if retornar["game"] == "main_scene.txt":
            retornar["reiniciar"] = True

    return retornar
