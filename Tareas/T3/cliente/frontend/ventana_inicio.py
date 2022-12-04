"""
Instanciamos la ventana carga de PYQT
"""
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from os.path import join
from utils import data_json

window_name, base_class = uic.loadUiType(join(*data_json("RUTA_PANTALLA_INICIO")))

class VentanaInicio(window_name, base_class):

    senal_mandar_nombre_usuario = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):

        self.setWindowTitle("MainWindow")
        self.boton_jugar.clicked.connect(self.iniciar_usuario)

    def mostrar_ventana(self):
        self.show()

    def esconder_ventana(self):
        self.hide()

    def iniciar_usuario(self):
        usuario = self.nombre_usuario.text()
        dicc_usuario = {"comando" : "ingreso", "name": usuario}
        self.senal_mandar_nombre_usuario.emit(dicc_usuario)
        pass

    def recibir_feedback(self, mensaje):
        coment = mensaje["comentario"]
        self.label_error.setText(coment)

