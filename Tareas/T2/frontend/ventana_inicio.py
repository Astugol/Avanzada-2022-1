import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap
import parametros as p

class VentanaInicio(QWidget):
    
    senal_abrir_ventana_principal = pyqtSignal()
    senal_abrir_ventana_ranking = pyqtSignal()

    def __init__(self):
        super().__init__()
        
        ## Geometría de la ventana
        self.setGeometry(300, 100, 300, 300)
        self.setWindowTitle("A casar aliens!")
        self.setStyleSheet("background-color: lightblue;")
        self.crear_elementos()

    def crear_elementos(self):
        #Label logo
        self.label_imagen = QLabel(self)
        pixeles = QPixmap(p.ruta_imagen)
        self.label_imagen.setPixmap(pixeles)
        self.label_imagen.setScaledContents(True)

        #hbox para el logo

        hbox0 = QHBoxLayout()
        hbox0.addStretch(3)
        hbox0.addWidget(self.label_imagen)
        hbox0.addStretch(3)

        #boton jugar
        self.boton_jugar = QPushButton("&Jugar", self)
        self.boton_jugar.clicked.connect(self.jugar)

        #hbox para boton

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.boton_jugar)
        hbox1.addStretch(1)

        #boton ranking
        self.boton_ranking = QPushButton("&Ranking", self)
        self.boton_ranking.clicked.connect(self.ver_ranking)

        #hbox para boton

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.boton_ranking)
        hbox2.addStretch(1)

        #creamos una vbox

        vbox = QVBoxLayout()
        #vbox.addWidget(self.label_imagen)
        vbox.addLayout(hbox0)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)

    def mostrar_ventana(self):
        self.show()
    
    def jugar(self):
        self.close()
        self.senal_abrir_ventana_principal.emit()
        pass

    def ver_ranking(self):
        self.close()
        self.senal_abrir_ventana_ranking.emit()
    pass