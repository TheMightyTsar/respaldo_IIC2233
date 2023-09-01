from PyQt5.QtWidgets import QApplication
from jsonManager import data_json
# importamos frontend
import frontend.ventanaJuego as VJ
import frontend.ventanaInicio as VI
import frontend.ventanaEspera as VE
import frontend.ventanaFinal as VF
# importamos backend
import backend.logicaJuego as LJ
import backend.logicaInicio as LI
import backend.logicaEspera as LE
import backend.client as CL

class DCCard(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.ventanaInicio = VI.VentanaInicio()
        self.ventanaEspera = VE.VentanaEspera()
        self.ventanaJuego = VJ.VentanaJuego()
        self.ventanaFinal = VF.VentanaFinal()
        self.user = CL.Cliente(data_json("HOST"), data_json("PORT"))

    def encender(self):
        self.ventanaInicio.show()