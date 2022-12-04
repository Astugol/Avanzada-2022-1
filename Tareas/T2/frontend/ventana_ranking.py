from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import parametros as p
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect, QUrl

window_name, base_class = uic.loadUiType(p.ruta_ui_ventana_ranking)

class VentanaRanking(window_name, base_class):

    senal_ordenar_ranking = pyqtSignal()
    senal_volver = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("A cazar aliens!")
        self.boton_volver.clicked.connect(self.volver)

    def arreglar_labels(self, nombres, puntajes):

        self.label_2.setText(f"1. {nombres[0]}")
        self.label_3.setText(f"2. {nombres[1]}")
        self.label_4.setText(f"3. {nombres[2]}")
        self.label_5.setText(f"4. {nombres[3]}")
        self.label_6.setText(f"5. {nombres[4]}")

        self.label_7.setText(f"{puntajes[0]} ptos")
        self.label_8.setText(f"{puntajes[1]} ptos")
        self.label_9.setText(f"{puntajes[2]} ptos")
        self.label_10.setText(f"{puntajes[3]} ptos")
        self.label_11.setText(f"{puntajes[4]} ptos")

    def mostrar_ventana(self):
        
        self.senal_ordenar_ranking.emit()
        
        self.show()

    def volver(self):
        self.senal_volver.emit()
        self.close()