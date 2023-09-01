"""
Modulo contiene implementación principal del cliente
"""
from PyQt5.QtCore import pyqtSignal, QObject
import socket
import json
from threading import Thread


class Cliente(QObject):

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.iniciar_cliente()

    def iniciar_cliente(self):
        """
        Se encarga de iniciar el cliente y conectar el socket
        """
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            self.comenzar_a_escuchar()


        except ConnectionError as e:
            print(f"\n-ERROR: El servidor no está inicializado. {e}-")
        except ConnectionRefusedError as e:
            print(f"\n-ERROR: No se pudo conectar al servidor.{e}-")

    def comenzar_a_escuchar(self):
        """
        Instancia el Thread que escucha los mensajes del servidor
        """
        thread = Thread(target=self.escuchar_servidor, daemon=True)
        thread.start()

    def escuchar_servidor(self):
        """
        Recibe mensajes constantes desde el servidor y responde.
        """
        try:
            while self.conectado:
                mensaje = self.recibir()
                if mensaje:
                    # Si hay mensaje, lo envío por una señal al backend
                    self.senal_manejar_mensaje.emit(mensaje)
        except ConnectionError:
            print('...')

    def enviar(self, mensaje):
        bytes_mensaje = self.codificar_mensaje(mensaje)
        largo_mensaje = len(bytes_mensaje).to_bytes(4, byteorder='little')
        self.socket_cliente.sendall(largo_mensaje + bytes_mensaje)

    def codificar_mensaje(self, mensaje):
        # se codifica el mensaje a bite array
        pass

    def decodificar_mensaje(self, mensaje_bytes):
        try:
            mensaje = json.loads(mensaje_bytes)
            return mensaje
        except json.JSONDecodeError:
            print("ERROR: No se pudo decodificar el mensaje")
            return {}
