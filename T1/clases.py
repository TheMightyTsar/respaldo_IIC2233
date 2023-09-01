# imports
import parametros
import CSV_extractor
import scene_handler
from programones_clases import Planta, Fuego, Agua
import random
from CSV_extractor import extraer_bayas, extraer_pocion, extraer_caramelos


# codigo

class MainGame:
    '''
    Objeto contenedor de todas las instancias de objetos del juego
    atributos:
    scene indica la escena/menu en la que se encuentra el juego
    jugador instancia de la clase Entrenedor que es el que escogio el jugador
    DCCampeonato contendor de la instancia de la clase Torneo
    reiniciar Booleano: si es True se creara una nueva instancia de MainGame, "reiniciadno" el juego
    Terminar juego, permite salir del ciclo de juego en main.py
    Objeto_a_usar: variable temporal, guarda la instancia de objeto a usar en un programon
    '''

    def __init__(self):

        self.scene = "main_scene.txt"
        self.jugador = None
        self.DCCampeonato = Torneo()
        self.reiniciar = False
        self.terminar_juego = False

        self.objeto_a_usar = None

    def imprimir_escena(self):
        scene_handler.imprimir_la_escena(self)

    def validar_entrada(self, entrada):
        return scene_handler.check_input(self, entrada)

    def accion_escena(self, entrada):
        if entrada == "s":
            self.terminar_juego = True
            print(parametros.DESPEDIDA_PRINT)
        else:
            validez = self.validar_entrada(entrada)

            if validez:

                acciones = scene_handler.accion_en_escena(self, entrada)

                if entrada == "v":
                    self.scene = acciones["game"]
                    self.reiniciar = acciones["reiniciar"]

                else:

                    if self.scene == "main_scene.txt":

                        self.jugador = self.DCCampeonato.restantes[int(entrada)]
                        self.DCCampeonato.nombre_jugador = self.jugador.nombre
                        self.scene = acciones["game"]

                    elif self.scene == "trainer_scene.txt":
                        self.scene = acciones["game"]

                    elif self.scene == "training_scene.txt":
                        self.jugador.energia += -1 * parametros.ENERGIA_ENTRENAMIENTO
                        if (self.jugador.energia - parametros.ENERGIA_ENTRENAMIENTO) >= 0:
                            (self.jugador.programones[int(entrada)]).experiencia += parametros.AUMENTO_DE_EXPERIENCIA

                        self.scene = "trainer_scene.txt"

                    elif self.scene == "use_object.txt":
                        self.objeto_a_usar = self.jugador.objetos.pop(int(entrada))
                        self.scene = "objectUser.txt"

                    elif self.scene == "objectUser.txt":
                        # revisar validez
                        self.jugador.programones[int(entrada)].recibir_objeto(self.objeto_a_usar)
                        self.objeto_a_usar = None
                        self.scene = "trainer_scene.txt"

                    elif self.scene == "choose_figther.txt":
                        for elem in self.DCCampeonato.restantes:
                            if elem.nombre != self.jugador.nombre:
                                elem.escoger_programon()

                            else:
                                elem.combatiente = elem.programones[int(entrada)]
                        print(f"HA COMENZADO LA RONDA {self.DCCampeonato.ronda}")
                        print("------------------------------")
                        perdio = self.DCCampeonato.combate()
                        self.scene = "trainer_scene.txt"
                        if self.DCCampeonato.ronda == 4:
                            self.reiniciar = True
                        elif perdio:
                            self.reiniciar = True

                    elif self.scene == "object_creator.txt":

                        ### VARIABLES RANDOM
                        EXITO = random.random()
                        RANDOM_CARAMELO = extraer_caramelos()[random.randint(0, -1 + len(extraer_caramelos()))]
                        RANDOM_POCION = extraer_pocion()[random.randint(0, -1 + len(extraer_pocion()))]
                        RANDOM_BAYA = extraer_bayas()[random.randint(0, -1 + len(extraer_bayas()))]

                        OBJETO_RANDOM = {"0": RANDOM_BAYA,
                                         "1": RANDOM_POCION,
                                         "2": RANDOM_CARAMELO}

                        if self.jugador.energia >= parametros.OBJETOS[entrada]["energia"]:
                            self.jugador.energia -= parametros.OBJETOS[entrada]["energia"]
                            print(f"*CLINK! CLANK!* creando un/una {parametros.OBJETOS[entrada][parametros.TIPO]}")
                            if EXITO >= parametros.OBJETOS[entrada]["crear"]:

                                self.jugador.objetos.append(Objetos(OBJETO_RANDOM[str(entrada)]))
                                print(f" EXITO EN LA CREACION DE {(self.jugador.objetos[-1]).nombre}")
                                self.scene = "trainer_scene.txt"
                            else:
                                print(f"Oh no el objeto ha explotado!!!  \nhas fallado en crearlo")

                        else:

                            print(f"No tienes energia para crear un/una "
                                  f"{parametros.OBJETOS[entrada][parametros.TIPO]}")


            else:
                print(parametros.ERROR_PRINT)


'''

Clase Torneo, esta clase CONTENDRA informacion de los participantes, quienes siguen y ronda
'''


class Torneo:
    def __init__(self):
        print("!!!se ha inicado el torneo")

        self.particpantes = self.crear_participantes()
        self._ronda = 0
        self.restantes = self.particpantes[:]
        self.perdedores = []
        self.nombre_jugador = None

    def crear_participantes(self):
        lista_entrenadores = CSV_extractor.extraer_entrenadores()
        lista_participantes = []

        for elem in lista_entrenadores:
            lista_participantes.append(Entrenador(elem))

        return lista_participantes

    def combate(self):
        """
        se encarga del combate, toma entrenadores al zara, de los que sigan el torneo,
        y hace que sus combatientes luchen (calculando sus puntajes de victoria)

        """
        duelo = {"0": None,
                 "1": None}
        ganadores = []
        combatientes = []
        terminar_ronda = False
        perdiste = False
        while not terminar_ronda:
            n_restantes = len(self.restantes) - 1

            if len(combatientes) == 2:
                duelo = {"0": combatientes[0].combatiente.combate(combatientes[1].combatiente),
                         "1": combatientes[1].combatiente.combate(combatientes[0].combatiente)}

                print(f"Ha comenzado el combate, "
                      f"el entrenador {combatientes[0].nombre} usa a {combatientes[0].combatiente.nombre}, "
                      f"se enfrenta a {combatientes[1].combatiente.nombre} de {combatientes[1].nombre}")

                if duelo["0"] == duelo["1"]:
                    ganador = random.randint(0, 1)
                    print(f"{combatientes[ganador].nombre} ha ganado el combate!!!")

                    ganadores.append(combatientes.pop(ganador))
                    self.perdedores.append(combatientes.pop())


                elif duelo["0"] > duelo["1"]:
                    print(f"{combatientes[0].nombre} ha ganado el combate!!!")

                    ganadores.append(combatientes.pop(0))
                    self.perdedores.append(combatientes.pop())


                elif duelo["0"] < duelo["1"]:
                    print(f"{combatientes[1].nombre} ha ganado el combate!!!")

                    ganadores.append(combatientes.pop(1))
                    self.perdedores.append(combatientes.pop())

                if n_restantes == -1:

                    terminar_ronda = True
                    self.restantes = ganadores[:]
                    self.ronda += 1

                    if self.ronda != 4:
                        print(f"DIING DIING hemos pasado a la Ronda {self.ronda}")

                    for elem in self.perdedores:
                        if elem.nombre == self.nombre_jugador:
                            perdiste = True
                            print(":( Has perdido, ....REINCIANDO SIMULACION...")



            else:

                if n_restantes == 0:
                    combatientes.append(self.restantes.pop(0))
                else:
                    combatiente = random.randint(0, n_restantes)
                    combatientes.append(self.restantes.pop(combatiente))
        return perdiste

    @property
    def ronda(self):
        return self._ronda

    @ronda.setter
    def ronda(self, value):

        if value == 4:
            self._ronda = value
            print(
                f"Ha terminado el torneo el campeon es .... {self.restantes[0].nombre} \n ....REINCIANDO SIMULACION...")
        else:
            print("aca estamos")
            print(self.restantes)
            for entrenadores in self.restantes:
                if entrenadores.nombre == self.nombre_jugador:
                    entrenadores.energia = parametros.MAX_ENERGIA
                for programon in entrenadores.programones:
                    print("entro al bonus")
                    programon.bonus_tipo()
            self._ronda = value


'''
Clase Entrenador, esta clase CONTENDRA Programones y podra crear objetos de la clase Objetos
'''


class Entrenador:
    def __init__(self, lista: list):

        self.nombre = lista[0]
        self.programones = lista[1].split(";")
        self._energia = int(lista[2])
        self.objetos = lista[3].split(";")
        self.asignar_programones()
        self.asignar_objetos()
        self.combatiente = None

    def asignar_programones(self):
        # ejecutar tras iniciar el objeto, deja los programones del jugador con la info importante

        info_programones = CSV_extractor.extraer_programones()
        programones_entrenador = []

        # ciclo de los programones del entrenador
        for programon in self.programones:
            for elem in info_programones:
                if programon == elem[0]:
                    if elem[1] == "fuego":
                        programones_entrenador.append(Fuego(elem, self.nombre))
                    if elem[1] == "agua":
                        programones_entrenador.append(Agua(elem, self.nombre))
                    if elem[1] == "planta":
                        programones_entrenador.append(Planta(elem, self.nombre))

        self.programones = programones_entrenador[:]

    def asignar_objetos(self):
        # ejecutar tras iniciar el objeto, deja los objetos del jugador con la info importante

        info_objetos = CSV_extractor.extraer_objetos()
        objetos_entrenador = []

        for objeto in self.objetos:
            for elem in info_objetos:

                if objeto == elem[0]:
                    objetos_entrenador.append(Objetos(elem))

        self.objetos = objetos_entrenador[:]

    def escoger_programon(self):
        cantidad = len(self.programones) - 1
        if cantidad != 0:
            numero = random.randint(0, cantidad)
            self.combatiente = self.programones[numero]
        else:
            self.combatiente = self.programones[0]
        pass

    #  hacer property energia

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, value):

        if value < 0:
            self._energia = self._energia

            print("No tienes energia suficiente :(")
        elif value < self._energia:
            print(f"FIUF has gastado {self._energia - value} de energia...")

            self._energia = value

        if value == parametros.MAX_ENERGIA:
            self._energia = value
            print("...Tras el combate has recuperado tus fuerzas")


'''
Clase Objetos, podran buffear a los programones
'''


class Objetos:
    def __init__(self, lista):
        self.nombre = lista[0]
        self.tipo = lista[1]
        self.bonusHP = 0
        # baya y caramelo
        self.bonusAD = 0
        # pocion y caramelo
        self.bonusDEF = 0
        # caramelo
        self.asignar_bonus()

    def asignar_bonus(self):
        if (self.tipo == "baya") or (self.tipo == "caramelo"):
            self.bonusHP = parametros.BUFF_VIDA

        if (self.tipo == "pocion") or (self.tipo == "caramelo"):
            self.bonusAD = parametros.BUFF_ATAQUE

        if self.tipo == "caramelo":
            self.bonusDEF = parametros.AUMENTO_DEFENSA
