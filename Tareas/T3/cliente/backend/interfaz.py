"""
Ventana principal del cliente que se encarga de funcionar como backend de la
mayoria de ventanas, de conectar señales y de procesar los mensajes recibidos
por el cliente
"""
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from backend.logica_juego import LogicaJuego
from frontend.ventana_final import VentanaFinal
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_espera import VentanaEspera
from frontend.ventana_inicio import VentanaInicio

class Interfaz(QObject):

    senal_mostrar_ventana_espera = pyqtSignal(dict)
    senal_mostrar_ventana_juego = pyqtSignal()
    senal_backend_info_comienzo = pyqtSignal(dict)
    senal_actualizar_turno = pyqtSignal(dict, int, int, str, int, int, int, bool, int, bool, str)
    senal_mostrar_ventana_inicio = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.color = None
        self.ventana_inicio = VentanaInicio()
        self.ventana_espera = VentanaEspera()
        self.ventana_juego = VentanaJuego()
        self.backend_ventana_juego = LogicaJuego()
        self.ventana_final = VentanaFinal()

        self.instanciar_timers()

        self.senal_mostrar_ventana_inicio.connect(self.mostrar_ventana_inicio)
        
        self.ventana_inicio.senal_mandar_nombre_usuario.connect(parent.enviar)
        
        self.senal_mostrar_ventana_espera.connect(self.show_ventana_espera)
        
        self.ventana_espera.senal_comenzar_juego.connect(parent.enviar)
        
        self.senal_mostrar_ventana_juego.connect(self.mostrar_ventana_juego)
        
        self.backend_ventana_juego.senal_enviar_info_comienzo.connect(self.ventana_juego.\
            recibir_info_comienzo)
        
        self.senal_backend_info_comienzo.connect(self.info_backend)

        self.ventana_juego.senal_tirar_dado.connect(self.backend_ventana_juego.tirar_dado)

        self.backend_ventana_juego.senal_enviar_turno_servidor.connect(parent.enviar)

        self.senal_actualizar_turno.connect(self.backend_ventana_juego.turno_jugado)

        self.backend_ventana_juego.senal_actualizar_labels_turno.connect(self.ventana_juego\
            .actualizar_labels)

        self.ventana_juego.senal_actualizar_posiciones.connect(self.backend_ventana_juego\
            .actualizar_posiciones)

        self.backend_ventana_juego.senal_terminar_juego.connect(self.post_juego)

        self.ventana_final.senal_cerrar_sesion.connect(parent.enviar)

    def mostrar_ventana_inicio(self):
        self.ventana_inicio.mostrar_ventana()

    def show_ventana_espera(self, mensaje):
        self.ventana_inicio.esconder_ventana()
        self.ventana_espera.actualizar_labels(mensaje)
        self.ventana_espera.mostrar_ventana(mensaje)

    def mostrar_ventana_juego(self):
        self.ventana_espera.esconder_ventana()
        self.ventana_juego.mostrar_ventana()

    def info_backend(self, mensaje):
        self.backend_ventana_juego.info_comienzo_de_partida(mensaje)

    def post_juego(self, labels, ganador):
        self.ventana_juego.boton_dado.setDisabled(True)
        self.timer_esperar_ganador.start()
        self.labels = labels
        self.ganador = ganador

    def post_juego2(self):
        self.timer_esperar_ganador.stop()
        self.ventana_juego.esconder_ventana()
        self.ventana_final.actualizar_labels(self.labels, self.ganador, self.id)
        self.ventana_final.mostrar_ventana()

    def instanciar_timers(self):
        ## Este timer lo instancio para que la ventana no se cierre inmediatamente y se alcance
        ## a distinguir quien es el ganador de la partida
        self.timer_esperar_ganador = QTimer()
        self.timer_esperar_ganador.setInterval(2000)
        self.timer_esperar_ganador.timeout.connect(self.post_juego2)

    def manejar_mensaje(self, mensaje):
        """
        Maneja un mensaje recibido desde el servidor.
        Genera la respuesta y los cambios en la interfaz correspondientes.

        Argumentos:
            mensaje (dict): Mensaje ya decodificado recibido desde el servidor
        """
        try:
            comando = mensaje["comando"]
            if comando == "ingreso exitoso":
                if self.ventana_espera.isVisible():
                    self.ventana_espera.actualizar_labels(mensaje)
                else:
                    self.id = mensaje["id"]
                    self.nombre_usuario = mensaje["nombre usuario"]
                    self.host = mensaje["host"]
                    self.color = mensaje["color asignado"]
                    self.turno = mensaje["turno_asignado"]
                    self.usuarios_activos = mensaje["usuarios"]
                    self.senal_mostrar_ventana_espera.emit(mensaje)

            elif comando == "ingreso fallido":
                self.ventana_inicio.recibir_feedback(mensaje)

            elif comando == "comenzar_partida":
                mensaje["color_usuario"] = self.color
                mensaje["nombre_usuario"] = self.nombre_usuario
                mensaje["id"] = self.id
                mensaje["turno"] = self.turno
                self.usuarios_activos = mensaje["jugadores_que_jugaran"]
                self.senal_backend_info_comienzo.emit(mensaje)
                self.senal_mostrar_ventana_juego.emit()

            elif comando == "actualizacion_turno_server":
                self.senal_actualizar_turno.emit(mensaje["nuevas_posiciones"],
                mensaje["numero_obtenido"], mensaje["turno_actual"], mensaje["siguiente"],
                mensaje["indicador"], mensaje["id_del_que_jugo"], mensaje["fichas_en_victoria"],
                mensaje["comi_a_otro"], mensaje["id_del_que_comi"], mensaje["juego_terminado"],
                mensaje["ganador"])

            elif comando == "mostrar_ventana_inicio":
                self.senal_mostrar_ventana_inicio.emit()

        except KeyError:
            return []

    