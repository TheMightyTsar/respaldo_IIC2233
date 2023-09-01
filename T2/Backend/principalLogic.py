from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p


class PrincipalLogic(QObject):
    errorJugar = pyqtSignal()
    check_juego = pyqtSignal()
    enviar_ambiente = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

        self.dia = False
        self.noche = False

    def cambiarEscenario(self, txt):
        if 'Salida Nocturna' == txt:
            self.noche = True
            self.dia = False
        else:
            self.noche = False
            self.dia = True

    def checkJugar(self):

        if (self.dia == True) or (self.noche == True):
            self.enviar_ambiente.emit(self.dia)
            self.check_juego.emit()


        else:

            self.errorJugar.emit()
