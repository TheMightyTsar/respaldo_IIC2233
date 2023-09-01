import parametros as p
from threading import Lock
from PyQt5.QtCore import QObject, pyqtSignal
from random import choice
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap


def get_tipo_zombie():
    tipo = choice(p.TIPO_ZOMBIE)

    return tipo


def get_y():
    y = choice(p.Y_INICIAL_ZOMBIE)
    return y


class Zombie(QObject):
    # se ha acabado el juego ha perdido el jugador
    derrota = pyqtSignal(str)
    # creara el widget del zombie respectivo para que se vea en pantalla
    crear_zombie = pyqtSignal(dict)
    # entrega el nuevo X del zombie
    caminado = pyqtSignal(int, int)
    conectar_con_casilla = pyqtSignal(dict)
    # entrega el daño infligido a la planta y a que casilla
    mordisco = pyqtSignal(dict)
    # señal enviada para ver si hay una planta en esa casilla
    puedo_comerte = pyqtSignal(int, int)
    # entrega el sprite nuevo del zombie
    enviar_sprite = pyqtSignal(list)
    eliminar_zombie = pyqtSignal(dict)

    def __init__(self, id):
        super().__init__()
        self._x = p.X_INICIAL_ZOMBIE
        self.y = get_y()
        self.ID = id
        self.tipo = get_tipo_zombie()
        self.lockHP = Lock()
        self.HP: int = p.VIDA_ZOMBIE
        self.speed: int = p.VELOCIDAD_ZOMBIE
        self.damage: int = p.DANO_MORDIDA
        self.frecuenciaMordida = p.INTERVALO_TIEMPO_MORDIDA
        self.cc = 1  # realentizacion entre 0 y 1

        # este sera el valor Y que pasara por la casilla
        self.linea = int(self.y - (p.ALTURA_ZOMBIE / 3))
        # 116 es la primera fila
        # 226 la segunda

        self.queHago = 'caminar'
        self.casillaAtacada = None
        self.comiendo = False

        self.sprites: dict = p.ZOMBIES_SPRITES[self.tipo]
        # waitedFrames guardara cuantos ticks han pasado, para ver cambios de sprite
        self.waitedFrames = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, p):
        self._x = p
        if p <= 400:
            self._x = 400
            self.derrota.emit('derrota')

    # elementos para conexiones

    def solicitarCreacionZombie(self):
        datos = {'tipo': self.tipo,
                 'pos': [self.x, self.y],
                 'ID': self.ID}
        self.crear_zombie.emit(datos)

    # gameplay

    def cambiarAccionZombie(self, ocupacionCasilla):
        if not ocupacionCasilla and self.comiendo:
            self.comiendo = False
            self.queHago = 'caminar'
            self.waitedFrames = 0

        elif ocupacionCasilla and not self.comiendo:
            self.comiendo = True
            self.queHago = 'comer'
            self.waitedFrames = 0

    def accion(self):
        '''
        esta funcion se ejecuta por cada tick, el zombie o camina o come
        '''

        if self.queHago == 'caminar':
            self.caminar()
        if self.queHago == 'comer':
            self.comer()
        self.waitedFrames += 1
        pass

    def caminar(self):
        '''
        cambia self.x del zombie, manda una señal para que su respectivo ZombieWidget haga lo mismo
        WaitedFrames, son los intervalos entre los que cambia su sprite y su accion
        solo en cierto Sprite caminan
        '''
        if self.waitedFrames == p.MAX_WF_ZOMBIE_WALK - p.TIEMPO_CAMINATA[self.tipo]:
            spriteEnviar = [self.ID, self.sprites['caminando'][1]]
            self.enviar_sprite.emit(spriteEnviar)

        if self.waitedFrames > p.MAX_WF_ZOMBIE_WALK - (p.TIEMPO_CAMINATA[self.tipo]*self.cc):
            datosParaCasilla = {}
            datosParaCasilla['ID'] = self.ID
            datosParaCasilla['linea'] = self.linea

            self.x += self.speed
            self.caminado.emit(self.ID, self.x)
            datosParaCasilla['x'] = self.x
            self.conectar_con_casilla.emit(datosParaCasilla)

        if self.waitedFrames == p.MAX_WF_ZOMBIE_WALK:
            self.waitedFrames = 0
            spriteEnviar = [self.ID, self.sprites['caminando'][0]]
            self.enviar_sprite.emit(spriteEnviar)

    def comer(self):
        if self.waitedFrames == 1:
            spriteEnviar = [self.ID, self.sprites['comiendo'][0]]
            self.enviar_sprite.emit(spriteEnviar)

        if self.waitedFrames == self.frecuenciaMordida/3:
            spriteEnviar = [self.ID, self.sprites['comiendo'][1]]
            self.enviar_sprite.emit(spriteEnviar)

        if self.waitedFrames == ((2*self.frecuenciaMordida) / 3):
            spriteEnviar = [self.ID, self.sprites['comiendo'][2]]
            self.enviar_sprite.emit(spriteEnviar)


        if self.waitedFrames == self.frecuenciaMordida:
            self.waitedFrames = 0
            datos = {}
            datos['idCasilla'] = self.casillaAtacada
            datos['dano'] = self.damage
            self.mordisco.emit(datos)

    def recibirDano(self, datos):

        damage = datos['damage']
        if 'cc' in datos:
            self.cc = datos['cc']
        with self.lockHP:
            self.HP -= damage
        if self.HP < 0:
            datos = {'id': self.ID}
            datos['casilla'] = self.casillaAtacada
            self.eliminar_zombie.emit(datos)
            self.deleteLater()


class ZombieWidget(QLabel):
    def __init__(self, datos, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ID = datos['ID']
        self.tipo = datos['tipo']

        self.posicion = datos['pos']
        self.setGeometry(self.posicion[0], self.posicion[1], p.ANCHO_ZOMBIE, p.ALTURA_ZOMBIE)

        self.setScaledContents(True)

        self.setVisible(True)

    def caminar(self, caminado):
        self.move(caminado, self.posicion[1])

    def cambiarSprite(self, Sprite):
        print('cambiar sprite')
        direct = Sprite[0]
        pixeles = QPixmap(direct)
        self.setPixmap(pixeles)
        self.setScaledContents(True)
