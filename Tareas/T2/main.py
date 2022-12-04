import sys

from PyQt5.QtWidgets import QApplication
from backend.logica_juego import Arma, LogicaJuego
from backend.logica_postjuego import LogicaPostJuego
from backend.logica_principal import LogicaPrincipal
from backend.logica_ranking import LogicaRanking

from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_postjuego import VentanaPostJuego
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_ranking import VentanaRanking

if __name__ == "__main__":
    app = QApplication([])
    
    #Instacia de Clases
    ventana_inicio = VentanaInicio()
    ventana_principal = VentanaPrincipal()
    ventana_juego = VentanaJuego()
    ventana_postjuego = VentanaPostJuego()
    ventana_ranking = VentanaRanking()

    #Instancia de la lógica
    arma = Arma()
    logica_principal = LogicaPrincipal()
    logica_juego = LogicaJuego(arma)
    logica_ranking = LogicaRanking()
    logica_postjuego = LogicaPostJuego()

    # Conectamos las señales
    ventana_inicio.senal_abrir_ventana_principal.connect(ventana_principal.mostrar_ventana)

    ventana_inicio.senal_abrir_ventana_ranking.connect(ventana_ranking.mostrar_ventana)

    ventana_principal.senal_enviar_login.connect(logica_principal.comprobar)

    logica_principal.senal_respuesta_validacion.connect(ventana_principal.recibir_validacion)

    logica_principal.senal_abrir_juego.connect(ventana_juego.mostrar_ventana)

    logica_principal.senal_cargar_usuario.connect(ventana_juego.cargar_jugador)

    ventana_juego.senal_mandar_jugador.connect(logica_juego.cargar_jugador)

    ventana_juego.senal_mostrar_mira.connect(logica_juego.mostrar_mira)

    logica_juego.senal_mostrar_mira.connect(ventana_juego.mover_mira)

    ventana_juego.senal_tecla.connect(logica_juego.mover_mira)

    ventana_juego.senal_comenzar_juego.connect(logica_juego.iniciar_juego)

    logica_juego.senal_mira.connect(ventana_juego.mover_mira)

    logica_juego.senal_mostrar_alien.connect(ventana_juego.mostrar_alien)

    logica_juego.senal_aliens.connect(ventana_juego.mover_aliens)

    logica_juego.senal_muerte_alienf1.connect(ventana_juego.muerte_alien_f1)

    ventana_juego.senal_esperaf2.connect(logica_juego.activar_timer_f2)

    logica_juego.senal_muerte_alienf2.connect(ventana_juego.muerte_alien_f2)

    logica_juego.senal_muerte_alienf3.connect(ventana_juego.muerte_alien_f3)

    logica_juego.senal_muerte_alienf4.connect(ventana_juego.muerte_alien_f4)

    logica_juego.senal_cambiar_mira.connect(ventana_juego.cambiar_mira_disparo)

    logica_juego.senal_volver_mira.connect(ventana_juego.volver_mira)

    logica_juego.senal_actualizar_balas.connect(ventana_juego.actualizar_balas)

    ventana_juego.senal_pausar_juego.connect(logica_juego.pausar_juego_timers)

    ventana_juego.senal_continuar_juego.connect(logica_juego.continuar_juego_timers)

    ventana_juego.senal_cargar_puntaje.connect(logica_postjuego.guardar_puntaje)

    ventana_juego.senal_volver_ventana_principal.connect(ventana_principal.mostrar_ventana)

    logica_juego.senal_juego_terminado.connect(ventana_juego.juego_terminado)

    logica_juego.senal_abrir_post_juego.connect(ventana_juego.pasar_post_juego)

    ventana_juego.senal_mostrar_ventana_postjuego.connect(ventana_postjuego.mostrar_ventana)

    ventana_postjuego.senal_abrir_ventana_inicio.connect(ventana_inicio.mostrar_ventana)

    logica_juego.senal_mandar_aliens_ventana.connect(ventana_juego.definir_aliens)

    ventana_postjuego.senal_siguiente_nivel.connect(ventana_juego.mostrar_ventana)

    ventana_postjuego.senal_guardar_puntaje.connect(logica_postjuego.guardar_puntaje)

    ventana_ranking.senal_ordenar_ranking.connect(logica_ranking.ordenar_ranking)

    logica_ranking.senal_ranking_ya_ordenado.connect(ventana_ranking.arreglar_labels)

    ventana_ranking.senal_volver.connect(ventana_inicio.mostrar_ventana)

    logica_juego.senal_actualizar_barra_progreso.connect(ventana_juego.actualizar_barra)

    ventana_juego.senal_cheatcode_balas.connect(logica_juego.cheatcode_balas)

    ventana_juego.senal_cheatcode_nivel.connect(logica_juego.cheatcode_nivel)

    ventana_inicio.show()
    sys.exit(app.exec())
