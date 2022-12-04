from curses.ascii import isalnum
from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, list)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, tupla_respuesta):
        # COMPLETAR
        nombre = tupla_respuesta[0]
        contrasena = tupla_respuesta[1]
        errores = []
        if (nombre.isalnum() == False or len(nombre) > p.MAX_CARACTERES) and contrasena != p.PASSWORD:
            errores.append("Usuario")
            errores.append("Contraseña")
            self.senal_respuesta_validacion(False, errores)
        
        elif nombre.isalnum() == False or len(nombre) > p.MAX_CARACTERES:
            errores.append("Usuario")
            self.senal_respuesta_validacion(False, errores)
        
        elif contrasena != p.PASSWORD:
            errores.append("Contraseña")
            self.senal_respuesta_validacion(False, errores)

        else:
            self.senal_abrir_juego(nombre)
            self.senal_respuesta_validacion(True, errores)
        pass
