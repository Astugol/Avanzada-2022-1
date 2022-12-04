from random import choice
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from random import randint
from backend.clase_alien import Alien
from backend.clase_arma import Arma
import parametros as p

class LogicaJuego(QObject):

    senal_mostrar_mira = pyqtSignal(Arma)
    senal_mira = pyqtSignal(Arma)
    senal_aliens = pyqtSignal(Alien)
    senal_mostrar_alien = pyqtSignal(QLabel, int, int)
    senal_muerte_alienf1 = pyqtSignal(Alien)
    senal_muerte_alienf2 = pyqtSignal(Alien)
    senal_muerte_alienf3 = pyqtSignal(Alien)
    senal_muerte_alienf4 = pyqtSignal(Alien)
    senal_cambiar_mira = pyqtSignal(Arma)
    senal_volver_mira = pyqtSignal(Arma)
    senal_actualizar_balas = pyqtSignal(Arma)
    senal_juego_terminado = pyqtSignal(bool)
    senal_abrir_post_juego = pyqtSignal(bool, int, int)
    senal_mandar_aliens_ventana = pyqtSignal(list)
    senal_actualizar_barra_progreso = pyqtSignal(int)

    def __init__(self, arma):
        super().__init__()

        self.arma = arma
        self.aliens = []
        self.aliens_muertos = []
        self.partiendo = True
        self.aliens_asesinados = []
        self.ultimo_alien_listo = False
        self.gano = False
        self.puntaje_parar = False
        self.termino = False

        self.timer_espera_disparo_act = False
        self.timer_espera_fase_2_act = False
        self.timer_espera_fase_3_act = False
        self.timer_espera_fase_4_act = False
        

    def cargar_jugador(self, jugador):

        self.jugador = jugador

    def instanciar_timer(self):

        self.timer_duracion_juego = QTimer()
        self.timer_duracion_juego.setInterval(self.duracion * 1000)
        self.timer_duracion_juego.timeout.connect(self.terminar_juego)

        self.timer_actualizar_juego = QTimer()
        self.timer_actualizar_juego.setInterval(p.ACTUALIZAR_JUEGO)
        self.timer_actualizar_juego.timeout.connect(self.actualizar_juego)

        self.timer_espera_fase_2 = QTimer()
        self.timer_espera_fase_2.setInterval(500)
        self.timer_espera_fase_2.timeout.connect(self.mandar_fase_2)

        self.timer_espera_fase_3 = QTimer()
        self.timer_espera_fase_3.setInterval(500)
        self.timer_espera_fase_3.timeout.connect(self.mandar_fase_3)

        self.timer_espera_fase_4 = QTimer()
        self.timer_espera_fase_4.setInterval(500)
        self.timer_espera_fase_4.timeout.connect(self.mandar_fase_4)

        self.timer_espera_disparo = QTimer()
        self.timer_espera_disparo.setInterval(1000)
        self.timer_espera_disparo.timeout.connect(self.volver_mira_normal)

        self.timer_cargar = QTimer()
        self.timer_cargar.setInterval(1000)
        self.timer_cargar.timeout.connect(self.terminar_juego)

        self.timer_esperar_termino_juego = QTimer()
        self.timer_esperar_termino_juego.setInterval(p.TIEMPO_TERMINATOR_DOG)
        self.timer_esperar_termino_juego.timeout.connect(self.abrir_post_juego)

        self.timer_duracion_juego.start()  ## COMIENZA A CORRER EL TIEMPO DEL JUEGO

    def actualizar_juego(self):
        
        if self.puntaje_parar == False:
            self.senal_actualizar_barra_progreso.emit(( (self.timer_duracion_juego.remainingTime()\
                 / 1000) / self.duracion ) * 100)
        self.senal_actualizar_balas.emit(self.arma)
        self.calcular_puntaje()

        for alien in self.aliens:

            if alien.salir == True:
                self.aliens.remove(alien)

            else:
                self.senal_aliens.emit(alien)

        if len(self.aliens_muertos) == 2:    ## AQUIÍ ESTÁ EL PROBLEMA!!!!
            self.iniciar_juego()
            self.aliens_muertos = []

        if len(self.aliens_asesinados) == int(self.numero_aliens_nivel):
            self.timer_duracion_juego.stop()
            self.puntaje_parar = True
            self.termino = True

            if self.aliens_asesinados[int(self.numero_aliens_nivel) - 1].salir == True:
                self.ultimo_alien_listo = True
                self.gano = True
                self.iniciar_juego()

    def calcular_balas(self):
        self.jugador.alien_matados = 0 ## DECLARAMOS QUE EL JUGADOR ESTÁ COMENZANDO EL NIVEL SIN ALIENS MATADOS
        self.numero_aliens_nivel = self.calcular_aliens()
        self.arma.balas = int(self.numero_aliens_nivel) * 2

    def iniciar_juego(self):

        if self.partiendo == True:
            self.calcular_balas()
            self.calcular_aliens()

        if self.cantidad_aliens > 0:
            self.mostrar_dos_aliens()
            
            if self.partiendo == True:
                self.instanciar_timer()

            self.timer_actualizar_juego.start()
            self.puntaje = 0
            self.arma.mira_label.raise_()
            self.partiendo = False

        elif self.cantidad_aliens == 0 and self.ultimo_alien_listo == True:
            self.timer_cargar.start()
            self.timer_actualizar_juego.stop()

    def calcular_puntaje(self):

        if self.puntaje_parar == False:
            self.tiempo_restante = round(self.timer_duracion_juego.remainingTime() // 1000) 
            self.jugador.puntaje_nivel = int( (len(self.aliens_asesinados) * 100 + \
                (self.arma.balas * 70 + self.tiempo_restante * 30) * self.jugador.nivel_actual) / \
                    self.alien_dificultad )

    def calcular_aliens(self):

        nivel = self.jugador.nivel_actual
        self.cantidad_aliens = int(nivel) * 2
        return self.cantidad_aliens

    def mostrar_dos_aliens(self):

        alien1 = Alien(self.jugador.ambiente)
        alien2 = Alien(self.jugador.ambiente)
        self.alien_dificultad = alien1.ponderador

        if self.jugador.nivel_actual == 1:
            
            if self.partiendo == True:
                self.duracion = int(p.DURACION_NIVEL_INICIAL * alien1.ponderador)
                self.velocidad_guardada = p.VELOCIDAD_ALIEN / alien1.ponderador
                alien1.velocidad_alien = self.velocidad_guardada
                alien2.velocidad_alien = self.velocidad_guardada
                self.jugador.velocidad_anterior = self.velocidad_guardada   ## LE RECORDAMOS AL PROGRAMA LA VELOCIDAD ANTERIOR QUE PODRÍA SER ÚTIL ANTE UN SUPUESTO PRÓXIMO NIVEL
                self.jugador.duracion_nivel_anterior = self.duracion  ## LE RECORDAMOS AL PROGRAMA LA DURACION

        elif self.jugador.nivel_actual > 1:
            
            if self.partiendo == True:
                self.duracion = self.jugador.duracion_nivel_anterior * alien1.ponderador
                self.velocidad_guardada = self.jugador.velocidad_anterior / alien1.ponderador
                alien1.velocidad_alien = self.velocidad_guardada
                alien2.velocidad_alien = self.velocidad_guardada
                self.jugador.velocidad_anterior = self.velocidad_guardada   ## LE RECORDAMOS AL PROGRAMA LA VELOCIDAD
                self.jugador.duracion_nivel_anterior = self.duracion ### LE RECORDAMOS AL PROGRAMA LA 
                
            else:

                alien1.velocidad_alien = self.velocidad_guardada
                alien2.velocidad_alien = self.velocidad_guardada

        

        if alien1.pos_actual.x() != alien2.pos_actual.x() and \
            alien1.pos_actual.y() != alien2.pos_actual.y():

            self.senal_mostrar_alien.emit(alien1.alien_label, alien1._x_actual, alien1._y_actual)
            self.senal_mostrar_alien.emit(alien2.alien_label, alien2._x_actual, alien2._y_actual)
            self.aliens.append(alien1)
            self.aliens.append(alien2)
            self.senal_mandar_aliens_ventana.emit(self.aliens)
            alien1.start_timer()
            alien2.start_timer()
            self.senal_aliens.emit(alien1)
            self.senal_aliens.emit(alien2)

        else:   #EN CASO DE QUE COMIENCEN EN LA MISMA POSICIÓN
            self.mostrar_dos_aliens()
        


    def mostrar_mira(self):

        self.arma.mostrar()
        self.senal_mostrar_mira.emit(self.arma)

    def mover_mira(self, dir):

        if self.termino == False:

            self.arma.mover(dir)
            self.senal_mira.emit(self.arma)

            for alien in self.aliens:

                if self.arma.disparo == True:

                    self.senal_cambiar_mira.emit(self.arma)
                    self.timer_espera_disparo.start()

                    if self.arma.pos_mira_precision.intersects(alien.pos_actual) \
                        and alien.muerto == False:

                        self.senal_muerte_alienf1.emit(alien)
                        self.aliens_muertos.append(alien)
                        self.cantidad_aliens -= 1
                        alien.muerto = True
                        self.aliens_asesinados.append(alien)

    def activar_timer_f2(self):

        self.timer_espera_fase_2.start()
                
    def mandar_fase_2(self):

        for alien in self.aliens:

            if alien.muerto == True:
                self.senal_muerte_alienf2.emit(alien)

        self.timer_espera_fase_2.stop()
        self.timer_espera_fase_3.start()

    def mandar_fase_3(self):

        for alien in self.aliens:

            if alien.muerto == True:
                self.senal_muerte_alienf3.emit(alien)

        self.timer_espera_fase_3.stop()
        self.timer_espera_fase_4.start()

    def mandar_fase_4(self):

        for alien in self.aliens:

            if alien.muerto == True:

                self.senal_muerte_alienf4.emit(alien)
                alien.termino_explosion = True

        self.timer_espera_fase_4.stop()

    def volver_mira_normal(self):

        self.senal_volver_mira.emit(self.arma)
        self.timer_espera_disparo.stop()

    def pausar_juego_timers(self):

        self.timer_actualizar_juego.stop()
        self.timer_duracion_juego.stop()
        self.timer_duracion_juego.setInterval(self.tiempo_restante * 1000)

        for alien in self.aliens:
            alien.pausa = True
            alien.timer_muerto.stop()

        if self.timer_espera_disparo.isActive() == True:
            self.timer_espera_disparo_act = True
            self.remaining_time_ted = self.timer_espera_disparo.remainingTime()
            self.timer_espera_disparo.stop()

        if self.timer_espera_fase_2.isActive() == True:
            self.timer_espera_fase_2_act = True
            self.remaining_time_tef2 = self.timer_espera_fase_2.remainingTime()
            self.timer_espera_fase_2.stop()

        if self.timer_espera_fase_3.isActive() == True:
            self.timer_espera_fase_3_act = True
            self.remaining_time_tef3 = self.timer_espera_fase_3.remainingTime()
            self.timer_espera_fase_3.stop()

        if self.timer_espera_fase_4.isActive() == True:
            self.timer_espera_fase_4_act = True
            self.remaining_time_tef4 = self.timer_espera_fase_4.remainingTime()
            self.timer_espera_fase_4.stop()

    def continuar_juego_timers(self):

        for alien in self.aliens:
            alien.pausa = False
            alien.start_timer()

        self.timer_actualizar_juego.start()
        self.timer_duracion_juego.start()

        if self.timer_espera_disparo_act == True:
            self.timer_espera_disparo.setInterval(self.remaining_time_ted)
            self.timer_espera_disparo.start()

        if self.timer_espera_fase_2_act == True:
            self.timer_espera_fase_2.setInterval(self.remaining_time_tef2)
            self.timer_espera_fase_2.start()

        if self.timer_espera_fase_3_act == True:
            self.timer_espera_fase_3.setInterval(self.remaining_time_tef3)
            self.timer_espera_fase_3.start()

        if self.timer_espera_fase_4_act == True:
            self.timer_espera_fase_4.setInteral(self.remaining_time_tef4)
            self.timer_espera_fase_4.start()

    def terminar_juego(self):

        self.termino = True
        self.timer_cargar.stop()
        self.timer_actualizar_juego.stop()
        self.timer_duracion_juego.stop()
        self.senal_juego_terminado.emit(self.gano)
        self.timer_esperar_termino_juego.start()

    def abrir_post_juego(self):

        self.senal_abrir_post_juego.emit(self.gano, self.arma.balas, self.tiempo_restante)
        self.timer_esperar_termino_juego.stop()
        self.aliens = []
        self.aliens_muertos = []
        self.partiendo = True
        self.aliens_asesinados = []
        self.ultimo_alien_listo = False
        self.gano = False
        self.puntaje_parar = False
        self.termino = False

    def cheatcode_balas(self):
        self.arma.balas = 99999

    def cheatcode_nivel(self):
        self.gano = True
        self.terminar_juego()