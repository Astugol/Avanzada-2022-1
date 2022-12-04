"""
Modulo contiene implementación principal del cliente
"""
import socket
import pickle
import threading
from utils import data_json
from backend.interfaz import Interfaz
import codificacion

class Cliente:
    def __init__(self):
        self.host = data_json("HOST")
        self.port = data_json("PORT")
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.interfaz = Interfaz(self)
        self.iniciar_cliente()

    def iniciar_cliente(self):
        """
        Se encarga de iniciar el cliente y conectar el socket
        """
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            thread = threading.Thread(target = self.escuchar_servidor, daemon=True)
            thread.start()
            self.interfaz.mostrar_ventana_inicio()
        except ConnectionResetError:
            self.socket_cliente.close()

    def escuchar_servidor(self):
        try:
            while self.conectado:
                mensaje = self.recibir()
                if not mensaje:
                    raise ConnectionResetError
                else:
                    self.interfaz.manejar_mensaje(mensaje)
        except ConnectionResetError:
            pass
        finally:
            self.socket_cliente.close()

    def recibir(self):

        ##ESTO HACE REFERENCIA A LA DECODIFICACIÓN
        
        ## --------------------------------------------------------------
        cantidad_bloques_bytes = self.socket_cliente.recv(4)
        cantidad_bloques = int.from_bytes(cantidad_bloques_bytes, byteorder = "little")
        array_mensaje = bytearray()
        for a in range(cantidad_bloques):
            #print("estoy en los bloques rey")
            numero_bloque = self.socket_cliente.recv(4)
            utilizo_20 = self.socket_cliente.recv(1)
            cantidad_bytes = self.socket_cliente.recv(1)
            cantidad_bytes_int = int.from_bytes(cantidad_bytes, byteorder = "little")
            #print(cantidad_bytes_int)
            array_mensaje += self.socket_cliente.recv(cantidad_bytes_int)
            #print("esto es lo que llevo de mensaje: ", array_mensaje)
        ## --------------------------------------------------------------
        try:
            desencripando = codificacion.desencriptar(array_mensaje)
            leible = pickle.loads(desencripando)
        except IndexError:
            raise ConnectionError
        #print(leible)
        return leible

    def enviar(self, msg):

        ## Lo serializaremos con PICKLE
        msg_bytes = pickle.dumps(msg)
        ## Lo encriptamos
        mensaje_encriptado = codificacion.encriptacion(msg_bytes)
        ## Lo codificamos
        mensaje_codificado = codificacion.codificar(mensaje_encriptado)
        ## Lo enviamos
        self.socket_cliente.sendall(mensaje_codificado)
        pass