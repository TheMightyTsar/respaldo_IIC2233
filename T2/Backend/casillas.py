'''
las casillas seran un objeto propio que heredaran de Qlabel, asi puedo personalizarlas
Su posicion y tamaño se hizo a mano revisando los resultados en QTDesigner
Quedo cierto espacio, 2 pixeles aprox, entre casillas por lo que a veces el zombie no comera aunque
parezca que esten en la misma casilla, esto es para evitar que un zombie coma dos plantas a la vez
Las casillas sirven como el "Frontend" de las plantas
'''
from PyQt5.QtWidgets import QLabel
import parametros as p
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, QObject


class casilla(QLabel):
    plantar_plantita = pyqtSignal(dict)
    quitar_planta = pyqtSignal(str)
    ocupacion_casilla = pyqtSignal(dict)

    def __init__(self, posicion_x, posicion_y, ID, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ancho = p.DATOS_CASILLAS['size'][0]
        self.alto = p.DATOS_CASILLAS['size'][1]

        self.setGeometry(posicion_x, posicion_y, self.ancho, self.alto)
        self.ID = ID  # nombre de la casilla

        self.ocupada = False
        self.namePlanta = None  # contendra la logica de la planta, esta conectada a casilla
        # que dara señales visuales

        self.setVisible(True)

        '''
        pixeles = QPixmap(p.GIRASOL_1)
        self.setPixmap(pixeles)
        self.setScaledContents(True)
        '''

    def asignarPlanta(self, plantita):
        self.namePlanta = plantita
        self.ocupada = True
        datos = {'id': self.ID,
                 'planta': self.namePlanta}
        self.plantar_plantita.emit(datos)
        self.iniciarSprite()

    def checkMouseSobreCasilla(self, xMouse, yMouse):
        if xMouse >= self.x() + self.ancho:
            return False
        if xMouse <= self.x():
            return False
        if yMouse >= self.y() + self.alto:
            return False
        if yMouse <= self.y():
            return False
        return True

    def quitarPlanta(self):

        self.namePlanta = None
        self.ocupada = False
        self.vaciarSprite()


    def cambiarSprite(self, sprite):
        # conecta con una señal de plantas.py en ventanaJuego
        pixeles = QPixmap(sprite)
        self.setPixmap(pixeles)
        self.setScaledContents(True)

    def vaciarSprite(self):
        pixeles = QPixmap()
        self.setPixmap(pixeles)

    def iniciarSprite(self):
        pixeles = QPixmap(p.PLANTAS[self.namePlanta][0])
        self.setPixmap(pixeles)
        self.setScaledContents(True)

    def ocupadaCasilla(self):
        respuesta = {}
        respuesta['idCasilla'] = self.ID
        respuesta['ocupada'] = self.ocupada
        self.ocupacion_casilla.emit(respuesta)

'''class cerebroCasilla(QObject):
    ocupacion_casilla = pyqtSignal(dict)
    def __init__(self, idCasilla):
        super(cerebroCasilla, self).__init__()
        self.ID = idCasilla
        self.ocupada = False
        
    def ocupadaCasilla(self):
        respuesta = {}
        respuesta['idCasilla'] = self.ID
        respuesta['ocupada'] = self.ocupada
        self.ocupacion_casilla.emit(respuesta)'''


