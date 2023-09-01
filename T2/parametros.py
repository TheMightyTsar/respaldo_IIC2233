import os

# CHECK IN
MIN_CARACTERES: int = 3
MAX_CARACTERES: int = 10


ERROR_INICIO_LARGO = 'El usuario ingresado es muy largo'
ERROR_INICIO_CORTO = 'El usuario que has ingresado es muy corto'
ERROR_INICIO_CARACTERES = 'Has ingresado un caracter no Alfanumerico'

PUNTAJE_ZOMBIE_DIURNO = 1
PUNTAJE_ZOMBIE_NOCTURNO = 2
'''puntaje_extra = puntaje_ronda × ponderador_dificultad'''

PONDERADOR_NOCTURNO = 1
PONDERADOR_DIURNO = 2
DIFICULTAD = {'salidaNocturna': PONDERADOR_NOCTURNO,
              'jardinAbuela': PONDERADOR_DIURNO}
DATOS_JUEGO = {'x': 240,
               'xMax': 1500,
               'y': 0,
               'yMax': 540,
               'ancho': 1260,
               'alto': 540}
SOLES_INICIALES = 100
COSTO_AVANZAR = 500
COSTOS_PLANTAS = {'girasol': 50,
           'lanzaGuisante': 100,
           'hieloGuisante': 150,
           'papa': 75}

'''En caso de disponer dicha cantidad de soles y oprimir
el botón, ganarás automáticamente la ronda sin eliminar a los zombies que faltaba'''

# TIMER, en milisegundos
TIME_BETWEEN_TICKS = 10

# CASILLAS
DATOS_CASILLAS = {'size': [65, 85]}  # [x, y], su posicion se le añadira 67 por cada x, 87 por y



# ZOMBIES
N_ZOMBIES = 12

TIPO_ZOMBIE = ('Hernan', 'Nico')
ALTURA_ZOMBIE = 100
ANCHO_ZOMBIE = 50
X_INICIAL_ZOMBIE = 1400
Y_INICIAL_ZOMBIE = [150, 260]

VIDA_ZOMBIE = 100

VELOCIDAD_ZOMBIE = -1
TIEMPO_CAMINATA = {'Nico': 20,
                   'Hernan': 30}  # Hernan es 1.5 mas rapido que Nico

DANO_MORDIDA = 7
INTERVALO_TIEMPO_MORDIDA = 150

MAX_WF_ZOMBIE_WALK = 100

# RUTAS ZOMBIES
HERNAN_RUNNER_1 = os.path.join(
    'Frontend', 'sprites', 'Zombies', 'Caminando', 'zombieHernanRunner_1.png'
)
HERNAN_RUNNER_2 = os.path.join(
    'Frontend', 'sprites', 'Zombies', 'Caminando', 'zombieHernanRunner_2.png'
)
HERNAN_COMIENDO_1 = os.path.join(
    'Frontend', 'sprites', 'Zombies', 'Comiendo', 'zombieHernanComiendo_1.png'
)
HERNAN_COMIENDO_2 = os.path.join(
    'Frontend', 'sprites', 'Zombies', 'Comiendo', 'zombieHernanComiendo_2.png'
)
HERNAN_COMIENDO_3 = os.path.join(
    'Frontend', 'sprites', 'Zombies', 'Comiendo', 'zombieHernanComiendo_3.png'
)
NICO_WALK_1 = os.path.join(
    'Frontend', 'sprites', 'Zombies', 'Caminando', 'zombieNicoWalker_1.png'
)
NICO_WALK_2 = os.path.join(
    'Frontend', 'sprites', 'Zombies', 'Caminando', 'zombieNicoWalker_2.png'
)
NICO_COMIENDO_1 = os.path.join(
    'Frontend', 'sprites', 'Zombies', 'Comiendo', 'zombieNicoComiendo_1.png'
)
NICO_COMIENDO_2 = os.path.join(
    'Frontend', 'sprites', 'Zombies', 'Comiendo', 'zombieNicoComiendo_2.png'
)
NICO_COMIENDO_3 = os.path.join(
    'Frontend', 'sprites', 'Zombies', 'Comiendo', 'zombieNicoComiendo_3.png'
)

ZOMBIES_SPRITES = {'Hernan': {'caminando': [HERNAN_RUNNER_1, HERNAN_RUNNER_2],
                              'comiendo': [HERNAN_COMIENDO_1,
                                           HERNAN_COMIENDO_2,
                                           HERNAN_COMIENDO_3]},
                   'Nico': {'caminando': [NICO_WALK_1, NICO_WALK_2],
                            'comiendo': [NICO_COMIENDO_1,
                                         NICO_COMIENDO_2,
                                         NICO_COMIENDO_3]}}



# Plantas
VIDA_PLANTA = 50
INTERVALO_DISPARO = 250  # expresado en ticks, 10 milisegundos
PORTE_BALA = 30
DANO_PROYECTIL = 20
RALENTIZAR_ZOMBIE = 0.5  # usa porcentajes para aumentar el numero de ticks para avanzar 0<X<1
INTERVALO_APARICION_SOLES = 1000  # cada cuanto se liberan soles
INTERVALO_SOLES_GIRASOL = 750  # cada cuantos ticks, el girasol suelta soles, 6 sgs
CANTIDAD_SOLES = 2 # cuantos soles libera en los intervalos
CAIDA_SOL = 1
SPEED_PROYECTIL = 2
SOLES_POR_RECOLECCION = 25
VARIACION_P_SOL = [-25, 25]
SIZE_SOL = 50
RUTA_SOL = os.path.join('Frontend', 'sprites', 'Elementos de juego', 'sol.png')
SOLES_EXTRA = 500
ULTIMATE_DAMAGE = 444




# Rutas plantas

GIRASOL_1 = os.path.join(
    'Frontend', 'sprites', 'Plantas', 'girasol_1.png'
)
GIRASOL_2 = os.path.join(
    'Frontend', 'sprites', 'Plantas', 'girasol_2.png'
)

GUISANTE_1 = os.path.join(
    'Frontend', 'sprites', 'Plantas', 'lanzaguisantes_1.png'
)
GUISANTE_2 = os.path.join(
    'Frontend', 'sprites', 'Plantas', 'lanzaguisantes_2.png'
)
GUISANTE_3 = os.path.join(
    'Frontend', 'sprites', 'Plantas', 'lanzaguisantes_3.png'
)

F_GUISANTE_1 = os.path.join(
    'Frontend', 'sprites', 'Plantas', 'lanzaguisantesHielo_1.png'
)
F_GUISANTE_2 = os.path.join(
    'Frontend', 'sprites', 'Plantas', 'lanzaguisantesHielo_2.png'
)
F_GUISANTE_3 = os.path.join(
    'Frontend', 'sprites', 'Plantas', 'lanzaguisantesHielo_3.png'
)

PAPA_1 = os.path.join(
    'Frontend', 'sprites', 'Plantas', 'papa_1.png'
)
PAPA_2 = os.path.join(
    'Frontend', 'sprites', 'Plantas', 'papa_2.png'
)
PAPA_3 = os.path.join(
    'Frontend', 'sprites', 'Plantas', 'papa_3.png'
)


SPRITES_GUISANTE = [GUISANTE_1, GUISANTE_2, GUISANTE_3]
BALAS_GUISANTE = [os.path.join('Frontend', 'sprites', 'Elementos de juego', 'guisante_1.png'),
                  os.path.join('Frontend', 'sprites', 'Elementos de juego', 'guisante_2.png'),
                  os.path.join('Frontend', 'sprites', 'Elementos de juego', 'guisante_3.png')]

BALAS_HGUISANTE = [os.path.join('Frontend', 'sprites', 'Elementos de juego', 'guisanteHielo_1.png'),
                   os.path.join('Frontend', 'sprites', 'Elementos de juego', 'guisanteHielo_2.png'),
                   os.path.join('Frontend', 'sprites', 'Elementos de juego', 'guisanteHielo_3.png')]


RUTA_PALA = os.path.join(
    'Frontend', 'sprites', 'Bonus', 'pala.png'
)

PLANTAS = {'girasol': [GIRASOL_1, GIRASOL_2],
           'lanzaGuisante': [GUISANTE_1, GUISANTE_2, GUISANTE_3],
           'hieloGuisante': [F_GUISANTE_1, F_GUISANTE_2, F_GUISANTE_3],
           'papa': [PAPA_1, PAPA_2, PAPA_3],
           'pala': RUTA_PALA}
# RUTAS FONDO
FONDO_DIA = os.path.join('Frontend', 'sprites', 'Fondos', 'jardinAbuela.png')
FONDO_NOCHE = os.path.join('Frontend', 'sprites', 'Fondos', 'salidaNocturna.png')
# RUTAS UI
RUTA_UI_VENTANA_INICIO = os.path.join(
    'Frontend', 'ui_files', 'ventana_inicio.ui'
)
RUTA_UI_VENTANA_JUEGO = os.path.join(
    'Frontend', 'ui_files', 'ventana_juego.ui'
)
RUTA_UI_VENTANA_POSTRONDA = os.path.join(
    'Frontend', 'ui_files', 'ventana_postronda.ui'
)

RUTA_UI_VENTANA_PRINCIPAL = os.path.join(
    'Frontend', 'ui_files', 'ventana_principal.ui'
)

RUTA_UI_VENTANA_RANKING = os.path.join(
    'Frontend', 'ui_files', 'ventana_ranking.ui'
)

# Ruta Ranking
RUTA_RANKING = os.path.join('puntajes.txt')

