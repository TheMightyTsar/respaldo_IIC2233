from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
import parametros as p


class balaNormal(QObject):
    destruir_bala = pyqtSignal(dict)
    mover_bala = pyqtSignal(dict)
    cambiar_sprite = pyqtSignal(dict)

    def __init__(self, idBala, x, y):
        super().__init__()
        self.idBala = idBala
        self._x = x
        self.y = y

        # relacionado a la animacion de destruccion
        self.frame = 1
        self.waited = 10
        self.frecuenciaFrames = 10
        self.destruyendo = False
        # relacionado a la animacion de destruccion

        self.velocidad = p.SPEED_PROYECTIL
        self.dano = p.DANO_PROYECTIL


    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, p):
        self._x = p
        if p >= 1500:
            self.destruyendo = True

    def mover(self):
        if not self.destruyendo:
            self.x += self.velocidad
            datos = {}
            datos['x'] = self.x
            datos['y'] = self.y
            datos['id'] = self.idBala
            datos['damage'] = self.dano
            self.mover_bala.emit(datos)

    def animar(self):
        if self.destruyendo:
            if self.waited == self.frecuenciaFrames:
                print(f'frame {self.frame} waited {self.waited}')
                if self.frame == 3:
                    datos = {'id': self.idBala}
                    self.destruir_bala.emit(datos)
                else:
                    datos = {}
                    datos['id'] = self.idBala
                    pixeles = QPixmap(p.BALAS_GUISANTE[self.frame])
                    datos['pixeles'] = pixeles
                    self.cambiar_sprite.emit(datos)
                    self.frame += 1
                    self.waited = 0
            self.waited += 1

    def impacto(self):
        self.destruyendo = True


class balaHielo(QObject):
    destruir_bala = pyqtSignal(dict)
    mover_bala = pyqtSignal(dict)
    cambiar_sprite = pyqtSignal(dict)

    def __init__(self, idBala, x, y):
        super().__init__()
        self.idBala = idBala
        self._x = x
        self.y = y
        # relacionado a la animacion de destruccion
        self.frame = 1
        self.frecuenciaFrames = 10
        self.destruyendo = False
        self.waited = 10
        # relacionado a la animacion de destruccion
        self.velocidad = p.SPEED_PROYECTIL
        self.dano = p.DANO_PROYECTIL
        self.cc = p.RALENTIZAR_ZOMBIE  # se le entregara este parametro al zombie
        # lo que alterara su velocidad

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, p):
        self._x = p
        if p >= 1500:
            self.destruyendo = True

    def mover(self):
        if not self.destruyendo:
            self.x += self.velocidad
            datos = {}
            datos['x'] = self.x
            datos['y'] = self.y
            datos['id'] = self.idBala
            datos['damage'] = self.dano
            datos['cc'] = self.cc
            self.mover_bala.emit(datos)

    def animar(self):
        if self.destruyendo:
            if self.waited == self.frecuenciaFrames:
                if self.frame == 3:
                    datos = {'id': self.idBala}
                    self.destruir_bala.emit(datos)
                else:
                    datos = {}
                    datos['id'] = self.idBala
                    pixeles = QPixmap(p.BALAS_HGUISANTE[self.frame])
                    datos['pixeles'] = pixeles
                    self.cambiar_sprite.emit(datos)
                    self.frame += 1
                    self.waited = 0
            self.waited += 1

    def impacto(self):
        self.destruyendo = True


class balaWidget(QLabel):
    def __init__(self, datos, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.idBala = datos['id']
        self.x = datos['x']
        self.y = datos['y']
        self.setGeometry(self.x, self.y, p.PORTE_BALA, p.PORTE_BALA)
        pixeles = QPixmap(p.BALAS_GUISANTE[0])
        self.setPixmap(pixeles)
        self.raise_()
        self.setScaledContents(True)
        self.setVisible(True)

    def mover(self, datos):
        self.move(datos['x'], datos['y'])

    def cambiarSprite(self, datos):
        self.setPixmap(datos['pixeles'])


class balaHieloWidget(QLabel):
    def __init__(self, datos, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.idBala = datos['id']
        self.x = datos['x']
        self.y = datos['y']
        self.setGeometry(self.x, self.y, p.PORTE_BALA, p.PORTE_BALA)
        pixeles = QPixmap(p.BALAS_HGUISANTE[0])
        self.setPixmap(pixeles)
        self.raise_()
        self.setScaledContents(True)
        self.setVisible(True)

    def mover(self, datos):
        self.move(datos['x'], datos['y'])

    def cambiarSprite(self, datos):
        self.setPixmap(datos['pixeles'])


'''
las plantas siguen una estructura, todas poseen accion
asi en logica podemos ingresarla a un diccionario y llmar la funcion facilmente
sin importar el tipo de planta
'''


class lanzaGuisante(QObject):
    change_sprite = pyqtSignal(dict)
    crear_bala = pyqtSignal(dict)
    destruyeme = pyqtSignal(str)

    def __init__(self, x, y):
        super(lanzaGuisante, self).__init__()
        self.nombre = 'lanzaGuisante'
        self.hp = p.VIDA_PLANTA
        self.frecuencia = p.INTERVALO_DISPARO
        self.waitedFrames = 0
        self.ID = None
        self.x = x
        self.y = y

    def asignarID(self, idPlanta):
        self.ID = idPlanta

    def accion(self):
        if self.waitedFrames < int(self.frecuencia / 3):
            # frame 1

            pass
        elif self.waitedFrames < int(self.frecuencia * 2 / 3):
            # frame 2
            pass

        else:
            # frame 3
            pass

        if self.waitedFrames == self.frecuencia:
            # crea la bala
            datos = {}
            datos['id'] = self.ID
            datos['x'] = p.DATOS_CASILLAS['size'][0] + self.x
            datos['y'] = self.y
            datos['tipo'] = 'normal'
            self.crear_bala.emit(datos)
            self.waitedFrames = 0

        self.waitedFrames += 1

    def recibirDamage(self, dano):
        self.hp -= dano

        if self.hp <= 0:
            self.destruyeme.emit(str(self.ID))


class hieloGuisante(QObject):
    change_sprite = pyqtSignal(dict)
    crear_bala = pyqtSignal(dict)
    destruyeme = pyqtSignal(str)

    def __init__(self, x, y):
        super(hieloGuisante, self).__init__()
        self.nombre = 'hieloGuisante'
        self.hp = p.VIDA_PLANTA
        self.frecuencia = p.INTERVALO_DISPARO
        self.waitedFrames = 0
        self.ID = None
        self.x = x
        self.y = y

    def asignarID(self, idPlanta):
        self.ID = idPlanta

    def accion(self):
        if self.waitedFrames < int(self.frecuencia / 3):
            # frame 1

            pass
        elif self.waitedFrames < int(self.frecuencia * 2 / 3):
            # frame 2
            pass

        else:
            # frame 3
            pass

        if self.waitedFrames == self.frecuencia:
            # crea la bala
            datos = {}
            datos['x'] = p.DATOS_CASILLAS['size'][0] + self.x
            datos['y'] = self.y
            datos['tipo'] = 'hielo'
            self.crear_bala.emit(datos)
            self.waitedFrames = 0

        self.waitedFrames += 1

    def recibirDamage(self, dano):
        self.hp -= dano

        if self.hp <= 0:
            self.destruyeme.emit(str(self.ID))


class papa(QObject):
    change_sprite = pyqtSignal(dict)
    destruyeme = pyqtSignal(str)

    def __init__(self):
        super(papa, self).__init__()
        self.nombre = 'papa'
        self.hp = p.VIDA_PLANTA * 2
        self.ID = None

    def asignarID(self, idPlanta):
        self.ID = idPlanta

    def accion(self):
        self.animar()

    def animar(self):
        datos = {'id': self.ID}
        if self.hp > int(2 * p.VIDA_PLANTA * 0.66):
            ruta = p.PLANTAS[self.nombre][0]
            datos['ruta'] = ruta
            self.change_sprite.emit(datos)
        elif self.hp > int(2 * p.VIDA_PLANTA * 0.33):
            ruta = p.PLANTAS[self.nombre][1]
            datos['ruta'] = ruta
            self.change_sprite.emit(datos)
        elif self.hp > 0:
            ruta = p.PLANTAS[self.nombre][2]
            datos['ruta'] = ruta
            self.change_sprite.emit(datos)

    def recibirDamage(self, dano):
        self.hp -= dano

        if self.hp <= 0:
            self.destruyeme.emit(str(self.ID))
            self.deleteLater()


class girasol(QObject):
    change_sprite = pyqtSignal(dict)
    emit_soles = pyqtSignal(dict)
    destruyeme = pyqtSignal(str)

    def __init__(self):
        super(girasol, self).__init__()
        self.nombre = 'girasol'
        self.hp = p.VIDA_PLANTA
        self.NSoles = p.CANTIDAD_SOLES
        self.FSoles = p.INTERVALO_SOLES_GIRASOL
        self.ticks = 0
        self.ID = None

    def asignarID(self, idPlanta):
        self.ID = idPlanta

    def accion(self):
        '''
        se ejecuta cada tick
        '''
        self.animar()
        self.soltarSoles()

        self.ticks += 1

    def soltarSoles(self):
        if self.ticks == self.FSoles:
            # si se cumple la frecuencia suelta los soles, emite señal que
            # recibira el backend, esta solicitara crear un label en x,y en la ventana
            datos_para_el_sol = {}
            datos_para_el_sol['girasol'] = self.ID
            # la funcion en el frontend creara el sol sobre el girasol si existe ese value
            datos_para_el_sol['valor'] = p.SOLES_POR_RECOLECCION
            for i in range(0, p.CANTIDAD_SOLES):
                print(i)
                self.emit_soles.emit(datos_para_el_sol)
            self.ticks = 0

    def animar(self):
        # cambiar los sprites para que quede guapo
        datos = {'id': self.ID}
        if self.ticks == self.FSoles - 100:  # un segundo que es cuando suelta el sol
            ruta = p.PLANTAS[self.nombre][1]
            datos['ruta'] = ruta
            self.change_sprite.emit(datos)

        if self.ticks == 1:
            ruta = p.PLANTAS[self.nombre][0]
            datos['ruta'] = ruta
            self.change_sprite.emit(datos)

    def recibirDamage(self, dano):
        self.hp -= dano

        if self.hp <= 0:
            self.destruyeme.emit(str(self.ID))


class pala(QObject):
    def __init__(self):
        super().__init__()
        self.nombre = 'pala'
