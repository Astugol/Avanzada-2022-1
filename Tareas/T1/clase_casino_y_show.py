from parametros import PROBABILIDAD_EVENTO, DINERO_SHOW, ENERGIA_SHOW, FRUSTRACION_SHOW
from random import random
import funciones

class Casino:
    def __init__(self):
        self.jugador = ""
        self.bebestibles = []
        self.juegos = []
        self.jugar()

    def evento_especial(self, jugador, bebestible):
        prob = random()
        if PROBABILIDAD_EVENTO > prob:
            print(f"Evento especial!!!! De regalo un/a {bebestible.nombre}")
            jugador.comprar_bebestible(bebestible)
            self.bebestibles.append(bebestible)
            
        else:
            print("No hubo evento especial :(")
    
    def jugar(self):
        seguir1 = True
        seguir2 = False
        while seguir1 == True:   ## Lo que estoy haciendo aquí es un loop para que siempre escoja una de las opciones disponibles
            funciones.menu_de_inicio()
            primera_decision = input("\nPor favor, seleccione una opción: ")
            if primera_decision != "1" and primera_decision != "X":
                print("\nError, por favor seleccione una de las opciones disponibles\n")
            elif primera_decision == "1":
                seguir2 = True
            elif primera_decision == "X":
                seguir1 = False
                seguir2 = False    
            while seguir2 == True: #Aquí lo que haré será hacer un loop para que el jugador siempre siga en el "juego" a menos que indique lo contrario.
                self.jugador = ""
                self.bebestibles = []
                self.juegos = []
                funciones.opciones_de_jugador()
                segunda_decision = input("\nPor favor, selccione una opción: \n")
                opciones_permitidas1 = funciones.opciones_de_jugador()

                if segunda_decision == "X":
                    seguir1 = False
                    seguir2 = False

                elif segunda_decision.isnumeric() == False:
                    print("Error, seleccione una de las opciones disponibles")

                elif int(segunda_decision) not in opciones_permitidas1:
                    print("Error, seleccione una de las opciones disponibles")
                
                else:
                    jugador = funciones.cargar_jugador(segunda_decision)
                    self.jugador = jugador  ## aquí agrego al jugador en la clase Casino
                    seguir3 = True
                    while seguir3 == True:
                        funciones.menu_principal()
                        tercera_decision = input("\nPor favor, seleccione una opción: ")
                        if tercera_decision not in ["0","1","2","3","4","X"]:
                            print("\nError, por favor seleccione una de las opciones disponibles\n")

                        elif tercera_decision == "X":
                            seguir1 = False
                            seguir2 = False
                            seguir3 = False

                        elif int(tercera_decision) == 1:
                            opciones_permitidas2 = funciones.desplegar_juegos()
                            cuarta_decision = input("\nPor favor, seleccione una opción: ")
                            if cuarta_decision == "X":
                                seguir1 = False
                                seguir2 = False
                                seguir3 = False

                            elif cuarta_decision.isnumeric() == False:
                                print("Error, seleccione una de las opciones disponibles")

                            elif int(cuarta_decision) not in opciones_permitidas2:
                                print("Error, seleccione una de las opciones disponibles")

                            else:
                                juego = funciones.cargar_juego(cuarta_decision)
                                apuesta = int(input("Cantidad que desea apostar: "))
                                if apuesta > jugador.dinero or apuesta > juego.apuesta_maxima or \
                                    apuesta < juego.apuesta_minima:
                                    print("Lo sentimos, no cumple con los requisitos para apostar.")

                                else:
                                    self.juegos.append(juego)  ##Aquí el jugador ya interactúa con el juego, por lo que lo agrego a la lista
                                    if jugador.personalidad == "Ludopata":
                                        resultado = jugador.apostar(juego, apuesta)
                                        jugador.agregar_juego_jugado(juego)
                                        jugador.ludopatia(resultado)
                                        juego.entregar_resultados(jugador, resultado)
                                        bebestible_random = funciones.bebestible_aleatorio()
                                        self.evento_especial(jugador, bebestible_random)

                                    elif jugador.personalidad == "Tacano":
                                        resultado = jugador.apostar(juego, apuesta)
                                        jugador.agregar_juego_jugado(juego)
                                        jugador.tacano_extremo(resultado, apuesta)
                                        juego.entregar_resultados(jugador, resultado)
                                        bebestible_random = funciones.bebestible_aleatorio()
                                        self.evento_especial(jugador, bebestible_random)

                                    elif jugador.personalidad == "Bebedor":
                                        resultado = jugador.apostar(juego, apuesta)
                                        jugador.agregar_juego_jugado(juego)
                                        juego.entregar_resultados(jugador, resultado)
                                        bebestible_random = funciones.bebestible_aleatorio()
                                        self.evento_especial(jugador, bebestible_random)

                                    elif jugador.personalidad == "Casual":
                                        if len(jugador.juegos_jugados) == 1:
                                            jugador.suerte_principiante()
                                        resultado = jugador.apostar(juego, apuesta)
                                        jugador.agregar_juego_jugado(juego)
                                        juego.entregar_resultados(jugador, resultado)
                                        bebestible_random = funciones.bebestible_aleatorio()
                                        self.evento_especial(jugador, bebestible_random)


                        elif int(tercera_decision) == 2:
                            funciones.carta_bebestibles()
                            opciones_permitidas3 = funciones.carta_bebestibles()
                            quinta_decision = input("\nPor favor, seleccione una opción: ")
                            if quinta_decision == "X":
                                seguir1 = False
                                seguir2 = False
                                seguir3 = False

                            elif quinta_decision.isnumeric() == False:
                                print("Error, seleccione una de las opciones disponibles")

                            elif int(quinta_decision) not in opciones_permitidas3:
                                print("Error, seleccione una de las opciones disponibles")

                            else:
                                bebestible = funciones.cargar_bebestible(quinta_decision)
                                compro = jugador.comprar_bebestible(bebestible)
                                if compro == True:
                                    self.bebestibles.append(bebestible)

                        elif int(tercera_decision) == 3:
                            funciones.ver_estado_del_jugador(jugador)
                            sexta_decision = input("\nPor favor, seleccione una opción: ")
                            if sexta_decision == "X":
                                seguir1 = False
                                seguir2 = False
                                seguir3 = False
                            
                            elif sexta_decision == "0":
                                pass

                            else:
                                print("Error, seleccione una de las opciones disponibles")

                        elif int(tercera_decision) == 4:
                            show = Show()
                            show.ver_show(jugador)
                        
                        elif int(tercera_decision) == 0:
                            seguir3 = False
                        
                        elif int(tercera_decision) == "X":
                            seguir1 = False
                            seguir2 = False
                            seguir3 = False
                        
                        else:
                            print("\nError, seleccione una de las opciones disponibles")

                        jugador.actualizar_deuda()

                        if jugador.dinero == 0:
                            print("Lo sentimos, perdiste todo tu dinero :(")
                            seguir1 = False
                            seguir2 = False
                            seguir3 = False
                        elif jugador.deuda <= 0:
                            print("Felicitaciones!!!! Lograste cumplir con la deuda")
                            seguir1 = False
                            seguir2 = False
                            seguir3 = False
                        elif jugador.energia == 0 and jugador.dinero < \
                            funciones.bebestible_mas_barato():
                            print("Lo sentimos, no puede seguir jugando")
                            seguir1 = False
                            seguir2 = False
                            seguir3 = False
                        elif jugador.energia < round((jugador.ego + jugador.frustracion) * 0.15) \
                            and jugador.dinero < funciones.bebestible_mas_barato():
                            print("Lo sentimos, no puede seguir jugando")
                            seguir1 = False
                            seguir2 = False
                            seguir3 = False
                        else:
                            pass
        print("\nNos vemos pronto!")


class Show:
    def __init__(self):
        pass

    def ver_show(self, jugador):
        if jugador.dinero >= DINERO_SHOW:
            energia1 = jugador.energia
            frustracion1 = jugador.frustracion
            jugador.energia += ENERGIA_SHOW
            jugador.frustracion -= FRUSTRACION_SHOW
            print("El show ha comenzado!")
            print(f"Tu energía paso de {energia1} a {jugador.energia}")
            print(f"Tu frustración paso de {frustracion1} a {jugador.frustracion}")
        else:
            print("No tienes suficiente dinero para ver el show :(")