from PyQt5.QtCore import QObject

class Jugador(QObject):

    def __init__(self, nombre, ambiente):
        super().__init__()
        
        self.nombre = nombre
        self.ambiente = ambiente
        self.nivel_actual = int(1)
        self.alien_matados = int(0)
        self.velocidad_anterior = int()
        self.duracion_nivel_anterior = int()
        self.puntaje_acumulado = int()
        self.puntaje_nivel = int()