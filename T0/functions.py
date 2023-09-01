###import###
import os
import menu_handler
import parametros
import random
import tablero_handler
import ranking
# jugador
class Jugador():

    '''
    crea la clase jugador
    '''


    def __init__(self, nombre):
        self.user_name = nombre
        self.user_points = 0
        self.user_tablero = None
        self.show_tablero = None
        self.user_bestias = None
        self.user_casillas = 0
    def save_user_info(self):
        '''

        :return:

        guarda las variables que contiene la clase Jugador
        '''
        save_string = self.user_name + ";;;" + str(self.user_points) + ";;;" \
                      + str(self.user_bestias) + ";;;" + str(self.user_casillas)
        return save_string

    def save_user_tableros(self):
        '''

        :return:

        guarda la informacion de los tableros, crea las lista a un string
        estos seran faciles de volver de nuevo a listas una vez cargados

        estos archivos terminan con ...tablero_save.txt
        '''
        save_string = ""
        for filas in range(0, len(self.user_tablero)):
            for elem in range(0,len(self.user_tablero[0])):
                save_string+= str(self.user_tablero[filas][elem])+","
            save_string = save_string[:len(save_string)-1]
            save_string+= ";"
        save_string = save_string[:len(save_string) - 1] + "\n"

        for filas in range(0, len(self.user_tablero)):
            for elem in range(0,len(self.user_tablero[0])):
                save_string+= str(self.show_tablero[filas][elem])+","
            save_string = save_string[:len(save_string)-1]
            save_string+= ";"
        save_string = save_string[:len(save_string) - 1]

        nombre_archivo = "saved/" + (self.user_name).upper() + "tablero_save.txt"
        open_txt = open(nombre_archivo, "w")
        write_txt = open_txt.write(save_string)
        open_txt.close()

    def win(self):
        '''
        :return: victory

        revisa si el jugador ha ganado, cuando las casillas que le faltan por revelar son las mismas que
        el numero de bestias Nexus
        '''
        victory = False
        vacios = 0

        for filas in self.show_tablero:
            for elem in filas:
                if elem == " ":
                    vacios+= 1
        if vacios == self.user_bestias:
            victory = True

        return victory


    def load_points(self, tablero, puntos, bestias, casillas):
        '''
        :param tablero:
        :param puntos:
        :param bestias:
        :param casillas:
        :return:

        carga la informacion importante del jugador, la carga desde su archivo de txt
        '''
        self.user_points = int(puntos)
        self.user_tablero = tablero
        self.user_bestias = int(bestias)
        self.user_casillas = int(casillas)

    def tablero_para_mostrar(self):
        '''
        con el objetivo de mostrar al usuario un tablero sin las posiciones de los Nexus
        se crea una copia del tablero
        '''
        tablero = []
        filas = []

        for i in range(0, len(self.user_tablero[0])):
            filas.append(" ")

        for i in range(0, len(self.user_tablero)):
            tablero.append(filas[:])

        self.show_tablero = tablero

    def actualizar_tablero(self, posicion):

        self.show_tablero[posicion[0]][posicion[1]] = self.user_tablero[posicion[0]][posicion[1]]

    def actualizar_puntaje(self):

        self.user_points = self.user_bestias * self.user_casillas * parametros.POND_PUNT

###datos numericos
numeros = "3456789101112131415"

###modulo donde se tendran las funciones, "BACKEND" del juego###

def load_game(user):

    '''

    :param user:
    :return:

    recibe el nombre de usuario que busca el jugador para cargar partida, revisa los archivos de la carpeta saved
    para saber si existen datos guardados, si no los hay regresa False, la administracion de esto se delega a
    menu_handler.py cadenas_escenas()
    '''

    save = False

    #hacer if, si existe el guardado cambiar Save por el guardado
    for file in os.listdir("saved"):

        if str(file[:len(file)-4]) == user.upper():
            open_txt = open("saved/"+file, "r")
            lines_txt = (open_txt.readline()).split(";;;")
            open_txt.close()
            save = lines_txt[:]



    return save

def exit_game():
    return True


def change_scene(scene, opcion): #changes menu

    '''

    :param scene:
    :param opcion:
    :return: new_scene

    redirige al modulo "menu_handler.py"
    simplemente por claridad
    '''

    new_scene = menu_handler.cadenas_escenas(scene, opcion)

    return new_scene


def goback_scene(scene):

    '''

    :param scene:
    :return:

    Funcion que busca la escena anterior, simplemente division por claridad
    '''

    before_scene = "main_title.txt"
    if (scene == "load_title.txt") or (scene == "new-game.txt"):
        before_scene = "main_title.txt"

    elif (scene == "fail-load.txt") or (scene == "succes-load.txt"):
        before_scene = "load_title.txt"

    elif (scene == "fail_new_game.txt") or (scene == "succes_newgame.txt"):
        before_scene = "new-game.txt"

    return before_scene


def load_scene(scene, opcion, jugador): #load menu and show it in screen

    '''

    :param scene:
    :param opcion:
    :return:

    "carga" la escena actual, imprime el archivo de texto que representa un menu
    el parametro opcion, es para poder imprimir el nombre del jugador en succes_newgame

    '''

    #check folder titles to load the scene
    escena = "titles/"+scene
    abrir_escena = open(escena, "r")
    lineas_escena = abrir_escena.readlines()
    abrir_escena.close()
    if scene == "succes_newgame.txt":
        lineas_escena[1] = (lineas_escena[1].strip("\n")) + " " + opcion

    if (scene == "end_game.txt") or (scene == "victory.txt"):
        lineas_escena[2] = (lineas_escena[2].strip("\n")) + " " + str(jugador.user_points)

    if scene == "puntajes.txt":
        print(lineas_escena[0])
        print(lineas_escena[1])
        ranking.imprimir_ranks()
        print(lineas_escena[2])
        print(lineas_escena[3])

    else:
        for linea in lineas_escena:
            print(linea)
    pass
#funciones de juego

def valid_medidas(medidas):
    '''

    :param medidas:
    :return: validos

    revisa si las medidas que quiere el jugador para su tablero son validas
    '''
    validos = False
    if "," in medidas:
        medidas = medidas.split(",")
        if len(medidas) == 2:
            if (medidas[0] in numeros) and (medidas[1] in numeros):
                if (3<= int(medidas[0]) <= 15) and (3<= int(medidas[0]) <= 15):
                    validos = [int(medidas[0]), int(medidas[1])]
    return validos



def numero_de_bestias(largo_ancho):
    '''

    :param largo_ancho:
    :return:

    calcula el numero de bestias Nexus
    '''

    n_bestias = int(int(largo_ancho[0]) * int(largo_ancho[1]) * parametros.PROB_BESTIA)

    return n_bestias

def crear_tablero(medidas):
    '''

    :param medidas:
    :return:

    crea el tablero que contiene las bestias Nexus, usa randint
    calcula dos valores random dentro de las medidas del tablero
    y prueba si esta vacia, si lo esta coloca un Nexus, en otro caso busca
    otra posicion
    '''
    #medidas = [largo ,ancho]
    tablero = []
    filas = []

    for i in range(0,int(medidas[1])):
        filas.append(" ")

    for i in range(0, int(medidas[0])):
        tablero.append(filas[:])



    n_bestias = numero_de_bestias(medidas)

    for i in range(0,n_bestias):
        sitio_disponible = False

        while not sitio_disponible:
            posicion = [random.randint(0, medidas[0]-1), random.randint(0, medidas[1]-1)]
            if tablero[posicion[0]][posicion[1]] == " ":
                tablero[posicion[0]][posicion[1]] = "N"
                sitio_disponible = True

    tablero = tablero_handler.nexus_cercanos(tablero)[:]
    return tablero