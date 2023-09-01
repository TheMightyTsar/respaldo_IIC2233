import sys
from PyQt5.QtWidgets import QApplication
from dccruz import DCCruz

### Código de cortesía de Felipe Pezoa, 2017
if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)


    sys.__excepthook__ = hook
    ### Código de cortesía de Felipe Pezoa, 2017

    game = DCCruz(sys.argv)
    game.encender()
    sys.exit(game.exec())
