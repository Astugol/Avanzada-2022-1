###    Instanciamos la ventana espera de PYQT   ###
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from os.path import join
from utils import data_json

window_name, base_class = uic.loadUiType(join(*data_json("RUTA_PANTALLA_JUEGO")))

class VentanaJuego(window_name, base_class):

    senal_tirar_dado = pyqtSignal(dict, dict)
    senal_actualizar_posiciones = pyqtSignal(dict, dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.pixeles_azul = QPixmap(data_json("FICHA_AZUL"))
        self.doble_pixeles_azul = QPixmap(data_json("FICHA_AZUL_DOBLE"))
        self.pixeles_rojo = QPixmap(data_json("FICHA_ROJA"))
        self.doble_pixeles_rojo = QPixmap(data_json("FICHA_ROJA_DOBLE"))
        self.pixeles_amarillo = QPixmap(data_json("FICHA_AMARILLA"))
        self.doble_pixeles_amarillo = QPixmap(data_json("FICHA_AMARILLA_DOBLE"))
        self.pixeles_verde = QPixmap(data_json("FICHA_VERDE"))
        self.doble_pixeles_verde = QPixmap(data_json("FICHA_VERDE_DOBLE"))
        self.posiciones_fichas = dict()
        self.posiciones_iniciales_fichas = dict()
        self.posiciones_zona_color_fichas = dict()
        self.posiciones_zona_victoria_fichas = dict()
        self.r = dict()   ### Nos servirá como resumen de la partida
    def init_gui(self):
        self.setWindowTitle("MainWindow")
        self.boton_dado.clicked.connect(self.tirar_dado)

    def mostrar_ventana(self):
        self.show()

    def tirar_dado(self):
        self.senal_tirar_dado.emit(self.posiciones_fichas, self.posiciones_iniciales_fichas)

    def recibir_info_comienzo(self, mensaje):
        info_de_los_jugadores = mensaje["jugadores_que_jugaran"]

        if len(info_de_los_jugadores) == 2:
            self.label_foto3.hide()
            self.label_27.hide()
            self.label_n3.hide()
            self.label_t3.hide()
            self.label_feb3.hide()
            self.label_fec3.hide()
            self.label_fev3.hide()
            self.label_foto4.hide()
            self.label_40.hide()
            self.label_n4.hide()
            self.label_t4.hide()
            self.label_feb4.hide()
            self.label_fec4.hide()
            self.label_fev4.hide()
        elif len(info_de_los_jugadores) == 3:
            self.label_40.hide()
            self.label_n4.hide()
            self.label_t4.hide()
            self.label_feb4.hide()
            self.label_fec4.hide()
            self.label_fev4.hide()
        try:
            for a in range(0, 4):
                jugador = info_de_los_jugadores[a]
                if a == 0:
                    self.label_turno.setText("Jugador de turno: " + jugador[0])
                    self.label_n1.setText(jugador[0])
                    self.label_t1.setText("Turno: " + str(jugador[2]))
                    self.label_feb1.setText("Fichas en base: 2")
                    self.label_fec1.setText("Fichas en color: 0")
                    self.label_fev1.setText("Fichas en victoria: 0")
                    if jugador[1] == "amarillo":
                        self.labelj1_1 = self.label_amarillo1
                        self.labelj1_2 = self.label_amarillo2
                        self.pixeles_j1 = self.pixeles_amarillo
                        self.doble_pixeles_j1 = self.doble_pixeles_amarillo
                        self.label_foto1.setPixmap(self.pixeles_amarillo)
                        self.posiciones_iniciales_fichas[a] = (590, 220)
                        self.posiciones_zona_color_fichas[a] = [(500, 330), (500, 440)]
                        self.posiciones_zona_victoria_fichas[a] = (500, 550)
                        self.posiciones_fichas[a] = [(590, 220), (590, 220)]
                    elif jugador[1] == "azul":
                        self.labelj1_1 = self.label_azul1
                        self.labelj1_2 = self.label_azul2
                        self.pixeles_j1 = self.pixeles_azul
                        self.doble_pixeles_j1 = self.doble_pixeles_azul
                        self.label_foto1.setPixmap(self.pixeles_azul)
                        self.posiciones_iniciales_fichas[a] = (60, 220)
                        self.posiciones_zona_color_fichas[a] = [(170, 320), (280, 320)]
                        self.posiciones_zona_victoria_fichas[a] = (390, 320)
                        self.posiciones_fichas[a] = [(60, 220), (60, 220)] 
                    elif jugador[1] == "verde":
                        self.labelj1_1 = self.label_verde1
                        self.labelj1_2 = self.label_verde2
                        self.pixeles_j1 = self.pixeles_verde
                        self.doble_pixeles_j1 = self.doble_pixeles_verde
                        self.label_foto1.setPixmap(self.pixeles_verde)
                        self.posiciones_iniciales_fichas[a] = (590, 760)
                        self.posiciones_zona_color_fichas[a] = [(480, 660), (370, 660)]
                        self.posiciones_zona_victoria_fichas[a] = (260, 660)
                        self.posiciones_fichas[a] = [(590, 760), (590, 760)]
                    else:
                        self.labelj1_1 = self.label_rojo1
                        self.labelj1_2 = self.label_rojo2
                        self.pixeles_j1 = self.pixeles_rojo
                        self.doble_pixeles_j1 = self.doble_pixeles_rojo
                        self.posiciones_iniciales_fichas[a] = (60, 760)
                        self.posiciones_zona_color_fichas[a] = [(150, 650), (150, 540)]
                        self.posiciones_zona_victoria_fichas[a] = (150, 430)
                        self.posiciones_fichas[a] = [(60, 760), (60, 760)]
                elif a == 1:
                    self.label_n2.setText(jugador[0])
                    self.label_t2.setText("Turno: " + str(jugador[2]))
                    self.label_feb2.setText("Fichas en base: 2")
                    self.label_fec2.setText("Fichas en color: 0")
                    self.label_fev2.setText("Fichas en victoria: 0")
                    if jugador[1] == "rojo":
                        self.labelj2_1 = self.label_rojo1
                        self.labelj2_2 = self.label_rojo2
                        self.pixeles_j2 = self.pixeles_rojo
                        self.doble_pixeles_j2 = self.doble_pixeles_rojo
                        self.label_foto2.setPixmap(self.pixeles_rojo)
                        self.posiciones_iniciales_fichas[a] = (60, 760)
                        self.posiciones_zona_color_fichas[a] = [(150, 650), (150, 540)]
                        self.posiciones_zona_victoria_fichas[a] = (150, 430)
                        self.posiciones_fichas[a] = [(60, 760), (60, 760)]
                    elif jugador[1] == "azul":
                        self.labelj2_1 = self.label_azul1
                        self.labelj2_2 = self.label_azul2
                        self.pixeles_j2 = self.pixeles_azul
                        self.doble_pixeles_j2 = self.doble_pixeles_azul
                        self.label_foto2.setPixmap(self.pixeles_azul)
                        self.posiciones_iniciales_fichas[a] = (60, 220)
                        self.posiciones_zona_color_fichas[a] = [(170, 320), (280, 320)]
                        self.posiciones_zona_victoria_fichas[a] = (390, 320)
                        self.posiciones_fichas[a] = [(60, 220), (60, 220)]
                    elif jugador[1] == "verde":
                        self.labelj2_1 = self.label_verde1
                        self.labelj2_2 = self.label_verde2
                        self.pixeles_j2 = self.pixeles_verde
                        self.doble_pixeles_j2 = self.doble_pixeles_verde
                        self.label_foto2.setPixmap(self.pixeles_verde)
                        self.posiciones_iniciales_fichas[a] = (590, 760)
                        self.posiciones_zona_color_fichas[a] = [(480, 660), (370, 660)]
                        self.posiciones_zona_victoria_fichas[a] = (260, 660)
                        self.posiciones_fichas[a] = [(590, 760), (590, 760)]
                    else:
                        self.labelj2_1 = self.label_amarillo1
                        self.labelj2_2 = self.label_amarillo2
                        self.pixeles_j2 = self.pixeles_amarillo
                        self.doble_pixeles_j2 = self.doble_pixeles_amarillo
                        self.posiciones_iniciales_fichas[a] = (590, 220)
                        self.posiciones_zona_color_fichas[a] = [(500, 330), (500, 440)]
                        self.posiciones_zona_victoria_fichas[a] = (500, 550)
                        self.posiciones_fichas[a] = [(590, 220), (590, 220)]
                elif a == 2:
                    self.label_n3.setText(jugador[0])
                    self.label_t3.setText("Turno: " + str(jugador[2]))
                    self.label_feb3.setText("Fichas en base: 2")
                    self.label_fec3.setText("Fichas en color: 0")
                    self.label_fev3.setText("Fichas en victoria: 0")
                    if jugador[1] == "rojo":
                        self.labelj3_1 = self.label_rojo1
                        self.labelj3_2 = self.label_rojo2
                        self.pixeles_j3 = self.pixeles_rojo
                        self.doble_pixeles_j3 = self.doble_pixeles_rojo
                        self.label_foto3.setPixmap(self.pixeles_rojo)
                        self.posiciones_iniciales_fichas[a] = (60, 760)
                        self.posiciones_zona_color_fichas[a] = [(150, 650), (150, 540)]
                        self.posiciones_zona_victoria_fichas[a] = (150, 430)
                        self.posiciones_fichas[a] = [(60, 760), (60, 760)]
                    elif jugador[1] == "amarillo":
                        self.labelj3_1 = self.label_amarillo1
                        self.labelj3_2 = self.label_amarillo2
                        self.pixeles_j3 = self.pixeles_amarillo
                        self.doble_pixeles_j3 = self.doble_pixeles_amarillo
                        self.label_foto3.setPixmap(self.pixeles_amarillo)
                        self.posiciones_iniciales_fichas[a] = (590, 220)
                        self.posiciones_zona_color_fichas[a] = [(500, 330), (500, 440)]
                        self.posiciones_zona_victoria_fichas[a] = (500, 550)
                        self.posiciones_fichas[a] = [(590, 220), (590, 220)]
                    elif jugador[1] == "verde":
                        self.labelj3_1 = self.label_verde1
                        self.labelj3_2 = self.label_verde2
                        self.pixeles_j3 = self.pixeles_verde
                        self.doble_pixeles_j3 = self.doble_pixeles_verde
                        self.label_foto3.setPixmap(self.pixeles_verde)
                        self.posiciones_iniciales_fichas[a] = (590, 760)
                        self.posiciones_zona_color_fichas[a] = [(480, 660), (370, 660)]
                        self.posiciones_zona_victoria_fichas[a] = (260, 660)
                        self.posiciones_fichas[a] = [(590, 760), (590, 760)]
                    else:
                        self.labelj3_1 = self.label_azul1
                        self.labelj3_2 = self.label_azul2
                        self.pixeles_j3 = self.pixeles_azul
                        self.doble_pixeles_j3 = self.doble_pixeles_azul
                        self.posiciones_iniciales_fichas[a] = (60, 220)
                        self.posiciones_zona_color_fichas[a] = [(170, 320), (280, 320)]
                        self.posiciones_zona_victoria_fichas[a] = (390, 320)
                        self.posiciones_fichas[a] = [(60, 220), (60, 220)]
                elif a == 3:
                    self.label_n4.setText(jugador[0])
                    self.label_t4.setText("Turno: " + str(jugador[2]))
                    self.label_feb4.setText("Fichas en base: 2")
                    self.label_fec4.setText("Fichas en color: 0")
                    self.label_fev4.setText("Fichas en victoria: 0")
                    if jugador[1] == "rojo":
                        self.labelj4_1 = self.label_rojo1
                        self.labelj4_2 = self.label_rojo2
                        self.pixeles_j4 = self.pixeles_rojo
                        self.doble_pixeles_j4 = self.doble_pixeles_rojo
                        self.label_foto4.setPixmap(self.pixeles_rojo)
                        self.posiciones_iniciales_fichas[a] = (60, 760)
                        self.posiciones_zona_color_fichas[a] = [(150, 650), (150, 540)]
                        self.posiciones_zona_victoria_fichas[a] = (150, 430)
                        self.posiciones_fichas[a] = [(60, 760), (60, 760)]
                    elif jugador[1] == "amarillo":
                        self.labelj4_1 = self.label_amarillo1
                        self.labelj4_2 = self.label_amarillo2
                        self.pixeles_j4 = self.pixeles_amarillo
                        self.doble_pixeles_j4 = self.doble_pixeles_amarillo
                        self.label_foto4.setPixmap(self.pixeles_amarillo)
                        self.posiciones_iniciales_fichas[a] = (590, 220)
                        self.posiciones_zona_color_fichas[a] = [(500, 330), (500, 440)]
                        self.posiciones_zona_victoria_fichas[a] = (500, 550)
                        self.posiciones_fichas[a] = [(590, 220), (590, 220)]
                    elif jugador[1] == "azul":
                        self.labelj4_1 = self.label_azul1
                        self.labelj4_2 = self.label_azul2
                        self.pixeles_j4 = self.pixeles_azul
                        self.doble_pixeles_j4 = self.doble_pixeles_azul
                        self.label_foto4.setPixmap(self.pixeles_azul)
                        self.posiciones_iniciales_fichas[a] = (60, 220)
                        self.posiciones_zona_color_fichas[a] = [(170, 320), (280, 320)]
                        self.posiciones_zona_victoria_fichas[a] = (390, 320)
                        self.posiciones_fichas[a] = [(60, 220), (60, 220)]
                    else:
                        self.labelj4_1 = self.label_verde1
                        self.labelj4_2 = self.label_verde2
                        self.pixeles_j4 = self.pixeles_verde
                        self.doble_pixeles_j4 = self.doble_pixeles_verde
                        self.posiciones_iniciales_fichas[a] = (590, 760)
                        self.posiciones_zona_color_fichas[a] = [(480, 660), (370, 660)]
                        self.posiciones_zona_victoria_fichas[a] = (260, 660)
                        self.posiciones_fichas[a] = [(590, 760), (590, 760)]
        except KeyError or IndexError:  ## En el caso de que no hayan 4 jugadores!
            return []
    
    def actualizar_labels(self, posiciones, numero, prox):
        self.label_numero.setText(f"Número obtenido: {numero}")
        self.label_turno.setText(f"Jugador de turno: {prox}")
        try:
            for a in range(0, 4):
                fichas_jugador = posiciones[a]
                if a == 0:
                    self.labelj1_1.setPixmap(self.pixeles_j1)
                    self.labelj1_2.setPixmap(self.pixeles_j1)
                    self.posiciones_fichas[a][0] = (fichas_jugador[0][0], fichas_jugador[0][1])
                    self.posiciones_fichas[a][1] = (fichas_jugador[1][0], fichas_jugador[1][1])
                    self.labelj1_1.move(fichas_jugador[0][0], fichas_jugador[0][1])
                    self.labelj1_2.move(fichas_jugador[1][0], fichas_jugador[1][1])
                    if self.posiciones_fichas[a][0] == self.posiciones_fichas[a][1]:
                        self.labelj1_1.setPixmap(self.doble_pixeles_j1)
                        self.labelj1_2.setPixmap(self.doble_pixeles_j1)
                    
                    if self.posiciones_fichas[a][0] == self.posiciones_zona_victoria_fichas[a]:
                        if self.posiciones_fichas[a][0] == self.posiciones_fichas[a][1]:
                            self.label_fev1.setText("Fichas en victoria: 2")
                        else:
                            self.label_fev1.setText("Fichas en victoria: 1")
                    if self.posiciones_fichas[a][1] == self.posiciones_iniciales_fichas[a]:
                        if self.posiciones_fichas[a][0] == self.posiciones_fichas[a][1]:
                            self.label_feb1.setText("Fichas en base: 2")
                        else:
                            self.label_feb1.setText("Fichas en base: 1")
                    else:
                        self.label_feb1.setText("Fichas en base: 0")
                    if self.posiciones_fichas[a][0] in self.posiciones_zona_color_fichas[a]:
                        contador1 = 1
                    elif self.posiciones_fichas[a][0] not in self.posiciones_zona_color_fichas[a]:
                        contador1 = 0
                    if self.posiciones_fichas[a][1] in self.posiciones_zona_color_fichas[a]:
                        contador2 = 1
                    if self.posiciones_fichas[a][1] not in self.posiciones_zona_color_fichas[a]:
                        contador2 = 0
                    self.label_fec1.setText(f"Fichas en color: {contador1 + contador2}")
                    self.r[a] = [self.label_n1, self.label_feb1, self.label_fec1, self.label_fev1]
                elif a == 1:
                    self.labelj2_1.setPixmap(self.pixeles_j2)
                    self.labelj2_2.setPixmap(self.pixeles_j2)
                    self.posiciones_fichas[a][0] = (fichas_jugador[0][0], fichas_jugador[0][1])
                    self.posiciones_fichas[a][1] = (fichas_jugador[1][0], fichas_jugador[1][1])
                    self.labelj2_1.move(fichas_jugador[0][0], fichas_jugador[0][1])
                    self.labelj2_2.move(fichas_jugador[1][0], fichas_jugador[1][1])
                    if self.posiciones_fichas[a][0] == self.posiciones_fichas[a][1]:
                        self.labelj2_1.setPixmap(self.doble_pixeles_j2)
                        self.labelj2_2.setPixmap(self.doble_pixeles_j2)
                    
                    if self.posiciones_fichas[a][0] == self.posiciones_zona_victoria_fichas[a]:
                        if self.posiciones_fichas[a][0] == self.posiciones_fichas[a][1]:
                            self.label_fev2.setText("Fichas en victoria: 2")
                        else:
                            self.label_fev2.setText("Fichas en victoria: 1")
                    if self.posiciones_fichas[a][1] == self.posiciones_iniciales_fichas[a]:
                        if self.posiciones_fichas[a][0] == self.posiciones_fichas[a][1]:
                            self.label_feb2.setText("Fichas en base: 2")
                        else:
                            self.label_feb2.setText("Fichas en base: 1")
                    else:
                        self.label_feb2.setText("Fichas en base: 0")
                    if self.posiciones_fichas[a][0] in self.posiciones_zona_color_fichas[a]:
                        contador1 = 1
                    elif self.posiciones_fichas[a][0] not in self.posiciones_zona_color_fichas[a]:
                        contador1 = 0
                    if self.posiciones_fichas[a][1] in self.posiciones_zona_color_fichas[a]:
                        contador2 = 1
                    if self.posiciones_fichas[a][1] not in self.posiciones_zona_color_fichas[a]:
                        contador2 = 0
                    self.label_fec2.setText(f"Fichas en color: {contador1 + contador2}")
                    self.r[a] = [self.label_n2, self.label_feb2, self.label_fec2, self.label_fev2]
                elif a == 2:
                    self.labelj3_1.setPixmap(self.pixeles_j3)
                    self.labelj3_2.setPixmap(self.pixeles_j3)
                    self.posiciones_fichas[a][0] = (fichas_jugador[0][0], fichas_jugador[0][1])
                    self.posiciones_fichas[a][1] = (fichas_jugador[1][0], fichas_jugador[1][1])
                    self.labelj3_1.move(fichas_jugador[0][0], fichas_jugador[0][1])
                    self.labelj3_2.move(fichas_jugador[1][0], fichas_jugador[1][1])
                    if self.posiciones_fichas[a][0] == self.posiciones_fichas[a][1]:
                        self.labelj3_1.setPixmap(self.doble_pixeles_j3)
                        self.labelj3_2.setPixmap(self.doble_pixeles_j3)

                    if self.posiciones_fichas[a][0] == self.posiciones_zona_victoria_fichas[a]:
                        if self.posiciones_fichas[a][0] == self.posiciones_fichas[a][1]:
                            self.label_fev3.setText("Fichas en victoria: 2")
                        else:
                            self.label_fev3.setText("Fichas en victoria: 1")
                    if self.posiciones_fichas[a][1] == self.posiciones_iniciales_fichas[a]:
                        if self.posiciones_fichas[a][0] == self.posiciones_fichas[a][1]:
                            self.label_feb3.setText("Fichas en base: 2")
                        else:
                            self.label_feb3.setText("Fichas en base: 1")
                    else:
                        self.label_feb3.setText("Fichas en base: 0")
                    if self.posiciones_fichas[a][0] in self.posiciones_zona_color_fichas[a]:
                        contador1 = 1
                    elif self.posiciones_fichas[a][0] not in self.posiciones_zona_color_fichas[a]:
                        contador1 = 0
                    if self.posiciones_fichas[a][1] in self.posiciones_zona_color_fichas[a]:
                        contador2 = 1
                    if self.posiciones_fichas[a][1] not in self.posiciones_zona_color_fichas[a]:
                        contador2 = 0
                    self.label_fec3.setText(f"Fichas en color: {contador1 + contador2}")
                    self.r[a] = [self.label_n3, self.label_feb3, self.label_fec3, self.label_fev3]
                elif a == 3:
                    self.labelj4_1.setPixmap(self.pixeles_j4)
                    self.labelj4_2.setPixmap(self.pixeles_j4)
                    self.posiciones_fichas[a][0] = (fichas_jugador[0][0], fichas_jugador[0][1])
                    self.posiciones_fichas[a][1] = (fichas_jugador[1][0], fichas_jugador[1][1])
                    self.labelj4_1.move(fichas_jugador[0][0], fichas_jugador[0][1])
                    self.labelj4_2.move(fichas_jugador[1][0], fichas_jugador[1][1])
                    if self.posiciones_fichas[a][0] == self.posiciones_fichas[a][1]:
                        self.labelj4_1.setPixmap(self.doble_pixeles_j4)
                        self.labelj4_2.setPixmap(self.doble_pixeles_j4)

                    if self.posiciones_fichas[a][0] == self.posiciones_zona_victoria_fichas[a]:
                        if self.posiciones_fichas[a][0] == self.posiciones_fichas[a][1]:
                            self.label_fev4.setText("Fichas en victoria: 2")
                        else:
                            self.label_fev4.setText("Fichas en victoria: 1")
                    if self.posiciones_fichas[a][1] == self.posiciones_iniciales_fichas[a]:
                        if self.posiciones_fichas[a][0] == self.posiciones_fichas[a][1]:
                            self.label_feb4.setText("Fichas en base: 2")
                        else:
                            self.label_feb4.setText("Fichas en base: 1")
                    else:
                        self.label_feb4.setText("Fichas en base: 0")
                    if self.posiciones_fichas[a][0] in self.posiciones_zona_color_fichas[a]:
                        contador1 = 1
                    elif self.posiciones_fichas[a][0] not in self.posiciones_zona_color_fichas[a]:
                        contador1 = 0
                    if self.posiciones_fichas[a][1] in self.posiciones_zona_color_fichas[a]:
                        contador2 = 1
                    if self.posiciones_fichas[a][1] not in self.posiciones_zona_color_fichas[a]:
                        contador2 = 0
                    self.label_fec4.setText(f"Fichas en color: {contador1 + contador2}")
                    self.r[a] = [self.label_n4, self.label_feb4, self.label_fec4, self.label_fev4]
                self.senal_actualizar_posiciones.emit(self.posiciones_fichas, self.r)
        except KeyError or IndexError:
            return []

    def esconder_ventana(self):
        self.hide()