from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_PRINCIPAL)


class VentanaPrincipal(window_name, base_class):
    changeScene = pyqtSignal(str)
    ir_a_jugar = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.dia_check.toggled.connect(self.enviarAmbiente)
        self.noche_check.toggled.connect(self.enviarAmbiente)
        self.boton_jugar.clicked.connect(self.checkPlay)

    def enviarAmbiente(self):
        boton = self.sender()
        self.changeScene.emit(boton.text())

    def checkPlay(self):
        self.ir_a_jugar.emit()

    def errorCheck(self):
        self.error_text.setHidden(False)

    def mostrar_ventana(self):
        self.error_text.setHidden(True)
        self.show()

    def ocultar_ventana(self):
        self.hide()
