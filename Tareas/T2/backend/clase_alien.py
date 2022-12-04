from random import choice
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from random import randint
import parametros as p

class Alien(QObject):

    def __init__(self, ambiente):
        super().__init__()
        self.termino_explosion = False
        self.muerto = False
        self.salir = False
        self.pausa = False
        self.tiempo_moverse = p.TIEMPO_MOVERSE_ALIEN
        self.velocidad_alien = int()
        self.mov_en_x = choice([-1,1])
        self.mov_en_y = choice([-1,1])
        self.pos_actual = QRect(*p.POS_INICIO_ALIEN)
        self.pos_actual.moveTo(randint(0, p.MAX_ANCHO), randint(0, p.MAX_ALTO))
        self._x_actual = self.pos_actual.x()
        self._y_actual = self.pos_actual.y()
        self.pixeles_disparof1 = QPixmap(p.ruta_fase_1)
        self.pixeles_disparof2 = QPixmap(p.ruta_fase_2)
        self.pixeles_disparof3 = QPixmap(p.ruta_fase_3)
        self.alien_label = QLabel('')
        self.explosion_label = QLabel('')

        if ambiente == "Tutorial Lunar":
            self.pixeles_alien = QPixmap(p.ruta_alien_lunar)
            self.pixeles_alien_muerto = QPixmap(p.ruta_alien_lunar_muerto)
            self.ponderador = p.PONDERADOR_TUTORIAL
        elif ambiente == "Entrenamiento en Júpiter":
            self.pixeles_alien = QPixmap(p.ruta_alien_jupiter)
            self.pixeles_alien_muerto = QPixmap(p.ruta_alien_jupiter_muerto)
            self.ponderador = p.PONDERADOR_ENTRENAMIENTO
        elif ambiente == "Invasión Intergaláctica":
            self.pixeles_alien = QPixmap(p.ruta_alien_galactico)
            self.pixeles_alien_muerto = QPixmap(p.ruta_alien_galactico_muerto)
            self.ponderador = p.PONDERADOR_INVASION
        
        self.alien_label.setPixmap(self.pixeles_alien)
        self.alien_label.setScaledContents(True)
        self.explosion_label.setScaledContents(True)
        self.alien_label.resize(p.HEIGHT_ALIEN, p.WIDTH_ALIEN)
        self.explosion_label.resize(p.HEIGHT_ALIEN, p.WIDTH_ALIEN)  
        self.alien_label.move(self.pos_actual.x(), self.pos_actual.y())
        self.instanciar_timer()

    @property
    def x_actual(self):
        return self._x_actual

    @x_actual.setter
    def x_actual(self, valor):
        if valor <= 0:
            self._x_actual = 0
        elif valor >= 1230:
            self._x_actual = 1230
        else:
            self._x_actual = valor

    @property
    def y_actual(self):
        return self._y_actual

    @y_actual.setter
    def y_actual(self, valor):
        if valor <= 0:
            self._y_actual = 0
        elif valor >= 680:
            self._y_actual = 680
        else:
            self._y_actual = valor

    def instanciar_timer(self):

        self.timer_vivo = QTimer()
        self.timer_vivo.setSingleShot(True)
        self.timer_vivo.setInterval(self.tiempo_moverse)
        self.timer_vivo.timeout.connect(self.movimiento_aliens)

        self.timer_muerto = QTimer()
        self.timer_muerto.setInterval(100)
        self.timer_muerto.timeout.connect(self.movimiento_aliens)
        
    def start_timer(self):
        self.timer_vivo.start()

    def movimiento_aliens(self):
        if self.muerto == False and self.pausa == False:
            
            self.muerto = False
            
            if self.x_actual <= 0:
                self.mov_en_x = self.mov_en_x * -1
            if self.y_actual <= 0:
                self.mov_en_y = self.mov_en_y * -1
            if self.x_actual >= 1230:
                self.mov_en_x = self.mov_en_x * -1
            if self.y_actual >= 680:
                self.mov_en_y = self.mov_en_y * -1

            self.x_actual += self.velocidad_alien * self.mov_en_x
            self.y_actual += self.velocidad_alien * self.mov_en_y
            self.pos_actual.moveTo(self.x_actual, self.y_actual)
            self.timer_vivo.start()

        elif self.muerto == True and self.pausa == False:
            self.y_actual += 20
            self.timer_vivo.stop()
            self.timer_muerto.start()
            if self.y_actual >= 680:
                self.alien_label.hide()
                if self.termino_explosion == True:
                    self.salir = True
