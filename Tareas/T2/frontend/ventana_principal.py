from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt

import parametros as p


window_name, base_class = uic.loadUiType(p.ruta_ui_ventana_principal)

class VentanaPrincipal(window_name, base_class):

    senal_enviar_login = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("A cazar aliens!")
        self.boton_cazar.clicked.connect(self.iniciar_usuario)

    def mostrar_ventana(self):
        self.label_usuario.clear()
        self.show()

    def iniciar_usuario(self):
        juegos = []
        usuario = self.label_usuario.text()
        juegos.append(self.boton_lunar.isChecked())  
        juegos.append(self.boton_jupiter.isChecked())
        juegos.append(self.boton_intergalactica.isChecked())  
        tupla = (juegos, usuario)
        self.senal_enviar_login.emit(tupla)

    def recibir_validacion(self, valid, errores):
        if valid == True:
            self.close()
        
        else:
            if "Usuario" in errores and "Ambiente" in errores:
                self.label_error.setText("Seleccione un ambiente e \ningrese un nombre de usuario \
valido")
                self.label_error.setAlignment(Qt.AlignCenter)

            elif "Usuario" in errores:
                self.label_error.setText("""Ingrese un nombre de usuario válido""")
            
            elif "Ambiente" in errores:
                self.label_error.setText("""Seleccione un ambiente para continuar""")