# imports
from PyQt5.QtWidgets import QApplication

'''
se importan las distintas ventanas que conforman el juego
'''
from Frontend.ventanaInicio import VentanaInicio
from Frontend.ventanaJuego import VentanaJuego
from Frontend.ventanaRanking import VentanaRanking
from Frontend.ventanaPrincipal import VentanaPrincipal
from Frontend.ventanaPostRonda import VentanaPostRonda

'''
se importa el backend
'''

from Backend.startLogic import StartLogic
from Backend.rankingLogic import RankingLogic
from Backend.principalLogic import PrincipalLogic
from Backend.gameLogic import GameLogic

import Backend.zombies as Zombies


class DCCruz(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.ronda = 1
        self.ambiente = None
        self.puntajeTotal = 0
        self.user = ''

        # frontend
        self.ventanaInicio = VentanaInicio()
        self.ventanaPrincipal = VentanaPrincipal()
        self.ventanaJuego = VentanaJuego(self.ronda, self.ambiente)
        self.ventanaPosronda = VentanaPostRonda()
        self.ventanaRanking = VentanaRanking()

        # backend y logicas

        self.logica_inicio = StartLogic()
        self.logica_ranking = RankingLogic()
        self.logica_principal = PrincipalLogic()
        self.logica_juego = GameLogic(self.ronda, self.ambiente)

        # conexiones
        self.conectar_inicio()
        self.conectar_ranking()
        self.conectar_principal()
        self.conectar_juego()
        self.conectar_postRonda()


        # mostrar postronda para debugear
    def encender(self):
        self.ventanaInicio.show()

    def salirJuego(self):
        self.quit()

    def conectar_inicio(self):
        # conexiones check usuario
        self.ventanaInicio.enviar_usuario.connect(self.logica_inicio.valid_user)
        self.logica_inicio.validar_entrada.connect(self.ventanaInicio.recibir_user)
        # permite ir de venta inicio a ventana ranking
        self.ventanaInicio.ir_ranking.connect(self.ventanaRanking.mostrar_ventana)
        self.logica_inicio.ir_a_principal.connect(self.ventanaPrincipal.mostrar_ventana)
        self.logica_inicio.ir_a_principal.connect(self.actualizarUser)

        # conexion para salir
        self.ventanaInicio.salirApp.connect(self.salirJuego)

    def conectar_ranking(self):
        # establece las conexiones para mostrar los valores correctos del ranking
        self.ventanaRanking.solicitar_ranking.connect(self.logica_ranking.actualizar_ranking)
        self.logica_ranking.ranking_actualizado.connect(self.ventanaRanking.mostrar_rank)

        # permite volver a la ventana de inicio una vez en la ventana ranking
        self.ventanaRanking.volver_inicio.connect(self.ventanaInicio.mostrar_ventana)

    def conectar_principal(self):
        # envia si se apreta un RadioButton
        self.ventanaPrincipal.changeScene.connect(self.logica_principal.cambiarEscenario)
        # si se apreta el boton_jugar
        self.ventanaPrincipal.ir_a_jugar.connect(self.logica_principal.checkJugar)
        # si es valido el check jugar
        self.logica_principal.check_juego.connect(self.ventanaPrincipal.ocultar_ventana)
        # añadir conexion con VentanaJuego
        self.logica_principal.check_juego.connect(self.ventanaJuego.mostrar_ventana)
        # le manda la señal a la logica_juego para saber que ambiente es
        self.logica_principal.enviar_ambiente.connect(self.logica_juego.selectClima)
        self.logica_principal.enviar_ambiente.connect(self.actualizarAmbiente)

        # si es invalido el check jugar
        self.logica_principal.errorJugar.connect(self.ventanaPrincipal.errorCheck)

    def conectar_juego(self):
        # CHEAT KILL
        self.ventanaJuego.cheat_kill.connect(self.logica_juego.matarLogicaZombie)
        # le manda la señal a la ventaJuego para seleccionar el ambiente
        self.logica_principal.enviar_ambiente.connect(self.ventanaJuego.selectClima)
        # se conecta el boton de salir
        self.ventanaJuego.salir_juego.connect(self.logica_juego.actualizarPostRonda)
        self.ventanaJuego.salir_a_pr.connect(self.logica_juego.avanzar)
        # se conecta el inicio de ronda, para inicar el Qtimer
        self.ventanaJuego.startRound.connect(self.logica_juego.iniciaRonda)
        # se conecta el boton de pausa con el pausar del Timer
        self.ventanaJuego.pausar.connect(self.logica_juego.pausarJuego)
        # actualizamos los labels de la ventana
        self.logica_juego.actualizar_ventana.connect(self.ventanaJuego.actualizarUI)
        self.logica_juego.actualizarVentana()
        self.logica_juego.actualizar_puntaje.connect(self.actualizarPuntaje)
        self.ventanaJuego.querer_avanzar.connect(self.logica_juego.avanzar)
        self.logica_juego.acabar_juego.connect(self.ventanaJuego.ocultarVentana)

        # conectamos lo relevante a los zombies
        self.logica_juego.crear_zombie_ventana.connect(self.ventanaJuego.crearZombie)
        self.logica_juego.mover_zombie.connect(self.ventanaJuego.moverZombie)
        self.logica_juego.sprite_zombie.connect(self.ventanaJuego.cambiarSpriteZombie)
        self.logica_juego.destruir_zombie.connect(self.ventanaJuego.matarZombie)

        # conectamos lo relevante a las plantas
        self.ventanaJuego.plantar_plantita.connect(self.logica_juego.crearLogicaPlanta)
        self.logica_juego.sprite_planta.connect(self.ventanaJuego.cambiarSpritePlanta)
        self.ventanaJuego.quitar_planta.connect(self.logica_juego.quitarLogicaPlanta)
        self.ventanaJuego.costo_planta.connect(self.logica_juego.sePuedeComprarPlanta)
        self.logica_juego.muy_caro.connect(self.ventanaJuego.cancelarMouseFollower)
        self.ventanaJuego.cobrar_planta.connect(self.logica_juego.comprarPlanta)
        self.logica_juego.destruir_planta.connect(self.ventanaJuego.destruirPlanta)
        # girasoles y soles
        self.logica_juego.crear_sol_ventana.connect(self.ventanaJuego.crearSol)
        self.ventanaJuego.sumar_soles.connect(self.logica_juego.sumarSoles)
        self.ventanaJuego.eliminar_sol.connect(self.logica_juego.quitarLogicaSol)
        self.logica_juego.mover_sol.connect(self.ventanaJuego.moverSol)

        # conectamos relevante a casillas
        self.ventanaJuego.send_datos_casillas.connect(self.logica_juego.recibirValoresDeCasilla)
        self.logica_juego.ticker.tick.connect(self.ventanaJuego.solicitarDatosCasillas)
        self.ventanaJuego.enviar_datos.connect(self.logica_juego.cambioCasilla)
        # conectamos guisantes
        self.logica_juego.crear_bala_ventana.connect(self.ventanaJuego.crearBala)
        self.logica_juego.mover_bala.connect(self.ventanaJuego.moverBala)
        self.logica_juego.cambiar_sprite_bala.connect(self.ventanaJuego.cambiarSpriteBala)
        self.logica_juego.destruir_bala.connect(self.ventanaJuego.destruirBala)

        # relacionado a post ronda
        self.logica_juego.ahorro_avanzar.connect(self.ventanaJuego.cambioCostoAvanzar)
        self.logica_juego.acabar_juego.connect(self.ventanaPosronda.mostrarVentana)
        self.logica_juego.actualizar_post_ronda.connect(self.ventanaPosronda.actualizarVentana)

    def conectar_postRonda(self):

        self.ventanaPosronda.volver_menu_inicio.connect(self.ventanaInicio.show)
        self.ventanaPosronda.volver_menu_inicio.connect(self.reiniciar)
        self.ventanaPosronda.siguiente_ronda.connect(self.newRound)
        self.ventanaPosronda.actualizar_ranking.connect(self.logica_ranking.add_puntaje)

    def actualizarUser(self, user):
        self.user = user
        self.ventanaPosronda.actualizarUser(user)

    def actualizarPuntaje(self, puntajeRonda):
        self.puntajeTotal += puntajeRonda
        self.ventanaPosronda.actualizarPuntajeTotal(self.puntajeTotal)

    def actualizarAmbiente(self, dia):
        if dia:
            self.ambiente = 'jardinAbuela'
        else:
            self.ambiente = 'salidaNocturna'

    def reiniciar(self):
        self.ronda = 1
        self.ambiente = None
        self.puntajeTotal = 0
        self.user = ''
        self.ventanaJuego = VentanaJuego(self.ronda, self.ambiente)
        self.logica_juego = GameLogic(self.ronda, self.ambiente)
        self.conectar_juego()
        self.conectar_principal()
        self.conectar_postRonda()

    def newRound(self):
        self.ronda += 1
        self.ventanaJuego.deleteLater()
        self.ventanaJuego = VentanaJuego(self.ronda, self.ambiente)
        self.logica_juego.deleteLater()
        self.logica_juego = GameLogic(self.ronda, self.ambiente)
        self.conectar_juego()
        self.conectar_principal()
        self.conectar_postRonda()
        self.ventanaJuego.mostrar_ventana()
