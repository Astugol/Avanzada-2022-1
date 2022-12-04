from random import choice
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from random import randint
from backend.clase_alien import Alien
import parametros as p

class Arma(QObject):
    
    senal_mostrar = pyqtSignal()

    def __init__(self, pos_mira = QRect(*p.POS_INICIO_MIRA)):
        super().__init__()
        self.pos_mira = pos_mira
        self.pos_mira_precision = QRect(*p.POS_INICIO_MIRA)
        self.disparo = False
        self.mira_label = QLabel("")
        self.pixeles_mira = QPixmap(p.ruta_mira)
        self.pixeles_disparo = QPixmap(p.ruta_mira_disparo)
        self.mira_label.setPixmap(self.pixeles_mira)
        self.mira_label.setScaledContents(True)
        self.mira_label.resize(p.WIDTH_MIRA, p.HEIGHT_MIRA)
        self.mira_label.move(self.pos_mira.x(), self.pos_mira.y())
        self.balas = int()

    @property
    def balas(self):
        return self._balas

    @balas.setter
    def balas(self, valor):
        if valor <= 0:
            self._balas = 0
        else:
            self._balas = valor

    def mostrar(self):
        self.pos_mira.moveTo(p.POS_INICIO_MIRA_X, p.POS_INICIO_MIRA_Y)    

    def mover(self, dir):
        if dir == "L":
            self.disparo = False
            if self.pos_mira.x() <= -30:
                self.pos_mira_precision.moveTo(-30 + 60, self.pos_mira.y() + 40)
                self.pos_mira.moveTo(-30, self.pos_mira.y())
            else:
                self.pos_mira_precision.moveTo(self.pos_mira.x() - 10 + 60, self.pos_mira.y() + 40)
                self.pos_mira.moveTo(self.pos_mira.x() - 10, self.pos_mira.y())
                
        elif dir == "R":
            self.disparo = False
            if self.pos_mira.x() >= 1185:
                self.pos_mira_precision.moveTo(1185 + 60, self.pos_mira.y() + 40)
                self.pos_mira.moveTo(1185, self.pos_mira.y())
            else:
                self.pos_mira_precision.moveTo(self.pos_mira.x() + 10 + 60, self.pos_mira.y() + 40)
                self.pos_mira.moveTo(self.pos_mira.x() + 10, self.pos_mira.y())

        elif dir == "U":
            self.disparo = False
            if self.pos_mira.y() <= -10:
                self.pos_mira_precision.moveTo(self.pos_mira.x() + 60, -10 + 40)
                self.pos_mira.moveTo(self.pos_mira.x(), -10)
            else: 
                self.pos_mira_precision.moveTo(self.pos_mira.x() + 60, self.pos_mira.y() - 10 + 40)
                self.pos_mira.moveTo(self.pos_mira.x(), self.pos_mira.y() - 10)

        elif dir == "D":
            self.disparo = False
            if self.pos_mira.y() >= 655:
                self.pos_mira_precision.moveTo(self.pos_mira.x() + 60, 655 + 40)
                self.pos_mira.moveTo(self.pos_mira.x(), 655)
            else:
                self.pos_mira_precision.moveTo(self.pos_mira.x() + 60, self.pos_mira.y() + 10 + 40)
                self.pos_mira.moveTo(self.pos_mira.x(), self.pos_mira.y() + 10)          

        elif dir == "K":
            self.disparo = True
            self.balas -= 1