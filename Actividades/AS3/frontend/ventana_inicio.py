from asyncio.windows_events import ERROR_CONNECTION_REFUSED
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton)
import os
from PyQt5.QtGui import QPixmap
import parametros


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()

        # Geometría
        self.setGeometry(600, 200, 500, 500)
        self.setWindowTitle('Ventana de Inicio')
        self.setStyleSheet("background-color: lightblue;")
        self.crear_elementos()

    def crear_elementos(self):
        # CCOMPLETAR
        #Label logo
        self.label_logo = QLabel("jhsjdsjdsnj")
        self.label_logo.setGeometry(100, 50, 300, 200)
        self.label_logo.setMaximumSize(300, 300)
        pixeles = QPixmap(parametros.RUTA_LOGO)
        self.label_logo.setPixmap(pixeles)
        self.label_logo.setScaledContents(True)



        self.label_nombre = QLabel("Ingrese su nombre:")
        self.nombre = QLineEdit("")
        self.label_contrasena = QLabel("Ingrese su contraseña:")
        self.label_contrasena1 = QLineEdit("")
        self.label_contrasena1.setEchoMode(QLineEdit.Password)
        self.boton1 = QPushButton('&Empezar juego!')
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.clicked.connect(self.enviar_login)


        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label_nombre)
        hbox1.addWidget(self.nombre)
    
        hbox1.addWidget(self.label_contrasena)
        hbox1.addWidget(self.label_contrasena1)
        vbox = QVBoxLayout()
        #vbox.addStretch(2)
        vbox.addWidget(self.label_logo)
        vbox.addLayout(hbox1)
        vbox.addWidget(self.boton1)
        self.setLayout(vbox)
       

        pass

    def enviar_login(self):
        # COMPLETAR
        nombre = self.nombre.text()
        contrasena = self.label_contrasena1.text()
        tupla = (nombre, contrasena)
        self.senal_enviar_login.emit(tupla)
        pass

    def recibir_validacion(self, valid, errores):
        # COMPLETAR
        if valid == True:
            self.hide()
            pass
        else:
            if "Usuario" in errores:
                self.nombre.setText("")
                self.nombre.setPlaceholderText("Usuario incorrecto!")
            elif "Contraseña" in errores:
                self.label_contrasena1.setText("")
                self.label_contrasena1.setPlaceholderText("Contraseña incorrecta!")
            elif "Contraseña" in errores and "Usuario" in errores:
                self.nombre.setText("")
                self.nombre.setPlaceholderText("Usuario incorrecto!")
                self.label_contrasena1.setText("")
                self.label_contrasena1.setText("Contraseña incorrecta!")
            pass    


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaInicio()
    ventana.show()
    sys.exit(app.exec_())
