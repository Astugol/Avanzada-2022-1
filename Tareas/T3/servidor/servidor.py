"""
Modulo contiene la implementación principal del servidor
"""
import pickle
import socket
import threading
from logica import Logica
from utils import data_json
import codificacion

class Servidor:

    # Esto se encarga de administrar el acceso a clientes_conectados para evitar errores.
    clientes_conectados_lock = threading.Lock()

    def __init__(self):
        self.host = data_json("HOST")
        self.port = data_json("PORT")
        self.socket_servidor = None
        self.conectado = False
        self.id_cliente = 0
        self.threads = list()
        self.logica = Logica()
        self.log("".center(80, "-"))
        self.log("Inicializando servidor...")
        self.clientes_conectados = {}
        self.iniciar_servidor()

    def iniciar_servidor(self):
        """
        Crea el socket, lo enlaza y comienza a escuchar
        """
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        self.conectado = True
        self.log(f"El host es: {self.host} y se está escuchando desde el puerto {self.port}")
        self.empezar_a_aceptar()

    def empezar_a_aceptar(self):
        """
        Crea y comienza el thread encargado de aceptar clientes
        """
        thread = threading.Thread(target = self.aceptar_clientes, daemon = True)
        thread.start()

    def aceptar_clientes(self):
        """
        Es arrancado como thread para de aceptar clientes, este se ejecuta
        siempre que se este conectado y acepta el socket del servidor. Luego
        se crea y comienza a escuchar al cliente. para finalmente aumentar en 1
        el id_cliente.
        """
        while self.conectado:
            socket_cliente, address = self.socket_servidor.accept()
            with self.clientes_conectados_lock:
                print(f"Un cliente con dirección {address} ha sido aceptado")
                id_cliente = self.id_cliente
                thread_cliente = threading.Thread(target = self.escuchar_cliente, 
                args = (id_cliente,))
                thread_cliente.start()
                self.clientes_conectados[id_cliente] = socket_cliente
                self.id_cliente += 1
                self.threads.append((id_cliente, thread_cliente))


    def escuchar_cliente(self, id_cliente):
        """
        Ciclo encargado de escuchar a cada cliente de forma individual, esta
        funcion se ejecuta siempre que el servidor este conectado, recibe el
        socket del cliente y si hay un mensaje, lo procesa con la funcion
        instanciada en la logica.
        """
        self.log(f"Comenzando a escuchar al cliente {id_cliente}...")
        try:
            socket_cliente_id = self.clientes_conectados[id_cliente]
            while self.conectado:      
                mensaje = self.recibir(socket_cliente_id, id_cliente)
                if not mensaje:
                    #print("No llego naipe rey")
                    raise ConnectionResetError
                respuesta, destinatarios = self.logica.manejar_mensaje(mensaje, id_cliente)
                if respuesta:
                    for destino in destinatarios:
                        socket_cliente = self.clientes_conectados[destino]
                        self.enviar(respuesta, socket_cliente)

        except (ConnectionResetError, ConnectionError):
            self.log(f"Error de conexión con el cliente {id_cliente}")
            self.eliminar_cliente(id_cliente)

    def recibir(self, socket_cliente_id, id_cliente):

        ##ESTO HACE REFERENCIA A LA DECODIFICACIÓN
        
        ## --------------------------------------------------------------
        cantidad_bloques_bytes = socket_cliente_id.recv(4)
        cantidad_bloques = int.from_bytes(cantidad_bloques_bytes, byteorder = "little")
        array_mensaje = bytearray()
        for a in range(cantidad_bloques):
            #print("estoy en los bloques rey")
            numero_bloque = socket_cliente_id.recv(4)  ## Estos bytes son inutiles, le pregunté a un
            utilizo_20 = socket_cliente_id.recv(1)     ## ayudante y me dijo que podía no ocuparlos
            cantidad_bytes = socket_cliente_id.recv(1)
            cantidad_bytes_int = int.from_bytes(cantidad_bytes, byteorder = "little")
            #print(cantidad_bytes_int)
            array_mensaje += socket_cliente_id.recv(cantidad_bytes_int)
            #print("esto es lo que llevo de mensaje: ", array_mensaje)
        ## --------------------------------------------------------------

        try:
            desencripando = codificacion.desencriptar(array_mensaje)
            leible = pickle.loads(desencripando)
        except IndexError:
            raise ConnectionError
        #print(leible)
        return leible

    def enviar(self, mensaje, socket_cliente):
        try:
            ## Lo serializaremos con PICKLE
            msg_bytes = pickle.dumps(mensaje)
            ## Lo encriptamos
            mensaje_encriptado = codificacion.encriptacion(msg_bytes)
            ## Lo codificamos
            mensaje_codificado = codificacion.codificar(mensaje_encriptado)
            ## Lo enviamos
            socket_cliente.sendall(mensaje_codificado)
            pass
        except ConnectionError:
            socket_cliente.close()


    def eliminar_cliente(self, id_cliente):
        
        with self.clientes_conectados_lock:
            #Tenemos que obtener el socket del cliente
            socket_cliente = self.clientes_conectados[id_cliente]
            #Cerramos el socket
            socket_cliente.close()
            #Borramos la entrada del diccionario
            del self.clientes_conectados[id_cliente]

    def cerrar_servidor(self):
        for id_cliente in list(self.clientes_conectados.keys()):
            self.eliminar_cliente(id_cliente)
        self.socket_servidor.close()

    def log(self, mensaje: str):
        """
        Imprime un mensaje en consola
        """
        print("|" + mensaje.center(80, " ") + "|")