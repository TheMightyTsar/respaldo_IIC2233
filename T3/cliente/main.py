import sys
import DCCardJitsu as DCC
import os

### Código de cortesía de Felipe Pezoa, 2017
if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)


    sys.__excepthook__ = hook
    ### Código de cortesía de Felipe Pezoa, 2017

    game = DCC.DCCard(sys.argv)
    game.encender()
    sys.exit(game.exec())

