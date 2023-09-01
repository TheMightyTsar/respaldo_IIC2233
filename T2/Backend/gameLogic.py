from PyQt5.QtCore import QObject, pyqtSignal, QTimer
import Backend.zaWarudo as zW
import aparicion_zombies as aZ
import parametros as p
import Backend.zombies as z
import Backend.plantas as Plantas
import Backend.soles as Soles
import random
from threading import Lock


class GameLogic(QObject):
    crear_zombie_ventana = pyqtSignal(dict)
    mover_zombie = pyqtSignal(int, int)
    sprite_zombie = pyqtSignal(list)
    sprite_planta = pyqtSignal(dict)
    muy_caro = pyqtSignal()
    mover_sol = pyqtSignal(dict)
    actualizar_ventana = pyqtSignal(dict)
    crear_sol_ventana = pyqtSignal(dict)
    crear_bala_ventana = pyqtSignal(dict)
    mover_bala = pyqtSignal(dict)
    cambiar_sprite_bala = pyqtSignal(dict)
    destruir_bala = pyqtSignal(dict)
    destruir_planta = pyqtSignal(str)
    destruir_zombie = pyqtSignal(str)
    actualizar_post_ronda = pyqtSignal(dict)
    actualizar_puntaje = pyqtSignal(int)
    ahorro_avanzar = pyqtSignal(str)
    acabar_juego = pyqtSignal()

    def __init__(self, ronda: int, clima: str):
        super().__init__()
        self.ronda = ronda
        self.clima = clima
        self.soles = p.SOLES_INICIALES
        self.esperaDeSoles = 0
        self.ZombiesRestantes: int = p.N_ZOMBIES
        self.ZombiesDestruidos: int = 0
        self.puntaje: int = 0

        # zombie related
        self.nZombies = 0
        self.zombies = {}
        self.creadorZombies = QTimer()
        # zombie related

        self.ticker = zW.TimeHandler()
        self.plantas = {}
        self.infoCasillas = None
        self.conexionesCasillas = {}
        self.n_soles = 0
        self.cerebroSoles = {}
        self.balas = {}
        self.nBalas = 0
        self.lock_id_balas = Lock()
        self.lock_id_soles = Lock()
        self.lock_zombies = Lock()
        self.terminoRonda = False
        self.actualizarVentana()

    def actualizarVentana(self):
        datos = {}
        datos['soles'] = self.soles
        datos['zombies_restantes'] = self.ZombiesRestantes
        datos['zombies_destruidos'] = self.ZombiesDestruidos
        datos['puntaje ronda'] = self.puntaje
        datos['ronda'] = self.ronda
        self.actualizar_ventana.emit(datos)

    def recibirValoresDeCasilla(self, datos):
        self.infoCasillas = datos
        for idCasilla in datos:
            self.conexionesCasillas[idCasilla] = []

    def iniciaRonda(self):
        tiempo_entre_zombies = self.intervaloZombies()

        self.creadorZombies.setInterval(tiempo_entre_zombies)
        self.creadorZombies.timeout.connect(self.crearZombies)
        self.creadorZombies.start()
        self.ticker.startTicker()
        self.ticker.tick.connect(self.ambienteCrearSoles)

    def pausarJuego(self, pausar: bool):
        self.ticker.pause = pausar
        if pausar:
            self.creadorZombies.stop()
        else:
            self.creadorZombies.start()

    def selectClima(self, dia):
        if not dia:
            self.clima = 'salidaNocturna'
        else:
            self.clima = 'jardinAbuela'

    def intervaloZombies(self):
        tiempo = 0
        dificultad = p.DIFICULTAD[self.clima]
        tiempo = aZ.intervalo_aparicion(self.ronda, dificultad) * 1000
        tiempo = int(tiempo)
        return tiempo

    def crearZombies(self):
        if self.nZombies < p.N_ZOMBIES:
            self.zombies[f'{self.nZombies}'] = z.Zombie(self.nZombies)
            self.zombies[f'{self.nZombies}'].crear_zombie.connect(self.crearZombieVentana)
            self.zombies[f'{self.nZombies}'].solicitarCreacionZombie()  # para ejecutar la señal
            self.zombies[f'{self.nZombies}'].enviar_sprite.connect(self.cambiarSpriteZombie)
            self.zombies[f'{self.nZombies}'].caminado.connect(self.moverZombie)
            self.zombies[f'{self.nZombies}'].conectar_con_casilla.connect(self.zombiePisaCasilla)
            self.zombies[f'{self.nZombies}'].mordisco.connect(self.danoAPlanta)
            self.zombies[f'{self.nZombies}'].eliminar_zombie.connect(self.muerte_zombie)
            self.zombies[f'{self.nZombies}'].derrota.connect(self.actualizarPostRonda)
            # le conectamos el timer al zombie
            self.ticker.tick.connect(self.zombies[f'{self.nZombies}'].accion)

            self.nZombies += 1
        if self.nZombies == p.N_ZOMBIES:
            self.creadorZombies.stop()

    def crearZombieVentana(self, datos):
        self.crear_zombie_ventana.emit(datos)

    def moverZombie(self, ID, distancia):
        self.mover_zombie.emit(ID, distancia)

    def cambiarSpriteZombie(self, datos):
        self.sprite_zombie.emit(datos)

    def zombiePisaCasilla(self, datosZombie):
        """
        lo que pasara sera que
        si el x del zombie esta dentro de la casilla, se conectaran si sale se desconecta
        """
        if datosZombie['linea'] == 116:
            for i in range(9, -1, -1):

                id_casilla = f'{i}0'
                id_zombie = str(datosZombie['ID'])

                x_minima = self.infoCasillas[id_casilla][0]
                x_maxima = self.infoCasillas[id_casilla][1]
                x_zombie = datosZombie['x']
                if x_minima <= x_zombie <= x_maxima:
                    if self.zombies[id_zombie].casillaAtacada == None:
                        self.zombies[id_zombie].casillaAtacada = id_casilla
                        self.conexionesCasillas[id_casilla].append(id_zombie)

                if x_minima - 1 == x_zombie:
                    # se desconecta de la casilla anterior
                    self.zombies[id_zombie].comiendo = False
                    self.zombies[id_zombie].queHago = 'caminar'
                    self.zombies[id_zombie].casillaAtacada = None
                    self.conexionesCasillas[id_casilla].remove(id_zombie)
        if datosZombie['linea'] == 226:
            for i in range(9, -1, -1):

                id_casilla = f'{i}1'
                id_zombie = str(datosZombie['ID'])

                x_minima = self.infoCasillas[id_casilla][0]
                x_maxima = self.infoCasillas[id_casilla][1]
                x_zombie = datosZombie['x']
                if x_minima <= x_zombie <= x_maxima:
                    if self.zombies[id_zombie].casillaAtacada == None:
                        self.zombies[id_zombie].casillaAtacada = id_casilla
                        self.conexionesCasillas[id_casilla].append(id_zombie)

                if x_minima - 1 == x_zombie:
                    # se desconecta de la casilla anterior
                    self.zombies[id_zombie].comiendo = False
                    self.zombies[id_zombie].queHago = 'caminar'
                    self.zombies[id_zombie].casillaAtacada = None
                    self.conexionesCasillas[id_casilla].remove(id_zombie)

    def cambioCasilla(self, datos):
        ocupada = datos['ocupada']
        idCasilla = datos['idCasilla']
        if len(self.conexionesCasillas[idCasilla]) != 0:
            for elem in self.conexionesCasillas[idCasilla]:
                self.zombies[elem].cambiarAccionZombie(ocupada)

    def muerte_zombie(self, datos):
        idZombie = datos['id']
        casilla = datos['casilla']
        if casilla != None:
            self.conexionesCasillas[casilla].remove(str(idZombie))
        self.destruir_zombie.emit(str(idZombie))
        self.zombies[str(idZombie)].deleteLater()
        del self.zombies[str(idZombie)]
        self.ZombiesRestantes -= 1
        self.ZombiesDestruidos += 1
        if self.clima == 'salidaNocturna':
            self.puntaje += p.PUNTAJE_ZOMBIE_NOCTURNO
        else:
            self.puntaje += p.PUNTAJE_ZOMBIE_DIURNO
        self.actualizarVentana()
        # revisar si zombies restantes es 0, si es asi, ganar y ponderar puntajes con la dificultad
        if self.ZombiesRestantes == 0:
            puntaje_extra = self.puntaje * p.DIFICULTAD[self.clima]
            self.puntaje += puntaje_extra
            self.terminoRonda = True
            self.actualizarPostRonda('victoria')

    def matarLogicaZombie(self, datos):
        self.zombies[str(datos['id'])].recibirDano(datos)

    def avanzar(self):
        if not self.terminoRonda:
            if self.soles >= p.COSTO_AVANZAR:
                self.soles -= p.COSTO_AVANZAR
                self.actualizarPostRonda('victoria')
                self.ticker.timer.stop()
                self.acabar_juego.emit()
        else:
            self.actualizarPostRonda('')
            self.ticker.timer.stop()
            self.acabar_juego.emit()

    def actualizarPostRonda(self, quePaso):
        self.terminoRonda = True
        self.ahorro_avanzar.emit(quePaso)
        self.ticker.timer.stop()
        self.actualizar_puntaje.emit(self.puntaje)
        datos = {'quePaso': quePaso, 'soles': self.soles,
                 'zombies_restantes': self.ZombiesRestantes,
                 'zombies_destruidos': self.ZombiesDestruidos,
                 'puntaje ronda': self.puntaje, 'ronda': self.ronda}
        self.actualizar_post_ronda.emit(datos)

    def sePuedeComprarPlanta(self, precio):
        if precio > self.soles:
            self.muy_caro.emit()

    def comprarPlanta(self, costo):
        self.soles -= costo
        self.actualizarVentana()

    def crearSolesGirasol(self, datos):
        idGirasol = datos['girasol']
        x_girasol = int(self.infoCasillas[idGirasol][0])
        variacion_x = random.randint(p.VARIACION_P_SOL[0], p.VARIACION_P_SOL[1])
        variacion_y = random.randint(p.VARIACION_P_SOL[0], p.VARIACION_P_SOL[1])

        if idGirasol.endswith('0'):
            y_girasol = 116
        else:
            y_girasol = 226
        self.lock_id_soles.acquire()
        datos['id'] = str(self.n_soles)
        self.n_soles += 1
        self.lock_id_soles.release()
        datos['x'] = x_girasol + variacion_x
        datos['y'] = y_girasol + variacion_y
        self.cerebroSoles[datos['id']] = Soles.solCerebro(datos['id'], datos['x'], datos['y'])
        '''
        ### Eliminar este comentario hace que los soles de girasoles tambien caigan
        self.ticker.tick.connect(self.cerebroSoles[datos['id']].moverWidget)
        self.cerebroSoles[datos['id']].mover.connect(self.moverSoles)
        '''
        self.crear_sol_ventana.emit(datos)

    def quitarLogicaSol(self, idSol):
        del self.cerebroSoles[idSol]

    def sumarSoles(self, monto):
        if self.clima == 'salidaNocturna':
            self.soles += monto
        else:
            self.soles += 2 * monto
        self.actualizarVentana()

    def ambienteCrearSoles(self):
        if self.clima == 'jardinAbuela':
            if self.esperaDeSoles == p.INTERVALO_APARICION_SOLES:
                x_sol = random.randint(p.DATOS_JUEGO['x'], p.DATOS_JUEGO['xMax'])
                datos = {}
                self.lock_id_soles.acquire()
                datos['id'] = str(self.n_soles)
                self.n_soles += 1
                self.lock_id_soles.release()
                datos['x'] = x_sol
                datos['y'] = -1 * p.SIZE_SOL
                datos['valor'] = p.SOLES_POR_RECOLECCION
                self.crear_sol_ventana.emit(datos)
                self.cerebroSoles[datos['id']] = Soles.solCerebro(datos['id'],
                                                                    datos['x'],
                                                                    datos['y'])
                self.ticker.tick.connect(self.cerebroSoles[datos['id']].moverWidget)
                self.cerebroSoles[datos['id']].mover.connect(self.moverSoles)
                self.esperaDeSoles = 0

            self.esperaDeSoles += 1

    def moverSoles(self, datos):
        self.mover_sol.emit(datos)

    def crearLogicaPlanta(self, datos):
        idPlanta = datos['id']
        namePlanta = datos['planta']
        x_planta = self.infoCasillas[idPlanta][0]
        if idPlanta.endswith('0'):
            y_planta = 196
        else:
            y_planta = 296

        if namePlanta == 'girasol':
            plantita = Plantas.girasol()
            self.plantas[idPlanta] = plantita
            self.plantas[idPlanta].emit_soles.connect(self.crearSolesGirasol)
        if namePlanta == 'papa':
            plantita = Plantas.papa()
            self.plantas[idPlanta] = plantita
        if namePlanta == 'hieloGuisante':
            plantita = Plantas.hieloGuisante(x_planta, y_planta)
            self.plantas[idPlanta] = plantita
            self.plantas[idPlanta].crear_bala.connect(self.crearLogicaBala)
        if namePlanta == 'lanzaGuisante':
            plantita = Plantas.lanzaGuisante(x_planta, y_planta)
            self.plantas[idPlanta] = plantita
            self.plantas[idPlanta].crear_bala.connect(self.crearLogicaBala)
        self.plantas[idPlanta].asignarID(idPlanta)
        self.plantas[idPlanta].destruyeme.connect(self.quitarLogicaPlanta)
        self.plantas[idPlanta].destruyeme.connect(self.quitarLabelPlanta)
        self.plantas[idPlanta].change_sprite.connect(self.cambiarSpritePlanta)
        self.ticker.tick.connect(self.plantas[idPlanta].accion)

    def crearLogicaBala(self, datos):
        self.lock_id_balas.acquire()
        idBala = str(self.nBalas)
        self.nBalas += 1
        self.lock_id_balas.release()
        tipo = datos['tipo']
        x_bala = datos['x']
        y_bala = datos['y']
        if tipo == 'hielo':
            self.balas[idBala] = Plantas.balaHielo(idBala, x_bala, y_bala)
        else:
            self.balas[idBala] = Plantas.balaNormal(idBala, x_bala, y_bala)
        self.balas[idBala].mover_bala.connect(self.moverBala)
        self.balas[idBala].mover_bala.connect(self.balaImpactaZombie)
        self.balas[idBala].cambiar_sprite.connect(self.cambiarSpriteBala)
        self.balas[idBala].destruir_bala.connect(self.destruirBala)
        datos['id'] = idBala
        self.crear_bala_ventana.emit(datos)
        self.ticker.tick.connect(self.balas[idBala].mover)
        self.ticker.tick.connect(self.balas[idBala].animar)

    def moverBala(self, datos):
        self.mover_bala.emit(datos)

    def cambiarSpriteBala(self, datos):
        self.cambiar_sprite_bala.emit(datos)

    def impactoBala(self, datos):
        self.balas[datos['id']].impacto()

    def destruirBala(self, datos):
        self.destruir_bala.emit(datos)

    def danoAPlanta(self, datos):
        idPlanta = datos['idCasilla']
        dano = int(datos['dano'])
        self.plantas[idPlanta].recibirDamage(dano)

    def quitarLogicaPlanta(self, idPlanta):
        self.plantas[idPlanta].deleteLater()

    def quitarLabelPlanta(self, idPlanta):
        self.plantas[idPlanta].deleteLater()
        self.destruir_planta.emit(idPlanta)

    def cambiarSpritePlanta(self, datos):
        self.sprite_planta.emit(datos)

    def balaImpactaZombie(self, datosBala):
        if datosBala['y'] == 196:
            lineaBala = 116
        else:
            lineaBala = 226
        zombieAtacado = None
        for idZombie in self.zombies:
            if self.zombies[idZombie] != None:
                if self.zombies[idZombie].linea == lineaBala:
                    x_min = self.zombies[idZombie].x
                    x_max = x_min + p.ANCHO_ZOMBIE
                    x_min_b = datosBala['x']
                    x_centro = x_min_b + (p.PORTE_BALA/2)

                    if x_min <= x_centro <= x_max:

                        zombieAtacado = idZombie
                        self.balas[datosBala['id']].impacto()
        if zombieAtacado != None:
            if self.zombies[zombieAtacado] != None:
                self.zombies[zombieAtacado].recibirDano(datosBala)