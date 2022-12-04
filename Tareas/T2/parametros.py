from random import randint
import os


WIDTH_MIRA = 150
HEIGHT_MIRA = 100
WIDTH_MIRA_PARA_PRECISION = 15
HEIGHT_MIRA_PARA_PRECISION = 10
POS_INICIO_MIRA = (650, 375, WIDTH_MIRA_PARA_PRECISION, HEIGHT_MIRA_PARA_PRECISION)

WIDTH_ALIEN = 71
HEIGHT_ALIEN = 71
WIDTH_ALIEN_PARA_PRECISION = 10
HEIGHT_ALIEN_PARA_PRECISION = 10
MAX_ANCHO = 1229
MAX_ALTO = 679
POS_INICIO_ALIEN = (randint(0, MAX_ANCHO), randint(0, MAX_ALTO), WIDTH_ALIEN, HEIGHT_ALIEN)

POS_INICIO_MIRA_X = 650
POS_INICIO_MIRA_Y = 375


TECLA_ARRIBA = "w"
TECLA_IZQUIERDA = "a"
TECLA_ABAJO = "s"
TECLA_DERECHA = "d"
TECLA_DISPARO = "k"
TECLA_PAUSA = "p"

DURACION_NIVEL_INICIAL = 30
VELOCIDAD_ALIEN = 5
TIEMPO_MOVERSE_ALIEN = 500
ACTUALIZAR_JUEGO = 0
TIEMPO_TERMINATOR_DOG = 2500

PONDERADOR_TUTORIAL = 0.9
PONDERADOR_ENTRENAMIENTO = 0.8
PONDERADOR_INVASION = 0.7

ruta_imagen = os.path.join("Sprites", "Logo", "Logo.png")
ruta_mira = os.path.join("Sprites", "Elementos juego", "Disparador_negro.png")
ruta_mira_disparo = os.path.join("Sprites", "Elementos juego", "Disparador_rojo.png")

ruta_ui_ventana_principal = os.path.join("frontend", "designer", "ventana_principal.ui")
ruta_ui_ventana_juego = os.path.join("frontend", "designer", "ventana_juego.ui")
ruta_ui_ventana_postjuego = os.path.join("frontend", "designer", "ventana_postjuego.ui")
ruta_ui_ventana_ranking = os.path.join("frontend", "designer", "ventana_ranking.ui")

ruta_fondo_luna = os.path.join("Sprites", "Fondos", "Luna.png")
ruta_fondo_jupiter = os.path.join("Sprites", "Fondos", "Jupiter.png")
ruta_fondo_intergalactico = os.path.join("Sprites", "Fondos", "Galaxia.png")

ruta_alien_lunar = os.path.join("Sprites", "Aliens", "Alien1.png")
ruta_alien_lunar_muerto = os.path.join("Sprites", "Aliens", "Alien1_dead.png")
ruta_alien_jupiter = os.path.join("Sprites", "Aliens", "Alien2.png")
ruta_alien_jupiter_muerto = os.path.join("Sprites", "Aliens", "Alien2_dead.png")
ruta_alien_galactico = os.path.join("Sprites", "Aliens", "Alien3.png")
ruta_alien_galactico_muerto = os.path.join("Sprites", "Aliens", "Alien3_dead.png")

ruta_fase_1 = os.path.join("Sprites", "Elementos Juego", "Disparo_f1.png")
ruta_fase_2 = os.path.join("Sprites", "Elementos Juego", "Disparo_f2.png")
ruta_fase_3 = os.path.join("Sprites", "Elementos Juego", "Disparo_f3.png")

ruta_audio_disparo = os.path.join("Sonidos", "disparo.wav")
ruta_audio_risa = os.path.join("Sonidos", "risa_robotica.wav")

ruta_animacion_perro_lunar = os.path.join("Sprites", "Terminator-Dog", "Perro_y_alien1.png")
ruta_animacion_perro_jupiter = os.path.join("Sprites", "Terminator-Dog", "Perro_y_alien2.png")
ruta_animacion_perro_galactico = os.path.join("Sprites", "Terminator-Dog", "Perro_y_alien3.png")

ruta_perro_normal = os.path.join("Sprites", "Terminator-Dog", "Dog1.png")

ruta_puntajes = os.path.join("puntajes.txt")