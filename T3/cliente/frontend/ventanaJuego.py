from PyQt5 import uic
import os
import cliente.jsonManager as JsonManage



window_name, base_class = uic.loadUiType(os.path.join(JsonManage.data_json('RUTA_VENTANA_JUEGO')))


class VentanaJuego(window_name, base_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


