
### dara ticks que indiquen el paso del tiempo,
# si no emiten no se ejecutan las funciones de los juegos, pyqtSygnal
from PyQt5.QtCore import pyqtSignal, QTimer, QObject
import parametros as p


class TimeHandler(QObject):
    tick = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.startedTicking = False
        self.pause = False
        self.timer = QTimer()


    def Ticks(self):
        '''
        envia la señal tick, cuando se envia los
        zombies, plantas y otros objetos en ventaja juego funcionan
        '''
        if not self.pause:
            self.tick.emit()


    def changePause(self, pausar: bool):
        self.pause = pausar

    def startTicker(self):
        self.startedTicking = True
        self.timer.setInterval(p.TIME_BETWEEN_TICKS)
        self.timer.timeout.connect(self.Ticks)
        self.timer.start()


