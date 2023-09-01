from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p
from threading import Lock

class RankingLogic(QObject):

    ranking_actualizado = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.lock_ranking = Lock()
        self.actualizar_ranking()

    def actualizar_ranking(self):
        '''
        esta funcion enviara una señal para actualizar la ventana de ranking.
        Usa self.lock_ranking para asegurar que no se habra ni se edite
        en otras partes del codigo puntajes.txt
        '''
        self.lock_ranking.acquire()
        open_txt = open(p.RUTA_RANKING, 'r')
        lines_txt = open_txt.readlines()
        open_txt.close()


        jugadores = []
        for elem in lines_txt:
            jugadores.append(elem.strip('\n').split(','))

        jugadores.sort(key=primeros_jugadores, reverse=True)
        jugadores = jugadores[:5]


        self.lock_ranking.release()

        self.ranking_actualizado.emit(jugadores)


    def add_puntaje(self, usuario, puntaje):
        self.lock_ranking.acquire()
        open_txt = open(p.RUTA_RANKING, 'r', encoding='utf-8')
        lines_txt = open_txt.readlines()
        open_txt.close()

        jugadores = []
        for linea in lines_txt:
            jugadores.append(linea.strip('\n').split(','))

        actualizado = False
        for i in range(0, len(jugadores)):
            if jugadores[i][0] == usuario:
                actualizado = True
                jugadores[i] = [usuario, puntaje]
        if not actualizado:
            jugadores.append([usuario, puntaje])

        open_txt = open(p.RUTA_RANKING, 'w', encoding='utf-8')
        for jugador in jugadores:
            print(f'{jugador[0]},{jugador[1]}', file=open_txt)
        open_txt.close()


        self.lock_ranking.release()

def primeros_jugadores(jugador_y_puntaje):
    '''
    :param jugador_y_puntaje:
    :return: Puntaje
    esta funcion esta hecha para hacer sort a la lista jugadores en
    el metodo actualizar_ranking de la
    clase RankingLogic

    '''
    puntaje = int(jugador_y_puntaje[1])
    return puntaje


