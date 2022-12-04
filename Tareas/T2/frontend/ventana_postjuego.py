from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import parametros as p
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect, QUrl

window_name, base_class = uic.loadUiType(p.ruta_ui_ventana_postjuego)

class VentanaPostJuego(window_name, base_class):

    senal_abrir_ventana_inicio = pyqtSignal()
    senal_siguiente_nivel = pyqtSignal(str)
    senal_guardar_puntaje = pyqtSignal(str, int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("A cazar aliens!")
        self.boton_salir.clicked.connect(self.salir)
        self.boton_siguiente_nivel.clicked.connect(self.siguiente_nivel)

    def mostrar_ventana(self, resultado, ambiente, jugador, balas, t):
        
        self.jugador = jugador
        self.ambiente = ambiente
        self.label_8.setText(f"{jugador.nivel_actual}")
        self.label_9.setText(f"{balas}")
        self.label_10.setText(f"{t} seg")
        self.label_11.setText(f"{jugador.puntaje_acumulado}")
        self.label_12.setText(f"{jugador.puntaje_nivel}")
        if ambiente == "Tutorial Lunar":
            pixeles = QPixmap(p.ruta_alien_lunar)
        elif ambiente == "Entrenamiento en Júpiter":
            pixeles = QPixmap(p.ruta_alien_jupiter)
        elif ambiente == "Invasión Intergaláctica":
            pixeles = QPixmap(p.ruta_alien_galactico)
        self.label_13.setPixmap(pixeles)
        if resultado == False:
            self.label_7.setText("¡Perdiste! No puedes seguir jugando :(")
            self.label_7.setStyleSheet("background-color: rgb(170, 0, 0);\
                 font: 18px; color: rgb(255, 255, 255)")
            self.boton_siguiente_nivel.setEnabled(False)
        elif resultado == True:
            self.boton_siguiente_nivel.setEnabled(True)
            self.label_7.setText("¡Puedes dominar el siguiente nivel!")
            self.label_7.setStyleSheet("background-color: rgb(0, 170, 0); font: 18px; \
                color: rgb(255, 255, 255)")
            jugador.puntaje_acumulado += jugador.puntaje_nivel
            jugador.nivel_actual += 1
            self.label_11.setText(f"{jugador.puntaje_acumulado}")
        self.show()

    def salir(self):
        self.senal_guardar_puntaje.emit(self.jugador.nombre, self.jugador.puntaje_acumulado)
        self.close()
        self.senal_abrir_ventana_inicio.emit()

    def siguiente_nivel(self):
        self.close()
        self.senal_siguiente_nivel.emit(self.ambiente)
