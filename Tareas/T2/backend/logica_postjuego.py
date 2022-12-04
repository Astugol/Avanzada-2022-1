from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import parametros as p
from PyQt5.QtCore import QObject

class LogicaPostJuego(QObject):

    def __init__(self):
        super().__init__()

    def guardar_puntaje(self, nombre, puntaje):
        with open(p.ruta_puntajes, "a", encoding = "utf-8") as archivo1:
            archivo1.write(f"\n{nombre},{puntaje}")