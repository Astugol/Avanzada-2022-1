"""
Modulo contiene implementación principal del cliente
"""
import socket
import json
from threading import Thread
from backend.interfaz import Interfaz


class Cliente:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.interfaz = Interfaz(self)
        self.iniciar_cliente()

    def iniciar_cliente(self):
        """
        Se encarga de iniciar el cliente y conectar el socket
        """

        # TODO: Completado por estudiante
        self.conectado = True
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.comenzar_a_escuchar()
            self.interfaz.mostrar_ventana_carga()
        except ConnectionError:
            self.log("Error de conexión!")
            self.conectado = False
        pass

    def comenzar_a_escuchar(self):
        """
        Instancia el Thread que escucha los mensajes del servidor
        """
        # TODO: Completado por 
        thread = Thread(target = self.escuchar_servidor)
        thread.start()
        pass

    def escuchar_servidor(self):
        """
        Recibe mensajes constantes desde el servidor y responde.
        """
        # TODO: Completado por estudiante
        try:
            while self.conectado == True:
                mensaje = self.recibir()
                print(mensaje)
                if mensaje != "" or mensaje != {}:
                    self.interfaz.manejar_mensaje(mensaje)
        except ConnectionError:
            print("Error de conexión")
        pass

    def recibir(self):
        """
        Se encarga de recibir lis mensajes del servidor.
        """
        # TODO: Completado por estudiante
        largo = self.socket_cliente.recv(4)
        largo_respuesta = int.from_bytes(largo, byteorder = "little")
        respuesta = bytearray()

        while len(respuesta) < largo_respuesta:
            leer_largo = min(64, largo_respuesta - len(respuesta))
            respuesta.extend(self.socket_cliente.recv(leer_largo))
        
        msj_decodificado = self.decodificar_mensaje(respuesta)
        return msj_decodificado

    def enviar(self, mensaje):
        """
        Envía un mensaje a un cliente.
        """
        # TODO: Completado por estudiante
        msj_codificado = self.codificar_mensaje(mensaje)
        lenght = len(msj_codificado).to_bytes(4, byteorder = "little")
        self.socket_cliente.sendall(lenght + msj_codificado)
        pass

    def codificar_mensaje(self, mensaje):
        """
        Codifica el mensaje a enviar
        """
        try:
            # TODO: Completado por estudiante
            msj_json = json.dumps(mensaje)
            msj = msj_json.encode()
            return msj
        except json.JSONDecodeError:
            print("ERROR: No se pudo codificar el mensaje")
            return b""

    def decodificar_mensaje(self, mensaje_bytes):
        """
        Decodifica el mensaje del servidor
        """
        try:
            # TODO: Completado por estudiante
            msj = json.loads(mensaje_bytes)
            return msj
        except json.JSONDecodeError:
            print("ERROR: No se pudo decodificar el mensaje")
            return {}

    def log(self, mensaje: str):
        """
        Imprime un mensaje en consola
        """
        print("|" + mensaje.center(80, " ") + "|")
