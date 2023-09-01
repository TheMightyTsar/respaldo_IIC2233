# imports
import random as R

"""
Codigo del cual importaremos todas las variables "constantes" de la Tarea
"""
# PATHS

PATH = "escenas/"

# entrenamiento
MIN_AUMENTO_EXPERIENCIA: int = 1000
MAX_AUMENTO_EXPERIENCIA: int = 1100
AUMENTO_DE_EXPERIENCIA: int = R.randint(MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA)
ENERGIA_ENTRENAMIENTO: int = 12
MAX_ENERGIA = 100
# informacion objetos

# subir de level, valores entre los que aumentara el los atributos de Vida, Ataque,
# Defensa y Velocidad
MIN_AUMENTO_ENTRENAMIENTO: int = 12
MAX_AUMENTO_ENTRENAMIENTO: int = 23
AUMENTO_ENTRENAMIENTO: int = R.randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
# tope de estadisticas
MAX_LVL: int = 100
MAX_EXP: int = 100
MAX_VIDA: int = 255
MAX_ATAQUE: int = 190
MAX_DEFENSA: int = 250
MAX_VELOCIDAD: int = 200

# beneficios de Tipo de programon
AUMENTAR_VIDA_PLANTA: int = 10
AUMENTAR_ATAQUE_FUEGO: int = 10
AUMENTAR_VELOCIDAD_AGUA: int = 10

COMBATE_FUEGO = {"fuego": 0,
                 "planta": 1,
                 "agua": -1}

COMBATE_AGUA = {"fuego": 1,
                 "planta": -1,
                 "agua": 0}

COMBATE_PLANTA = {"fuego": -1,
                 "planta": 0,
                 "agua": 1}
COMBATE_TIPOS = {"fuego": COMBATE_FUEGO,
                 "planta": COMBATE_PLANTA,
                 "agua": COMBATE_AGUA}

# objetos
BUFF_VIDA = R.randint(1, 10)
BUFF_ATAQUE = R.randint(1, 7)
AUMENTO_DEFENSA = 17
GASTO_ENERGIA_BAYA = 13
GASTO_ENERGIA_POCION = 12
GASTO_ENERGIA_CARAMELO = 27
PROB_EXITO_BAYA = 0.67
PROB_EXITO_POCION = 0.63
PROB_EXITO_CARAMELO = 0.22

BAYA = {"crear": PROB_EXITO_BAYA,
        "energia": GASTO_ENERGIA_BAYA,
        "tipo": "baya"}
POCION = {"crear": PROB_EXITO_POCION,
          "energia": PROB_EXITO_POCION,
          "tipo": "pocion"}
CARAMELO = {"crear": PROB_EXITO_CARAMELO,
            "energia": GASTO_ENERGIA_CARAMELO,
            "tipo": "caramelo"}
OBJETOS = {"0": BAYA,
           "1": POCION,
           "2": CARAMELO}


# diccionario escenas
TRAINER_SCENE = {"1": "training_scene.txt",
                 "2": "choose_figther.txt",
                 "3": "resumen_ronda.txt",
                 "4": "object_creator.txt",
                 "5": "use_object.txt",
                 "6": "trainer_status.txt",
                 "v": "main_scene.txt"}

# check in variables
TIPO = "tipo"

ABECEDARIO = "ABCDEFGHIJKMNOPQ"

ESCENAS_VOLVER = ["trainer_status.txt", "use_object.txt", "object_creator.txt", "choose_figther.txt",
                  "training_scene.txt", "resumen_ronda.txt", "fight_resumen.txt"]

NUMBER_LEN1 = "0123456789"

NUMBER_LEN2 = ["10", "12", "13", "14", "15"]

OPCIONES_ENTRENADOR = "123456"

OBJETOS_CREABLES = "012"



# print out
DESPEDIDA_PRINT = "beep ... beep .. beep . bep \n Se ha finalizado la simulacion del DCCampeonato"
ERROR_PRINT = " ................\n ... ENTRADA ERRONEA... \n ................"