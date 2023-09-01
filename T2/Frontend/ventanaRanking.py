from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_RANKING)


class VentanaRanking(window_name, base_class):



    # se enviara esta señal al backend para que otorgue una lista actualizada de los rankings
    solicitar_ranking = pyqtSignal()
    # se permite volver a la ventana de Inicio
    volver_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.volverButton.clicked.connect(self.ocultar_ventana)

    def mostrar_ventana(self):
        self.solicitar_ranking.emit()

        self.show()

    def ocultar_ventana(self):
        self.volver_inicio.emit()
        self.hide()

    def mostrar_rank(self, ranking):
        '''
        :param ranking:
        :return:

        actualiza el texto de los labels en ranking para mostrar valores nuevos
        '''
        primer = ranking[0]
        segundo = ranking[1]
        tercer = ranking[2]
        cuarto = ranking[3]
        quinto = ranking[4]

        self.usuario_1.setText(primer[0])
        self.puntaje_1.setText(primer[1])

        self.usuario_2.setText(segundo[0])
        self.puntaje_2.setText(segundo[1])

        self.usuario_3.setText(tercer[0])
        self.puntaje_3.setText(tercer[1])

        self.usuario_4.setText(cuarto[0])
        self.puntaje_4.setText(cuarto[1])

        self.usuario_5.setText(quinto[0])
        self.puntaje_5.setText(quinto[1])
