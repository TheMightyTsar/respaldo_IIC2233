from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p

class PostRoundLogic(QObject):
    def __init__(self):
        super().__init__()