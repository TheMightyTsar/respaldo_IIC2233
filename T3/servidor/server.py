import socket
from threading import Thread
import cripto
import jsonManager as JM

class servidor:
    def __init__(self, Host, Port):
        self.host = Host
        self.port = Port
        self.socket_servidor = None
        self.id_cliente = 0
        self.log("".center(80, "-"))
        self.log("Inicializando servidor")
        self.sockets = {}
        self.users = []
        self.iniciar_servidor()

    def iniciar_servidor(self):
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        self.log("".center(80, "-"))
        self.log('...Servidor Iniciado...')
        txt = "Cliente".center(10, " ") + "|".center(10, " ")\
              +"Evento".center(10, " ") + "|".center(10, " ") + "Detalles"

        self.log(txt)
        self.comenzar_aceptar()


    def comenzar_aceptar(self):
        while True:  # Siempre aceptando clientes
            try:
                socket_cliente, _ = self.socket_servidor.accept()
                thread = Thread(
                    target=self.escuchar_cliente,
                    args=(self.id_cliente, socket_cliente),
                    daemon=True  # Los thread se cierran junto al servidor
                )
                thread.start()
                txt = f"{self.id_cliente}".center(10, " ") + "|".center(10, " ") \
                      + "conectando".center(10, " ") + "|".center(10, " ")

                self.log(txt)

                self.sockets[self.id_cliente] = socket_cliente
                self.id_cliente += 1


            except ConnectionError:
                self.log('...')

    def escuchar_cliente(self, id_cliente, socket_cliente):
        try:
            while True:  # Siempre escuchando mensajes
                mensaje = self.recibir_mensaje(socket_cliente)
                if not mensaje:  # No hay mensaje, levantar un error específico
                    raise ConnectionResetError
                respuesta = self.procesar_mensaje(mensaje, socket_cliente)
                if respuesta:
                    self.enviar_mensaje(respuesta, socket_cliente)

        except ConnectionError:  # Atajar cualquier error del tipo Connection
            self.log('...')


    def recibir_mensaje(self, socket_cliente):
        bytes_mensaje = bytearray()
        bytes_largo_mensaje = socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(bytes_largo_mensaje, byteorder='little')
        while len(bytes_mensaje) < largo_mensaje:
            bytes_mensaje += socket_cliente.recv(min(64, largo_mensaje - len(bytes_mensaje)))
        return self.decodificar_mensaje(bytes_mensaje)

    def enviar_mensaje(self, mensaje, socket_cliente):
        bytes_mensaje = self.codificar_mensaje(mensaje)
        largo_mensaje = len(bytes_mensaje).to_bytes(4, byteorder='little')
        socket_cliente.sendall(largo_mensaje + bytes_mensaje)

    def codificar_mensaje(self, mensaje):
        # transforma un str a un bitearray
        pass

    def decodificar_mensaje(self, mensaje_bytes):
        return cripto.desencriptar(mensaje_bytes)

    def procesar_mensaje(self, mensaje, socket):

        pass

    def validarUsuario(self, username, socketCliente):
        if 1 <= username.lenght() <= 10:
            if username not in self.users:
                return True
            else:
                self.enviar_mensaje(JM.data_json('ERROR_USER_USED'), socketCliente)
                return False
        self.enviar_mensaje(JM.data_json('ERROR_USER_LARGO'), socketCliente)
        return False

    def log(self, mensaje):
        print("|" + mensaje.center(80, " ") + "|")
