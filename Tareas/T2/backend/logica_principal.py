from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p

class LogicaPrincipal(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, list)
    senal_abrir_juego = pyqtSignal(str)
    senal_cargar_usuario = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()

    def comprobar(self, tupla_respuesta):
        lista_ambiente = tupla_respuesta[0]
        nombre = tupla_respuesta[1]
        continuar = bool()
        errores = []
        ambiente_escogido = ""

        if (nombre == "" or nombre.isalnum() == False) and (lista_ambiente[0] == False and \
            lista_ambiente[1] == False and lista_ambiente[2] == False):
            
            continuar = False
            errores.append("Usuario")
            errores.append("Ambiente")
            self.senal_respuesta_validacion.emit(continuar, errores)

        elif nombre == "" or nombre.isalnum() == False:
            errores.append("Usuario")
            continuar = False
            self.senal_respuesta_validacion.emit(continuar, errores)

        else:
            if lista_ambiente[0] == True:
                ambiente_escogido = "Tutorial Lunar"
                continuar = True
                self.senal_cargar_usuario.emit(nombre, ambiente_escogido)
                self.senal_abrir_juego.emit(ambiente_escogido)
                self.senal_respuesta_validacion.emit(continuar, errores)

            elif lista_ambiente[1] == True:
                ambiente_escogido = "Entrenamiento en Júpiter"
                continuar = True
                self.senal_cargar_usuario.emit(nombre, ambiente_escogido)
                self.senal_abrir_juego.emit(ambiente_escogido)
                self.senal_respuesta_validacion.emit(continuar, errores)

            elif lista_ambiente[2] == True:
                ambiente_escogido = "Invasión Intergaláctica"
                continuar = True
                self.senal_cargar_usuario.emit(nombre, ambiente_escogido)
                self.senal_abrir_juego.emit(ambiente_escogido)
                self.senal_respuesta_validacion.emit(continuar, errores)
                
            else:
                errores.append("Ambiente")
                self.senal_respuesta_validacion.emit(continuar, errores)
