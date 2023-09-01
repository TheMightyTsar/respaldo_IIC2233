from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p

class StartLogic(QObject):

    validar_entrada = pyqtSignal(bool, str)
    ir_a_principal = pyqtSignal(str)


    def __init__(self):
        super().__init__()

    def valid_user(self, entrada):
        '''
        :param entrada:
        :return: valid -> bool
        funcion que revisa si el nombre entregado por el usuario es valido
        '''
        error_message = ""
        if p.MIN_CARACTERES <= len(entrada) <= p.MAX_CARACTERES:
            valid = True
            for elem in entrada:
                elem_valido = False

                if elem.isalpha():
                    elem_valido = True

                if elem.isnumeric():
                    elem_valido = True

                if not elem_valido:
                    valid = False
                    error_message = p.ERROR_INICIO_CARACTERES
        else:
            valid = False
            if p.MIN_CARACTERES > len(entrada):
                error_message = p.ERROR_INICIO_CORTO
            else:
                error_message = p.ERROR_INICIO_LARGO

        if valid:
            self.ir_a_principal.emit(entrada)
        self.validar_entrada.emit(valid, error_message)

