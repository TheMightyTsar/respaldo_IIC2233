from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_INICIO)


class VentanaInicio(window_name, base_class):
    enviar_usuario = pyqtSignal(str)
    ir_ranking = pyqtSignal()
    ir_a_principal = pyqtSignal()

    salirApp = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # revisamos los elementos para que se ingrese el usuario
        self.ingresarUsuario.setText('')
        self.ingresarUsuario.setPlaceholderText('Ingresa Tu Usuario')
        self.jugar.clicked.connect(self.enviar_user)

        # conecciones para cambiar de ventana al ir a ventana_ranking
        self.ranking.clicked.connect(self.ir_ranking)
        self.ranking.clicked.connect(self.ocultar_ventana)

        # conecciones para salir de la app
        self.salir.clicked.connect(self.quitApp)

    def enviar_user(self):
        usuario = self.ingresarUsuario.text()
        self.enviar_usuario.emit(usuario)

    def recibir_user(self, valid, error):
        if valid:
            self.ir_a_principal.emit()
            self.hide()
        else:
            self.ingresarUsuario.setText('')
            self.errorText.setText(error)

    def mostrar_ventana(self):
        self.show()

    def ocultar_ventana(self):
        self.hide()

    def quitApp(self):
        print("saliendo...")
        self.salirApp.emit()






