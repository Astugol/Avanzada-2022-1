"""
Este módulo contiene la clase Logica
"""
import random
from threading import Lock
from utils import data_json


class Logica:

    lock_ingreso = Lock()
    lock_jugadores_activos = Lock()

    def __init__(self):

        self.usuarios_activos = dict()
        self.colores_disponibles = ["rojo", "azul", "amarillo", "verde"]
        self.colores_escogidos = []
        pass

    def manejar_mensaje(self, mensaje, id_cliente):
        """
        Maneja un mensaje recibido desde el cliente.
        """
        try:
            comando = mensaje["comando"]
        except KeyError:
            print(f"ERROR: mensaje de cliente {id_cliente} no cumple el formato.")
            return dict()

        respuesta = dict()
        destinatarios = list()
        
        if comando == "ingreso":
            nombre_ingresado = mensaje["name"]
            print(f"Un jugador ingresó el siguiente nombre: {nombre_ingresado}", end = "")
            with self.lock_ingreso:
                if len(self.usuarios_activos) == data_json("CANTIDAD_JUGADORES_PARTIDA"):
                    respuesta = {"comando": "ingreso fallido",
                     "comentario": "Se alcanzó la cantidad máxima de jugadores"}
                    destinatarios = [id_cliente]
                    print(", sin embargo, la sala está llena")

                else:
                    valido, comentario = self.validar_nombre(nombre_ingresado)
                    if valido:
                        with self.lock_jugadores_activos:
                            print(", y cumple con todos los requisitos")
                            
                            respuesta = {"comando": "ingreso exitoso",
                            "nombre usuario": nombre_ingresado, "id": id_cliente}

                            ###Ahora le asignaremos el color aleatoriamente
                            rango = len(self.colores_disponibles)
                            elegido = random.randint(0, rango - 1)
                            color = self.colores_disponibles.pop(elegido)
                            self.colores_escogidos.append(color)
                            respuesta["color asignado"] = color
                            respuesta["colores"] = self.colores_escogidos

                            self.usuarios_activos[id_cliente] = (nombre_ingresado, color, \
                                len(self.usuarios_activos) + 1)  ## Len corresponde al turno
                            destinatarios = [id for id in self.usuarios_activos.keys()]

                            if len(self.usuarios_activos) == 1:
                                respuesta["host"] = True
                            else:
                                respuesta["host"] = False
                            respuesta["turno_asignado"] = len(self.usuarios_activos)
                            respuesta["usuarios"] = self.usuarios_activos
                    else:
                        print(", pero el nombre ingresado no es válido")
                        destinatarios = [id_cliente]
                        respuesta = {"comando": "ingreso fallido", "comentario": comentario}

        elif comando == "comenzar_juego":
            # Hay que avisarle a los jugadores que comenzó la partida
            destinatarios = [id for id in self.usuarios_activos.keys()]
            respuesta["comando"] = "comenzar_partida"
            respuesta["turno_actual"] = 1
            self.turno = 1
            respuesta["jugadores_que_jugaran"] = self.usuarios_activos
            print("Se ha comenzado una nueva partida")
            print("-------------------------------------------------------------------------------")

        elif comando == "ejecutando_turno":
            # Hay que avisarle a todos los jugadores los cambios que se realicen
            destinatarios = [id for id in self.usuarios_activos.keys()]
            nombre = mensaje["nombre"]
            print(f"Es el turno del cliente con turno 1, que le corresponde a {nombre}")
            """fichas_misma_posicion = False"""
            numero_aleatorio = random.randint(1, 3)
            jugador = mensaje["id_jugador"]
            fichas = mensaje["posiciones_jugadores"]
            fichas_en_victoria = mensaje["fichas_en_victoria"]
            zona_victoria1 = mensaje["estoy_zona_victoria1"]
            #print("Turno de ", jugador)
            fichas_jugador = fichas[jugador]
            #print("Fichas de todos: ", fichas)
            #print("Fichas de jugador: ", fichas_jugador)
            posiciones_posibles = mensaje["posiciones_posibles"]
            indicador = int(mensaje["indicador"])

            posiciones_iniciales = mensaje["posiciones_iniciales"]
            comi_a_otro = False
            id_del_que_comi = int()

            termino = False
            ganador = ""
            
            if fichas_en_victoria == 0:
                if zona_victoria1 == False: #Ocuparemos la primera ficha
                    if numero_aleatorio == 1:
                        indicador += 1
                        posicion_nueva = posiciones_posibles[indicador]
                        fichas_jugador[0] = posicion_nueva
                    elif numero_aleatorio == 2:
                        indicador += 2
                        posicion_nueva = posiciones_posibles[indicador]
                        fichas_jugador[0] = posicion_nueva
                    elif numero_aleatorio == 3:
                        indicador += 3
                        posicion_nueva = posiciones_posibles[indicador]
                        fichas_jugador[0] = posicion_nueva
                    print(f"El jugador {jugador} avanzó {numero_aleatorio} posiciones")
                    

                    for a in range(0, len(self.usuarios_activos)):
                        if a == jugador:
                            continue
                        fichas_jugador_a_ver = fichas[a]
                        for b in range(0, 2):
                            ficha = fichas_jugador_a_ver[b]
                            if fichas_jugador[0] == ficha:
                                comi_a_otro = True
                                id_del_que_comi = a
                                fichas[a][b] = posiciones_iniciales[a]
                                print(f"El jugador {nombre} ha comido una ficha al jugador\
                                    {self.usuarios_activos[id_del_que_comi][0]}")


                else:
                    numero_que_necesita = 19 - indicador
                    if numero_aleatorio < numero_que_necesita:
                        indicador += numero_aleatorio
                        posicion_nueva = posiciones_posibles[indicador]
                        fichas_jugador[0] = posicion_nueva
                        print(f"El jugador {jugador} avanzó {numero_aleatorio} posiciones")

                    elif numero_aleatorio == numero_que_necesita:
                        indicador += numero_aleatorio
                        posicion_nueva = posiciones_posibles[indicador]
                        fichas_jugador[0] = posicion_nueva
                        fichas_en_victoria += 1
                        print(f"El jugador {jugador} avanzó {numero_aleatorio} posiciones")
                        print(f"¡Justo en el blanco! {nombre} puso la ficha en la zona de victoria")

            elif fichas_en_victoria == 1:
                if zona_victoria1 == False: #Ocuparemos la segunda ficha
                    if numero_aleatorio == 1:
                        indicador += 1
                        posicion_nueva = posiciones_posibles[indicador]
                        fichas_jugador[1] = posicion_nueva
                    elif numero_aleatorio == 2:
                        indicador += 2
                        posicion_nueva = posiciones_posibles[indicador]
                        fichas_jugador[1] = posicion_nueva
                    elif numero_aleatorio == 3:
                        indicador += 3
                        posicion_nueva = posiciones_posibles[indicador]
                        fichas_jugador[1] = posicion_nueva
                    print(f"El jugador {jugador} avanzó {numero_aleatorio} posiciones")

                    for a in range(0, len(self.usuarios_activos)):
                        if a == jugador:
                            continue
                        fichas_jugador_a_ver = fichas[a]
                        for b in range(0, 2):
                            ficha = fichas_jugador_a_ver[b]
                            if fichas_jugador[1] == ficha:
                                comi_a_otro = True
                                id_del_que_comi = a
                                fichas[a][b] = posiciones_iniciales[a]
                                print(f"El jugador {nombre} ha comido una ficha al jugador\
 {self.usuarios_activos[id_del_que_comi][0]}")

                    
                else:
                    numero_que_necesita = 19 - indicador
                    if numero_aleatorio < numero_que_necesita:
                        indicador += numero_aleatorio
                        posicion_nueva = posiciones_posibles[indicador]
                        fichas_jugador[1] = posicion_nueva
                        print(f"El jugador {jugador} avanzó {numero_aleatorio} posiciones")

                    elif numero_aleatorio == numero_que_necesita:
                        indicador += numero_aleatorio
                        posicion_nueva = posiciones_posibles[indicador]
                        fichas_jugador[1] = posicion_nueva
                        fichas_en_victoria += 1
                        print(f"La posición nueva del jugador {nombre} es: {posicion_nueva}")
                        print(f"El jugador {jugador} avanzó {numero_aleatorio} posiciones")
                        print(f"¡Justo en el blanco! {nombre} puso la ficha en la zona de victoria")
                        print(f"Fin de la partida! El ganador es {nombre}!!")
                        ganador = nombre
                        termino = True
            print("-------------------------------------------------------------------------------")
            fichas[jugador] = fichas_jugador

            if self.turno != len(self.usuarios_activos):
                self.turno += 1
            else:
                self.turno = 1
            ##print("Fichas de todos: ", fichas)
            ##print("Fichas de jugador: ", fichas_jugador)
            respuesta["comando"] = "actualizacion_turno_server"
            respuesta["nuevas_posiciones"] = fichas 
            respuesta["numero_obtenido"] = numero_aleatorio
            respuesta["turno_actual"] = self.turno
            respuesta["siguiente"] = self.usuarios_activos[self.turno - 1][0]
            respuesta["indicador"] = indicador
            respuesta["id_del_que_jugo"] = jugador
            respuesta["fichas_en_victoria"] = fichas_en_victoria
            respuesta["comi_a_otro"] = comi_a_otro
            respuesta["id_del_que_comi"] = id_del_que_comi
            respuesta["juego_terminado"] = termino
            respuesta["ganador"] = ganador
        
        elif comando == "cerrar_sesion":
            destinatarios = [mensaje["id"]]
            respuesta["comando"] = "mostrar_ventana_inicio"
            self.desconectar_usuario(id_cliente)

        return respuesta, destinatarios

    def validar_nombre(self, nombre):
        with self.lock_jugadores_activos:
            nombres_activos = [nombre[0] for nombre in self.usuarios_activos.values()]
            #Revisamos el nombre en los usuarios activos
            if nombre in nombres_activos:
                return False, "Este nombre está ocupado por otro usuario"
            #Revisamos que cumpla con las condiciones de formato
            if len(nombre) < 1 or len(nombre) > 10 or nombre.isalnum() == False:
                return False, "El nombre ingresado no cumple con el formato requerido"
            return True, None

    def desconectar_usuario(self, id_cliente):
        """
        Recibe una id de un cliente desde el servidor y la saca junto a su usuario asociado
        de el diccionario de usuarios activos.
        """
        with self.lock_jugadores_activos:
            try:
                del self.usuarios_activos[id_cliente]
            except KeyError:
                pass
