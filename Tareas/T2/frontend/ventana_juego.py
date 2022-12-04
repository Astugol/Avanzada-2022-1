from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt, QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from backend.clase_jugador import Jugador
import parametros as p


window_name, base_class = uic.loadUiType(p.ruta_ui_ventana_juego)


class VentanaJuego(window_name, base_class):
    
    senal_tecla = pyqtSignal(str)
    senal_mostrar_mira = pyqtSignal()
    senal_comenzar_juego = pyqtSignal()
    senal_esperaf2 = pyqtSignal()
    senal_pausar_juego = pyqtSignal()
    senal_continuar_juego = pyqtSignal()
    senal_mandar_jugador = pyqtSignal(Jugador)
    senal_mostrar_ventana_postjuego = pyqtSignal(bool, str, Jugador, int, int)
    senal_cargar_puntaje = pyqtSignal(str, int)
    senal_volver_ventana_principal = pyqtSignal()
    senal_cheatcode_balas = pyqtSignal()
    senal_cheatcode_nivel = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.pausa = False
        self.aliens = []
        self.teclas_apretadas = []

    def init_gui(self):
        self.setWindowTitle("A cazar aliens!")
        self.boton_pausa.clicked.connect(self.pausar_juego)
        self.boton_salir.clicked.connect(self.salir_juego)

    def cargar_jugador(self, username, ambiente):
        self.jugador = Jugador(username, ambiente)
        self.senal_mandar_jugador.emit(self.jugador)


    def mostrar_alien(self, label, x, y):
        label.move(x, y)
        label.setParent(self)
        label.setVisible(True)
        pass

    def mostrar_mira(self):
        self.senal_mostrar_mira.emit()

    def mostrar_ventana(self, ambiente):
        
        self.player = QMediaPlayer()
        self.url_disparo = QUrl.fromLocalFile(p.ruta_audio_disparo)
        self.contenido_disparo = QMediaContent(self.url_disparo)
        self.player.setMedia(self.contenido_disparo)

        self.player1 = QMediaPlayer()
        self.url_disparo1 = QUrl.fromLocalFile(p.ruta_audio_risa)
        self.contenido_disparo1 = QMediaContent(self.url_disparo1)
        self.player1.setMedia(self.contenido_disparo1)

        self.label_6.setText(f"{self.jugador.puntaje_acumulado} ptos")

        self.ambiente = ambiente
        
        if ambiente == "Tutorial Lunar":
            pixeles = QPixmap(p.ruta_fondo_luna)
            self.pixeles_animacion_perro = QPixmap(p.ruta_animacion_perro_lunar)
            self.label_fondo.setPixmap(pixeles)
            self.label_fondo.setScaledContents(True)
            self.show()
            self.actualizar_nivel()
            self.mostrar_mira()
            self.senal_comenzar_juego.emit()
        
        elif ambiente == "Entrenamiento en Júpiter":
            pixeles = QPixmap(p.ruta_fondo_jupiter)
            self.pixeles_animacion_perro = QPixmap(p.ruta_animacion_perro_jupiter)
            self.label_fondo.setPixmap(pixeles)
            self.label_fondo.setScaledContents(True)
            self.show()
            self.actualizar_nivel()
            self.mostrar_mira()
            self.senal_comenzar_juego.emit()
        
        elif ambiente == "Invasión Intergaláctica":
            pixeles = QPixmap(p.ruta_fondo_intergalactico)
            self.pixeles_animacion_perro = QPixmap(p.ruta_animacion_perro_galactico)
            self.label_fondo.setPixmap(pixeles)
            self.label_fondo.setScaledContents(True)
            self.show()
            self.actualizar_nivel()
            self.mostrar_mira()
            self.senal_comenzar_juego.emit()
        
        self.label_10.setText(f"{self.jugador.nivel_actual}")
    pass

    def keyPressEvent(self, event):
        if self.pausa == False:
            if event.text().lower() == p.TECLA_ARRIBA:
                self.senal_tecla.emit("U")
            elif event.text().lower() == p.TECLA_ABAJO:
                self.senal_tecla.emit("D")
            elif event.text().lower() == p.TECLA_DERECHA:
                self.senal_tecla.emit("R")
            elif event.text().lower() == p.TECLA_IZQUIERDA:
                self.senal_tecla.emit("L")
            elif event.text().lower() == p.TECLA_DISPARO:
                self.senal_tecla.emit("K")
            elif event.text().lower() == p.TECLA_PAUSA:
                self.pausar_juego()

            self.teclas_apretadas.append(event.text().lower())

            try:
                if self.teclas_apretadas[-1] == "i" and self.teclas_apretadas[-2] == "n" and \
                self.teclas_apretadas[-3] == "v" and self.teclas_apretadas[-4] == "o":
                    self.senal_cheatcode_balas.emit()
                    
                if self.teclas_apretadas[-1] == "a" and self.teclas_apretadas[-2] == "i" and \
                    self.teclas_apretadas[-3] == "c":
                    self.senal_cheatcode_nivel.emit()
            except IndexError:
                pass

        elif self.pausa == True:
            if event.text().lower() == p.TECLA_PAUSA:
                self.pausar_juego()

    def definir_aliens(self, lista_de_aliens):
        for alien in lista_de_aliens:
            self.aliens.append(alien)

    def mover_mira(self, mira):
        mira.mira_label.setParent(self)
        mira.mira_label.setVisible(True)
        mira.mira_label.move(mira.pos_mira.x(),
                                     mira.pos_mira.y())

    def mover_aliens(self, alien):
        alien.alien_label.move(alien.x_actual, alien.y_actual)
        
    def muerte_alien_f1(self, alien):
        alien.alien_label.setPixmap(alien.pixeles_alien_muerto)
        alien.explosion_label.move(alien.alien_label.x(), alien.alien_label.y())
        alien.explosion_label.setPixmap(alien.pixeles_disparof1)
        alien.explosion_label.setParent(self)
        alien.explosion_label.setVisible(True)
        self.senal_esperaf2.emit()

    def muerte_alien_f2(self, alien):
        alien.explosion_label.setPixmap(alien.pixeles_disparof2)

    def muerte_alien_f3(self, alien):
        alien.explosion_label.setPixmap(alien.pixeles_disparof3)

    def muerte_alien_f4(self, alien):
        alien.explosion_label.hide()

    def cambiar_mira_disparo(self, arma):
        arma.mira_label.setPixmap(arma.pixeles_disparo)
        self.player.play()

    def volver_mira(self, arma):
        arma.mira_label.setPixmap(arma.pixeles_mira)

    def actualizar_balas(self, arma):
        numero = arma.balas
        self.label_4.setText(f"X{numero}")

    def actualizar_nivel(self):
        self.label_10.setText(f"{self.jugador.nivel_actual}")

    def pausar_juego(self):

        if self.pausa == False:
            self.senal_pausar_juego.emit()
            self.pausa = True

        elif self.pausa == True:
            self.senal_continuar_juego.emit()
            self.pausa = False

    def juego_terminado(self, resultado):
        
        if resultado == True:
            self.label_11.setText("¡Nivel superado!")
            self.label_9.setPixmap(self.pixeles_animacion_perro)
            self.player1.play()
        
        elif resultado == False:
            self.label_11.setText("Nivel no superado :(")

    def pasar_post_juego(self, resultado, balas, t):
        self.close()
        self.senal_mostrar_ventana_postjuego.emit(resultado, self.ambiente, self.jugador, balas, t)
        self.reiniciar_ventana()

    def reiniciar_ventana(self):
        for alien in self.aliens:
            alien.alien_label.hide()
        self.label_11.setText("")
        pixeles_perro_normal = QPixmap(p.ruta_perro_normal)
        self.label_9.setPixmap(pixeles_perro_normal)

    def salir_juego(self):
        self.senal_cargar_puntaje.emit(self.jugador.nombre, self.jugador.puntaje_acumulado)
        self.senal_volver_ventana_principal.emit() ### en rúbrica dice ventana principal así que lo dejé así
        self.reiniciar_ventana()
        self.close()

    def actualizar_barra(self, porcentaje):
        self.progressBar.setValue(porcentaje)

    