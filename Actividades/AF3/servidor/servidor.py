"""
Modulo contiene la implementación principal del servidor
"""
import json
import socket
import threading
from logica import Logica


class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = None
        self.conectado = False
        self.logica = Logica(self)
        self.id_cliente = 0
        self.log("".center(80, "-"))
        self.log("Inicializando servidor...")
        self.iniciar_servidor()

    def iniciar_servidor(self):
        """
        Crea el socket, lo enlaza y comienza a escuchar
        """
        # TODO: Completado por estudiante
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        self.conectado = True
        self.log(f"El host es: {self.host} y se está escuchando desde el puerto {self.port}")
        self.comenzar_a_aceptar()
        pass
        

    def comenzar_a_aceptar(self):
        """
        Crea y comienza el thread encargado de aceptar clientes
        """
        # TODO: Completado por estudiante
        thread = threading.Thread(target = self.aceptar_clientes)
        thread.start()
        pass
        

    def aceptar_clientes(self):
        """
        Es arrancado como thread para de aceptar clientes, este se ejecuta
        siempre que se este conectado y acepta el socket del servidor. Luego
        se crea y comienza a escuchar al cliente. para finalmente aumentar en 1
        el id_cliente.
        """
        while self.conectado:
        # TODO: Completado por estudiante
            try:
                client_socket, _ = self.socket_servidor.accept()
                thread_escuchando_cliente = threading.Thread(target = self.escuchar_cliente,
                args = (self.id_cliente , client_socket), daemon = True)
                thread_escuchando_cliente.start()
                self.id_cliente += 1
                pass
            except ConnectionError as fallo:
                print("Conexión fallida")
                thread_escuchando_cliente.close()
                pass


    def escuchar_cliente(self, id_cliente, socket_cliente):
        """
        Ciclo encargado de escuchar a cada cliente de forma individual, esta
        funcion se ejecuta siempre que el servidor este conectado, recibe el
        socket del cliente y si hay un mensaje, lo procesa con la funcion
        instanciada en la logica.
        """
        self.log(f"Comenzando a escuchar al cliente {id_cliente}...")
        # TODO: Completado por estudiante
        try:
            while self.conectado:
                mensaje_recibido = self.recibir_mensaje(socket_cliente)
                
                if mensaje_recibido:
                    respuesta_procesada = self.logica.procesar_mensaje(mensaje_recibido, socket_cliente)
                    if respuesta_procesada:
                        self.enviar_mensaje(respuesta_procesada, socket_cliente)
                    pass
                    
                else:
                    print("El mensaje es vacío, hay un error de conexión")
                    self.eliminar_cliente(id_cliente, socket_cliente)
                    
                pass
        except ConnectionError as fallo:
            print("Conexión fallida")
            self.eliminar_cliente(id_cliente, socket_cliente)
            pass


    def recibir_mensaje(self, socket_cliente):
        """
        Recibe un mensaje del cliente, lo DECODIFICA usando el protocolo
        establecido y lo des-serializa retornando un diccionario.
        """
        # TODO: Completado por estudiante
        largo_respuesta = socket_cliente.recv(4)
        lenght_respuesta = int.from_bytes(largo_respuesta, byteorder = "little")
        respuesta = bytearray()

        while len(respuesta) < lenght_respuesta:
            leer_largo = min(64, lenght_respuesta - len(respuesta))
            respuesta.extend(socket_cliente.recv(leer_largo))

        decodificado = self.decodificar_mensaje(respuesta)
        return decodificado

    def enviar_mensaje(self, mensaje, socket_cliente):
        """
        Recibe una instruccion,
        lo CODIFICA usando el protocolo establecido y lo envía al cliente
        """
        # TODO: Completado por estudiante
        msj_codificado = self.codificar_mensaje(mensaje)
        lenght = len(msj_codificado).to_bytes(4, byteorder = "little")
        socket_cliente.sendall(lenght + msj_codificado)
        pass

    def enviar_archivo(self, socket_cliente, ruta):
        """
        Recibe una ruta a un archivo a enviar y los separa en chunks de 8 kb
        """
        with open(ruta, "rb") as archivo:
            chunk = archivo.read(8000)
            largo = len(chunk)
            while largo > 0:
                chunk = chunk.ljust(8000, b"\0")  # Padding
                msg = {
                    "comando": "chunk",
                    "argumentos": {"largo": largo, "contenido": chunk.hex()},
                    "ruta": ruta,
                }
                self.enviar_mensaje(msg, socket_cliente)
                chunk = archivo.read(8000)
                largo = len(chunk)

    def eliminar_cliente(self, id_cliente, socket_cliente):
        """
        Elimina un cliente del diccionario de clientes conectados
        """
        try:
            # Cerramos el socket
            self.log(f"Borrando socket del cliente {id_cliente}.")
            socket_cliente.close()
            # Desconectamos el usuario de la lista de jugadores
            self.logica.procesar_mensaje(
                {"comando": "desconectar", "id": id_cliente}, socket_cliente
            )

        except KeyError as e:
            self.log(f"ERROR: {e}")

    def codificar_mensaje(self, mensaje):
        try:
            msj_json = json.dumps(mensaje)
            msj = msj_json.encode()
            return msj

        except json.JSONDecodeError:
            print("NO SE PUDO CODIFICAR")


    def decodificar_mensaje(self, mensaje_bytes):
        try:
            mensaje_decodificado = json.loads(mensaje_bytes)
            return mensaje_decodificado

        except json.JSONDecodeError:
            print("NO SE PUDO DECODIFICAR")

    def log(self, mensaje: str):
        """
        Imprime un mensaje en consola
        """
        print("|" + mensaje.center(80, " ") + "|")
