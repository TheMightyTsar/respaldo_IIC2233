from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import parametros as p
import Backend.zombies as z
import Backend.mouse as SelfMouse
import Backend.plantas as Plantas
import Backend.casillas as Casillas
import Backend.soles as Soles
from PyQt5.QtWidgets import QLabel, QPushButton

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)


class VentanaJuego(window_name, base_class):
    pausar = pyqtSignal(bool)
    startRound = pyqtSignal()
    nextRound = pyqtSignal()
    salir_juego = pyqtSignal(str)
    querer_avanzar = pyqtSignal()
    solicitarDatos = pyqtSignal()
    enviar_datos = pyqtSignal(dict)
    send_datos_casillas = pyqtSignal(dict)
    plantar_plantita = pyqtSignal(dict)
    quitar_planta = pyqtSignal(str)
    costo_planta = pyqtSignal(int)
    cobrar_planta = pyqtSignal(int)
    sumar_soles = pyqtSignal(int)
    eliminar_sol = pyqtSignal(str)
    cheat_kill = pyqtSignal(dict)
    salir_a_pr = pyqtSignal()

    def __init__(self, ronda: int, clima: str):
        # se inicializa lo nescesario
        super().__init__()
        self.setupUi(self)
        self.cantidad_rondas.setText(str(ronda))
        self.setMouseTracking(True)
        self.fondo.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.mouseFollower = None
        self.mousePresionado = False
        self.casillas = {}
        self.conectarUI()
        self.iniciada_ronda = False
        self.nZombies = 0
        self._clima = clima
        self.setClima()
        self.pausado: bool = False
        self.zombies = {}
        self.soles = {}
        self.balas = {}
        self.CHEAT = ''
        self.victoria.setVisible(False)
        self.derrota.setVisible(False)
    # eventos de mouse
    def mousePressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        boton = event.button()
        sol = None
        if boton == 2:
            for idSol in self.soles:
                click = False
                falso = 0
                if x >= self.soles[idSol].x_sol + p.SIZE_SOL:
                    click = False
                    falso += 1
                if x <= self.soles[idSol].x_sol:
                    click = False
                    falso += 1

                if y >= self.soles[idSol].y_sol + p.SIZE_SOL:
                    click = False
                    falso += 1
                if y <= self.soles[idSol].y_sol:
                    click = False
                    falso += 1
                if falso == 0:
                    click = True
                if click:
                    valor_sol = self.soles[idSol].value
                    self.sumar_soles.emit(valor_sol)

                    sol = idSol
        if sol != None:
            self.sumar_soles.emit(self.soles[sol].value)
            self.soles[sol].deleteLater()
            self.eliminar_sol.emit(str(sol))
            del self.soles[sol]

    def mouseMoveEvent(self, event):
        '''
        movera el mouseFollower si se mantiene presionado el click
        '''
        x = event.pos().x()
        y = event.pos().y()

        if self.mouseFollower != None:
            if self.mousePresionado:
                self.mouseFollower.move(x - 50, y - 50)

    def mouseReleaseEvent(self, event):
        self.mousePresionado = False
        if self.mouseFollower != None:
            '''
                    hara que se emita una señal si es que
                    mouseFollower != None
                    la posicion del mouse que checkeara con las casillas, que responderan
                    si es valida la posicion mouseFollower emite soltar planta
            '''
            sobreCasilla = False
            idCasilla = ''
            x = event.pos().x()
            y = event.pos().y()
            for elem in self.casillas.values():
                if elem.checkMouseSobreCasilla(x, y):
                    sobreCasilla = True
                    idCasilla = elem.ID

            nombre_planta = self.mouseFollower.plantaEscogida
            if nombre_planta == 'pala':
                if sobreCasilla:
                    if self.casillas[idCasilla].ocupada:
                        self.casillas[idCasilla].quitarPlanta()
                        self.quitar_planta.emit(idCasilla)
            else:
                if sobreCasilla:
                    self.casillas[idCasilla].asignarPlanta(nombre_planta)
                    costo_plantar = p.COSTOS_PLANTAS[nombre_planta]
                    self.cobrar_planta.emit(costo_plantar)
            self.mouseFollower.deleteLater()
            self.mouseFollower = None

    def keyPressEvent(self, event):
        # P es la key 80
        if event.key() == 80:
            self.pausarJuego()
        else:
            self.CHEAT += event.text()
            print(self.CHEAT)

    def keyReleaseEvent(self, event):
        if self.CHEAT == 'SUN':
            self.sumar_soles.emit(p.SOLES_EXTRA)
        if self.CHEAT == 'KIL':
            print('enviando señal cheat')
            for idZ in self.zombies:
                datos = {'id': idZ, 'damage': p.ULTIMATE_DAMAGE}
                self.cheat_kill.emit(datos)
        self.CHEAT = ''
        pass


    def cancelarMouseFollower(self):
        # se ejcuta si no se puede comprar la planta
        self.mouseFollower.deleteLater()
        self.mouseFollower = None

    def crearGuisanteFollower(self):
        if not self.pausado:
            '''
            se crea el mouseFollower y tiene asignado un guisante
            '''
            planta = 'lanzaGuisante'
            self.mouseFollower = SelfMouse.MouseFollower(planta, self)
            self.mouseFollower.setAttribute(Qt.WA_TransparentForMouseEvents)
            self.mousePresionado = True
            costo = p.COSTOS_PLANTAS[planta]
            self.costo_planta.emit(costo)

    def crearHieloGuisanteFollower(self):
        if not self.pausado:
            '''
            se crea el mouseFollower y tiene asignado un Hielo Guisante
            '''
            plantita = 'hieloGuisante'
            self.mouseFollower = SelfMouse.MouseFollower(plantita, self)
            self.mouseFollower.setAttribute(Qt.WA_TransparentForMouseEvents)
            self.mousePresionado = True
            costo = p.COSTOS_PLANTAS[plantita]
            self.costo_planta.emit(costo)

    def crearGirasolFollower(self):
        if not self.pausado:
            '''
            se crea el mouseFollower y tiene asignado un Girasol
            '''
            plantita = 'girasol'
            self.mouseFollower = SelfMouse.MouseFollower(plantita, self)
            self.mouseFollower.setAttribute(Qt.WA_TransparentForMouseEvents)
            self.mousePresionado = True
            costo = p.COSTOS_PLANTAS[plantita]
            self.costo_planta.emit(costo)

    def crearPapaFollower(self):
        if not self.pausado:
            '''
            se crea el mouseFollower y tiene asignado una papa
            '''
            plantita = 'papa'
            self.mouseFollower = SelfMouse.MouseFollower(plantita, self)
            self.mouseFollower.setAttribute(Qt.WA_TransparentForMouseEvents)
            self.mousePresionado = True
            costo = p.COSTOS_PLANTAS[plantita]
            self.costo_planta.emit(costo)

    def crearPalaFollower(self):
        if not self.pausado:
            '''
            se crea el mouseFollower y tiene asignado una pala
            '''
            plantita = 'pala'
            self.mouseFollower = SelfMouse.MouseFollower(plantita, self)
            self.mouseFollower.setAttribute(Qt.WA_TransparentForMouseEvents)
            self.mousePresionado = True

    def plantarPlantita(self, datos):
        self.plantar_plantita.emit(datos)

    def cambiarSpritePlanta(self, datos):
        idPlanta = datos['id']
        ruta = datos['ruta']
        pixeles = QPixmap(ruta)
        self.casillas[idPlanta].setPixmap(pixeles)

    def iniciarRonda(self):
        if not self.iniciada_ronda:
            self.iniciada_ronda = True
            self.startRound.emit()

    def mostrar_ventana(self):
        self.setMouseTracking(True)
        self.setCasillas()
        self.show()

    def ocultarVentana(self):
        self.hide()

    def actualizarUI(self, datos):
        self.cantidad_zombies_restantes.setText(str(datos['zombies_restantes']))
        self.cantidad_zombies_destruidos.setText(str(datos['zombies_destruidos']))
        self.cantidad_soles.setText(str(datos['soles']))
        self.cantidad_puntaje.setText(str(datos['puntaje ronda']))

    def salirJuego(self):

        self.salir_juego.emit('derrota')

    def pausarJuego(self):
        '''
        envia la señal nescesaria para pausar el juego en caso que se presione el boton de pausa

        '''
        if self.iniciada_ronda:
            if self.pausado:
                self.boton_pausa.setText('Pausar')
                self.pausado = False
                self.pausar.emit(False)
            else:
                self.boton_pausa.setText('Reanudar')
                self.pausado = True
                self.pausar.emit(True)

    def conectarUI(self):
        self.boton_pausa.clicked.connect(self.pausarJuego)
        self.boton_salir.clicked.connect(self.salirJuego)
        self.boton_start_ronda.clicked.connect(self.iniciarRonda)
        self.boton_avanzar.clicked.connect(self.quererAvanzar)
        # botones plantas (drag and drop) se usa pressed
        self.boton_guisante.pressed.connect(self.crearGuisanteFollower)
        self.boton_hielo.pressed.connect(self.crearHieloGuisanteFollower)
        self.boton_girasol.pressed.connect(self.crearGirasolFollower)
        self.boton_papa.pressed.connect(self.crearPapaFollower)
        self.boton_pala.pressed.connect(self.crearPalaFollower)

    def quererAvanzar(self):
        self.querer_avanzar.emit()

    def cambioCostoAvanzar(self, quePaso):
        self.costo_avanzar.setText(str(0))
        if quePaso == 'derrota':
            self.derrota.setVisible(True)
            self.derrota.raise_()

        if quePaso == 'victoria':
            self.victoria.setVisible(True)
            self.victoria.raise_()


    def setCasillas(self):
        '''
        pone las casillas en la ventana, tambien guardara la ID y los x abordados
        por cada casilla, esto en el dict datos
        '''
        datos = {}
        posicion_y = 190
        for y in range(0, 2):
            posicion_x = 470
            for x in range(0, 10):
                idCasilla = f'{x}{y}'
                self.casillas[idCasilla] = Casillas.casilla(posicion_x,
                                                            posicion_y,
                                                            idCasilla,
                                                            self)
                self.casillas[idCasilla].plantar_plantita.connect(self.plantarPlantita)
                self.solicitarDatos.connect(self.casillas[idCasilla].ocupadaCasilla)
                self.casillas[idCasilla].ocupacion_casilla.connect(self.actualizacionDatosCasila)
                datos[idCasilla] = [posicion_x, posicion_x + 65]

                posicion_x += 65
            posicion_y += 87
        self.send_datos_casillas.emit(datos)

    def solicitarDatosCasillas(self):
        self.solicitarDatos.emit()

    def actualizacionDatosCasila(self, datos):
        self.enviar_datos.emit(datos)

    def setClima(self):
        if self._clima == 'salidaNocturna':
            pixeles = QPixmap(p.FONDO_NOCHE)
            self.fondo.setPixmap(pixeles)

        else:
            pixeles = QPixmap(p.FONDO_DIA)
            self.fondo.setPixmap(pixeles)

    def selectClima(self, dia):

        if not dia:
            self._clima = 'salidaNocturna'
        else:
            self._clima = 'patioAbuela'

        self.setClima()

    def crearZombie(self, datos):
        self.zombies[datos['ID']] = z.ZombieWidget(datos, self)
        self.zombies[datos['ID']].setAttribute(Qt.WA_TransparentForMouseEvents)

    def moverZombie(self, idZombie, distancia):
        self.zombies[idZombie].caminar(distancia)

    def cambiarSpriteZombie(self, datos):
        idZombie = datos[0]
        direction = datos[1]
        pixeles = QPixmap(direction)
        self.zombies[idZombie].setPixmap(pixeles)

    def destruirPlanta(self, idPlanta):
        self.casillas[idPlanta].quitarPlanta()

    def crearSol(self, datos):
        # considerar agregar lock
        idSol = datos['id']
        x = datos['x']
        y = datos['y']
        valor = datos['valor']
        self.soles[idSol] = Soles.solesWidget(idSol, valor, x, y, self)
        self.soles[idSol].setAttribute(Qt.WA_TransparentForMouseEvents)

    def moverSol(self, datos):

        idSol = datos['id']
        xSol = datos['x']
        ySol = datos['y']
        self.soles[idSol].mover(ySol)

    def crearBala(self, datos):
        idBala = datos['id']
        tipo = datos['tipo']
        if tipo == 'hielo':
            self.balas[idBala] = Plantas.balaHieloWidget(datos, self)
        else:
            self.balas[idBala] = Plantas.balaWidget(datos, self)

    def moverBala(self, datos):
        idBala = datos['id']
        self.balas[idBala].mover(datos)

    def cambiarSpriteBala(self, datos):
        idBala = datos['id']
        self.balas[idBala].cambiarSprite(datos)

    def destruirBala(self, datos):
        idBala = datos['id']
        self.balas[idBala].deleteLater()

    def matarZombie(self, zombieID):

        self.zombies[int(zombieID)].deleteLater()
