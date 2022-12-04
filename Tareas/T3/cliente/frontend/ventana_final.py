"""
Instanciamos la ventana final de PYQT
"""
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt
from os.path import join
from utils import data_json

window_name, base_class = uic.loadUiType(join(*data_json("RUTA_PANTALLA_FINAL")))

class VentanaFinal(window_name, base_class):

    senal_cerrar_sesion = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("MainWindow")
        self.boton_volver.clicked.connect(self.volver_ventana_inicio)

    def mostrar_ventana(self):
        self.show()

    def esconder_ventana(self):
        self.hide()

    def actualizar_labels(self, labels, ganador, id):
        self.id = id
        if len(labels) == 2:
            self.label_5.hide()
            self.nombre_j3.hide()
            self.label_feb3.hide()
            self.label_fec3.hide()
            self.label_fev3.hide()
            self.label_6.hide()
            self.nombre_j4.hide()
            self.label_feb4.hide()
            self.label_fec4.hide()
            self.label_fev4.hide()
        
        elif len(labels) == 3:
            self.label_6.hide()
            self.nombre_j4.hide()
            self.label_feb4.hide()
            self.label_fec4.hide()
            self.label_fev4.hide()

        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setText(f"EL/LA GANADOR/A ES: {ganador}")

        try:
            labels_1 = labels[0]
            self.nombre_j1.setText(labels_1[0].text())
            self.label_feb1.setText(labels_1[1].text())
            self.label_fec1.setText(labels_1[2].text())
            self.label_fev1.setText(labels_1[3].text())
            labels_2 = labels[1]
            self.nombre_j2.setText(labels_2[0].text())
            self.label_feb2.setText(labels_2[1].text())
            self.label_fec2.setText(labels_2[2].text())
            self.label_fev2.setText(labels_2[3].text())
            labels_3 = labels[2]
            self.nombre_j3.setText(labels_3[0].text())
            self.label_feb3.setText(labels_3[1].text())
            self.label_fec3.setText(labels_3[2].text())
            self.label_fev3.setText(labels_3[3].text())
            labels_4 = labels[3]
            self.nombre_j4.setText(labels_4[0].text())
            self.label_feb4.setText(labels_4[1].text())
            self.label_fec4.setText(labels_4[2].text())
            self.label_fev4.setText(labels_4[3].text())
        except KeyError or IndexError:
            return []

    def volver_ventana_inicio(self):
        self.esconder_ventana()
        diccionario = {"comando": "cerrar_sesion", "id": self.id}
        self.senal_cerrar_sesion.emit(diccionario)
        