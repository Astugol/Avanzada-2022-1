"""
Instanciamos la ventana espera de PYQT
"""
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from os.path import join
from utils import data_json

window_name, base_class = uic.loadUiType(join(*data_json("RUTA_PANTALLA_ESPERA")))

class VentanaEspera(window_name, base_class):

    senal_comenzar_juego = pyqtSignal(dict)

    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.pixeles_azul = QPixmap(data_json("FICHA_AZUL"))
        self.pixeles_rojo = QPixmap(data_json("FICHA_ROJA"))
        self.pixeles_amarillo = QPixmap(data_json("FICHA_AMARILLA"))
        self.pixeles_verde = QPixmap(data_json("FICHA_VERDE"))

    def init_gui(self):

        self.setWindowTitle("MainWindow")
        self.boton_iniciar.clicked.connect(self.iniciar_partida)

    def mostrar_ventana(self, mensaje):

        if mensaje["host"] == False:
            if self.boton_iniciar is not None:
                #print("Desactivando boton dado que no es admin!")
                self.boton_iniciar.setDisabled(True)

        elif mensaje["host"] == True:
            self.boton_iniciar.setDisabled(True)
        self.show()

    def esconder_ventana(self):
        self.hide()

    def iniciar_usuario(self):

        usuario = self.nombre_usuario.text()
        dicc_usuario = {"comando" : "ingreso", "name": usuario}
        self.senal_mandar_nombre_usuario.emit(dicc_usuario)
        pass

    def actualizar_labels(self, mensaje):

        lista_usuarios = [usuario[0] for usuario in mensaje["usuarios"].values()]
        if len(lista_usuarios) == 1:
            self.nombre_j1.setText(lista_usuarios[0])
            self.color_j1.setText(mensaje["colores"][0])

            if mensaje["colores"][0] == "azul":
                self.imagen_j1.setPixmap(self.pixeles_azul)
            elif mensaje["colores"][0] == "rojo":
                self.imagen_j1.setPixmap(self.pixeles_rojo)
            elif mensaje["colores"][0] == "verde":
                self.imagen_j1.setPixmap(self.pixeles_verde)
            elif mensaje["colores"][0] == "amarillo":
                self.imagen_j1.setPixmap(self.pixeles_amarillo)

            self.label_4.hide()
            self.nombre_j2.hide()
            self.color_j2.hide()
            self.imagen_j2.hide()
            self.label_5.hide()
            self.nombre_j3.hide()
            self.color_j3.hide()
            self.imagen_j3.hide()
            self.label_6.hide()
            self.nombre_j4.hide()
            self.color_j4.hide()
            self.imagen_j4.hide()

        elif len(lista_usuarios) == 2:

            self.nombre_j1.setText(lista_usuarios[0])
            self.color_j1.setText(mensaje["colores"][0])
            self.nombre_j2.setText(lista_usuarios[1])
            self.color_j2.setText(mensaje["colores"][1])

            if mensaje["colores"][0] == "azul":
                self.imagen_j1.setPixmap(self.pixeles_azul)
            elif mensaje["colores"][0] == "rojo":
                self.imagen_j1.setPixmap(self.pixeles_rojo)
            elif mensaje["colores"][0] == "verde":
                self.imagen_j1.setPixmap(self.pixeles_verde)
            elif mensaje["colores"][0] == "amarillo":
                self.imagen_j1.setPixmap(self.pixeles_amarillo)

            if mensaje["colores"][1] == "azul":
                self.imagen_j2.setPixmap(self.pixeles_azul)
            elif mensaje["colores"][1] == "rojo":
                self.imagen_j2.setPixmap(self.pixeles_rojo)
            elif mensaje["colores"][1] == "verde":
                self.imagen_j2.setPixmap(self.pixeles_verde)
            elif mensaje["colores"][1] == "amarillo":
                self.imagen_j2.setPixmap(self.pixeles_amarillo)

            self.label_4.show()
            self.nombre_j2.show()
            self.color_j2.show()
            self.imagen_j2.show()
            self.label_5.hide()
            self.nombre_j3.hide()
            self.color_j3.hide()
            self.imagen_j3.hide()
            self.label_6.hide()
            self.nombre_j4.hide()
            self.color_j4.hide()
            self.imagen_j4.hide()

        elif len(lista_usuarios) == 3:
            
            self.nombre_j1.setText(lista_usuarios[0])
            self.color_j1.setText(mensaje["colores"][0])
            self.nombre_j2.setText(lista_usuarios[1])
            self.color_j2.setText(mensaje["colores"][1])
            self.nombre_j3.setText(lista_usuarios[2])
            self.color_j3.setText(mensaje["colores"][2])

            if mensaje["colores"][0] == "azul":
                self.imagen_j1.setPixmap(self.pixeles_azul)
            elif mensaje["colores"][0] == "rojo":
                self.imagen_j1.setPixmap(self.pixeles_rojo)
            elif mensaje["colores"][0] == "verde":
                self.imagen_j1.setPixmap(self.pixeles_verde)
            elif mensaje["colores"][0] == "amarillo":
                self.imagen_j1.setPixmap(self.pixeles_amarillo)

            if mensaje["colores"][1] == "azul":
                self.imagen_j2.setPixmap(self.pixeles_azul)
            elif mensaje["colores"][1] == "rojo":
                self.imagen_j2.setPixmap(self.pixeles_rojo)
            elif mensaje["colores"][1] == "verde":
                self.imagen_j2.setPixmap(self.pixeles_verde)
            elif mensaje["colores"][1] == "amarillo":
                self.imagen_j2.setPixmap(self.pixeles_amarillo)

            if mensaje["colores"][2] == "azul":
                self.imagen_j3.setPixmap(self.pixeles_azul)
            elif mensaje["colores"][2] == "rojo":
                self.imagen_j3.setPixmap(self.pixeles_rojo)
            elif mensaje["colores"][2] == "verde":
                self.imagen_j3.setPixmap(self.pixeles_verde)
            elif mensaje["colores"][2] == "amarillo":
                self.imagen_j3.setPixmap(self.pixeles_amarillo)

            self.label_5.show()
            self.nombre_j3.show()
            self.color_j3.show()
            self.imagen_j3.show()
            self.label_6.hide()
            self.nombre_j4.hide()
            self.color_j4.hide()
            self.imagen_j4.hide()

        elif len(lista_usuarios) == 4:

            if mensaje["colores"][0] == "azul":
                self.imagen_j1.setPixmap(self.pixeles_azul)
            elif mensaje["colores"][0] == "rojo":
                self.imagen_j1.setPixmap(self.pixeles_rojo)
            elif mensaje["colores"][0] == "verde":
                self.imagen_j1.setPixmap(self.pixeles_verde)
            elif mensaje["colores"][0] == "amarillo":
                self.imagen_j1.setPixmap(self.pixeles_amarillo)

            if mensaje["colores"][1] == "azul":
                self.imagen_j2.setPixmap(self.pixeles_azul)
            elif mensaje["colores"][1] == "rojo":
                self.imagen_j2.setPixmap(self.pixeles_rojo)
            elif mensaje["colores"][1] == "verde":
                self.imagen_j2.setPixmap(self.pixeles_verde)
            elif mensaje["colores"][1] == "amarillo":
                self.imagen_j2.setPixmap(self.pixeles_amarillo)

            if mensaje["colores"][2] == "azul":
                self.imagen_j3.setPixmap(self.pixeles_azul)
            elif mensaje["colores"][2] == "rojo":
                self.imagen_j3.setPixmap(self.pixeles_rojo)
            elif mensaje["colores"][2] == "verde":
                self.imagen_j3.setPixmap(self.pixeles_verde)
            elif mensaje["colores"][2] == "amarillo":
                self.imagen_j3.setPixmap(self.pixeles_amarillo)

            self.nombre_j1.setText(lista_usuarios[0])
            self.color_j1.setText(mensaje["colores"][0])
            self.nombre_j2.setText(lista_usuarios[1])
            self.color_j2.setText(mensaje["colores"][1])
            self.nombre_j3.setText(lista_usuarios[2])
            self.color_j3.setText(mensaje["colores"][2])
            self.nombre_j4.setText(lista_usuarios[3])
            self.color_j4.setText(mensaje["colores"][3])

            if mensaje["colores"][3] == "azul":
                self.imagen_j4.setPixmap(self.pixeles_azul)
            elif mensaje["colores"][3] == "rojo":
                self.imagen_j4.setPixmap(self.pixeles_rojo)
            elif mensaje["colores"][3] == "verde":
                self.imagen_j4.setPixmap(self.pixeles_verde)
            elif mensaje["colores"][3] == "amarillo":
                self.imagen_j4.setPixmap(self.pixeles_amarillo)

            self.label_6.show()
            self.nombre_j4.show()
            self.color_j4.show()
            self.imagen_j4.show()

        if len(lista_usuarios) >= data_json("MINIMO_JUGADORES") and self.boton_iniciar is not None:
            self.boton_iniciar.setEnabled(True)

        if len(lista_usuarios) == data_json("MAXIMO_JUGADORES"):
            self.iniciar_partida()

    def iniciar_partida(self):
        diccinario_mensaje = dict()
        diccinario_mensaje["comando"] = "comenzar_juego"
        self.senal_comenzar_juego.emit(diccinario_mensaje)