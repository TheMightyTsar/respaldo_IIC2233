'''
Este modulo contiene un objeto que hereda de Qlabel.
Seguira al mouse, asi que en caso de que se quiera poner una planta, paresca que se esta
arrastrando hasta la casilla
Cuando se presionen los botones para comprar plantas se hace visible, cuando
se suelte el click del mouse se hace invisible
'''
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
import parametros as p
from PyQt5.QtCore import pyqtSignal


class MouseFollower(QLabel):
    soltar_planta = pyqtSignal(dict)

    def __init__(self, planta, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.plantaEscogida = planta # str

        self.raise_()
        self.sprites = p.PLANTAS[self.plantaEscogida]
        self.setGeometry(-100, -100, p.DATOS_CASILLAS['size'][0],
                         p.DATOS_CASILLAS['size'][1])
        if self.plantaEscogida == 'pala':
            pixeles = QPixmap(self.sprites)
        else:
            pixeles = QPixmap(self.sprites[0])
        self.setPixmap(pixeles)
        self.setScaledContents(True)
        self.setVisible(True)

    def soltarPlanta(self):

        self.soltar_planta.emit()
