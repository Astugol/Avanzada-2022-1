from PyQt5.QtCore import QObject, pyqtSignal

class LogicaJuego(QObject):

    senal_enviar_info_comienzo = pyqtSignal(dict)
    senal_enviar_turno_servidor = pyqtSignal(dict)
    senal_actualizar_labels_turno = pyqtSignal(dict, int, str)
    senal_terminar_juego = pyqtSignal(dict, str)

    def __init__(self):
        super().__init__()

    def info_comienzo_de_partida(self, mensaje):
        self.id = mensaje["id"]
        self.color = mensaje["color_usuario"]
        self.nombre_usuario = mensaje["nombre_usuario"]
        self.turno_actual = mensaje["turno_actual"]
        self.mi_turno = mensaje["turno"]
        self.fichas_en_base = 2
        self.fichas_en_victoria = 0
        self.fichas_en_color = 0
        self.indicador_posicion = 0
        self.zona_victoria1 = False
        self.labels_jugadores = dict()
        if self.color == "rojo":
            self.posiciones_posibles = [(60, 760), (60, 650), (60, 540), (60, 430), (60, 320),
            (170, 220), (280, 220), (390, 220), (500, 220), (590, 330), (590, 440), (590, 550),
            (590, 660), (480, 760), (370, 760), (260, 760), (150, 760), (150, 650), (150, 540),
            (150, 430)]
        elif self.color == "azul":
            self.posiciones_posibles = [(60, 220), (170, 220), (280, 220), (390, 220), (500, 220),
            (590, 330), (590, 440), (590, 550), (590, 660), (480, 760), (370, 760), (260, 760),
            (150, 760), (60, 650), (60, 540), (60, 430), (60, 320), (170, 320), 
            (280, 320), (390, 320)]
        elif self.color == "amarillo":
            self.posiciones_posibles = [(590, 220), (590, 330), (590, 440), (590, 550), (590, 660),
            (480, 760), (370, 760), (260, 760), (150, 760), (60, 650), (60, 540),
            (60, 430), (60, 320), (170, 220), (280, 220), (390, 220), (500, 220), (500, 330),
            (500, 440), (500, 550)]
        elif self.color == "verde":
            self.posiciones_posibles = [(590, 760), (480, 760), (370, 760), (260, 760), (150, 760),
            (60, 650), (60, 540), (60, 430), (60, 320), (170, 220), (280, 220),
            (390, 220), (500, 220), (590, 330), (590, 440), (590, 550), (590, 660), (480, 660),
            (370, 660), (260, 660)]
        self.senal_enviar_info_comienzo.emit(mensaje)

    def tirar_dado(self, posiciones, posiciones_iniciales):
        self.posiciones = posiciones
        if self.mi_turno == self.turno_actual:  ## Nos aseguramos que sea su turno
            ## Estuve a punto de poner aquí el número aleatorio, pero como todo lo tiene que
            ## supervisar el servidor, preferí hacerlo en la misma lógica del servidor
            ## (en casos de un posible hackeo y que la persona quiera avanzar justamente las X
            ## posiciones para avanzar)
            if self.indicador_posicion == 19:
                self.indicador_posicion = 0
                self.zona_victoria1 = False
            mensaje = {"comando" : "ejecutando_turno", "posiciones_jugadores": self.posiciones,
                "id_jugador": self.id, "posiciones_posibles" : self.posiciones_posibles,
                "indicador": self.indicador_posicion, "estoy_zona_victoria1": self.zona_victoria1,
                "nombre": self.nombre_usuario, "fichas_en_victoria": self.fichas_en_victoria,
                "posiciones_iniciales": posiciones_iniciales}
            self.senal_enviar_turno_servidor.emit(mensaje)

    def turno_jugado(self, posiciones, numero, turno_actual, proximo, indicador, id, fichas_vict,
    comi_o_no, id_del_que_comi, juego_terminado, ganador):
        self.turno_actual = turno_actual
        if id == self.id:
            self.indicador_posicion = indicador
            self.fichas_en_victoria = fichas_vict
            if self.indicador_posicion >= 16:
                self.zona_victoria1 = True
        if comi_o_no == True:
            if id_del_que_comi == self.id:
                self.indicador_posicion = 0
        self.senal_actualizar_labels_turno.emit(posiciones, numero, proximo)
        if juego_terminado:
            self.senal_terminar_juego.emit(self.labels_jugadores, ganador)

    def actualizar_posiciones(self, posiciones, labels):
        self.posiciones = posiciones
        self.labels_jugadores = labels
        