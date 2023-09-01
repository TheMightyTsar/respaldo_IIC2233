from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_POSTRONDA)


class VentanaPostRonda(window_name, base_class):
    siguiente_ronda = pyqtSignal()
    volver_menu_inicio = pyqtSignal()
    actualizar_ranking = pyqtSignal(str, int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.user = None
        self.puntaje = None
        self.continuar.clicked.connect(self.siguiente_ronda)

        self.volver_menu.clicked.connect(self.volverMenu)

    def actualizarVentana(self, datos):
        self.soles.setText(str(datos['soles']))
        self.z_destruidos.setText(str(datos['zombies_destruidos']))
        self.puntaje_ronda.setText(str(datos['puntaje ronda']))
        self.ronda.setText(str(datos['ronda']))
        print(datos['quePaso'])
        if datos['quePaso'] == 'victoria':
            print('entro if')
            self.derrota.setVisible(False)
            self.victoria.setVisible(True)
            self.continuar.setVisible(True)
        if datos['quePaso'] == 'derrota':
            print('entro else')
            self.continuar.setVisible(False)
            self.victoria.setVisible(False)
            self.derrota.setVisible(True)
        self.actualizar_ranking.emit(self.user, self.puntaje)

    def actualizarPuntajeTotal(self, valor):
        self.puntaje = valor
        self.puntaje_total.setText(str(valor))

    def actualizarUser(self, user):
        self.user = user

    def siguienteRonda(self):
        self.ocultarVentana()
        self.siguiente_ronda.emit()

    def volverMenu(self):
        self.ocultarVentana()
        self.volver_menu_inicio.emit()

    def mostrarVentana(self):
        self.show()

    def ocultarVentana(self):
        self.hide()