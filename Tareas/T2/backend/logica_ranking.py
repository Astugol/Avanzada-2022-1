from PyQt5 import uic
from PyQt5.QtGui import QPixmap
#import parametros as p
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect, QUrl
import os

class LogicaRanking(QObject):

    senal_ranking_ya_ordenado = pyqtSignal(list, list)

    def __init__(self):
        super().__init__()

    def ordenar_ranking(self):
        
        nombres_ordenados = []
        puntajes_ordenados = []

        nombres = []
        puntajes = []

        with open(os.path.join("puntajes.txt"), "rt", encoding="utf-8") as archivo1:
            lineas1 = archivo1.readlines()
            for linea in lineas1:
                completo = linea.strip().split(",")
                nombres.append(completo[0])
                puntajes.append(int(completo[1]))
        
        for _ in range(5):
            a = max(puntajes)
            posicion = puntajes.index(a)
            nombres_ordenados.append(nombres[posicion])
            puntajes_ordenados.append(puntajes[posicion])
            eliminamos1 = puntajes.pop(posicion)
            eliminamos2 = nombres.pop(posicion)
        
        self.senal_ranking_ya_ordenado.emit(nombres_ordenados, puntajes_ordenados)
