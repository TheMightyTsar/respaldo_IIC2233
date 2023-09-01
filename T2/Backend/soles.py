from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
import parametros as p

class solesWidget(QLabel):

    def __init__(self, idSol, valor, px, py, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.idSol = str(idSol)
        self.value = valor
        self.x_sol = px
        self.y_sol = py
        self.setGeometry(self.x_sol, self.y_sol,
                         p.SIZE_SOL, p.SIZE_SOL)
        pixeles = QPixmap(p.RUTA_SOL)
        self.setPixmap(pixeles)
        self.setScaledContents(True)
        self.raise_()
        self.setVisible(True)

    def mover(self, pY):
        self.y_sol = pY
        self.move(self.x_sol, pY)


class solCerebro(QObject):
    mover = pyqtSignal(dict)

    def __init__(self, idSol, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.idSol = idSol

    def moverWidget(self):
        if self.y < p.DATOS_JUEGO['yMax'] - p.SIZE_SOL:
            self.y += p.CAIDA_SOL
            datos = {}
            datos['id'] = self.idSol
            datos['x'] = self.x
            datos['y'] = self.y
            self.mover.emit(datos)