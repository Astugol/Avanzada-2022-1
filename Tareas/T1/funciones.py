from random import randint
import clases

def menu_de_inicio():
    print("*** Menú de Inicio ***")
    print("----------------------")
    print("[1] Iniciar partida")
    print("[X] Salir")
    pass

def opciones_de_jugador():
    print("   *** Opciones de jugador ***   ")
    print("---------------------------------")
    ayuda_headers = 1
    listado = 0
    lista_opciones_permitidas = ["X"]
    diccionario = {}
    lista_atributos = []
    with open("jugadores.csv", "rt", encoding = "utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        for linea in lineas1:
            completo = linea.strip().split(",")
            if ayuda_headers == 1:
                for atributo in completo:
                    lista_atributos.append(atributo)
            
            elif ayuda_headers != 1:
                for a in range (len(completo)):
                    diccionario[lista_atributos[a]] = completo[a]
                print(f"[{listado}] {diccionario['nombre']}: {diccionario['personalidad']}")
            lista_opciones_permitidas.append(int(listado))
            listado += 1
            ayuda_headers += 1
    print("[0] Volver")
    print("[X] Salir")
    return lista_opciones_permitidas

def cargar_jugador(opcion):
    
    ayuda_headers = 1
    listado = 0
    diccionario = {}
    lista_atributos = []
    with open("jugadores.csv", "rt", encoding = "utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        for linea in lineas1:
            completo = linea.strip().split(",")
            if ayuda_headers == 1:
                for atributo in completo:
                    lista_atributos.append(atributo)
            
            elif ayuda_headers != 1:
                for a in range (len(completo)):
                    diccionario[lista_atributos[a]] = completo[a]
                if int(opcion) == int(listado):
                    if diccionario["personalidad"] == "Ludopata":
                        jugador = clases.Ludopata(diccionario["nombre"], diccionario["energia"],\
                             diccionario["suerte"], diccionario["dinero"], \
                                 diccionario["frustracion"], diccionario["ego"], \
                                     diccionario["personalidad"], diccionario["carisma"], \
                                         diccionario["confianza"], diccionario["juego favorito"])
                    elif diccionario["personalidad"] == "Tacano":
                        jugador = clases.Tacano(diccionario["nombre"], diccionario["energia"],\
                             diccionario["suerte"], diccionario["dinero"], \
                                 diccionario["frustracion"], diccionario["ego"], \
                                     diccionario["personalidad"], diccionario["carisma"], \
                                         diccionario["confianza"], diccionario["juego favorito"])
                    elif diccionario["personalidad"] == "Bebedor":
                        jugador = clases.Bebedor(diccionario["nombre"], diccionario["energia"],\
                             diccionario["suerte"], diccionario["dinero"], \
                                 diccionario["frustracion"], diccionario["ego"], \
                                     diccionario["personalidad"], diccionario["carisma"], \
                                         diccionario["confianza"], diccionario["juego favorito"])
                    elif diccionario["personalidad"] == "Casual":
                        jugador = clases.Casual(diccionario["nombre"], diccionario["energia"],\
                             diccionario["suerte"], diccionario["dinero"], \
                                 diccionario["frustracion"], diccionario["ego"], \
                                     diccionario["personalidad"], diccionario["carisma"], \
                                         diccionario["confianza"], diccionario["juego favorito"])
            listado += 1
            ayuda_headers += 1
    return jugador
                

def menu_principal():
    print("\n   *** Menú Principal ***   ")
    print("----------------------------")
    print("[1] Opciones de Juegos")
    print("[2] Carta de Bebestibles")
    print("[3] Ver estado del Jugador")
    print("[4] Ver Show")
    print("[0] Volver")
    print("[X] Salir")

def desplegar_juegos():
    print("   *** Opciones de Juegos ***   ")
    print("--------------------------------")
    ayuda_headers = 1
    listado = 0
    lista_opciones_permitidas = []
    diccionario = {}
    lista_atributos = []
    with open("juegos.csv", "rt", encoding = "utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        for linea in lineas1:
            completo = linea.strip().split(",")
            if ayuda_headers == 1:
                for atributo in completo:
                    lista_atributos.append(atributo)
            
            elif ayuda_headers != 1:
                for a in range (len(completo)):
                    diccionario[lista_atributos[a]] = completo[a]
                print(f"[{listado}] {diccionario['nombre']}")
            lista_opciones_permitidas.append(int(listado))
            listado += 1
            ayuda_headers += 1
    print("[0] Volver")
    print("[X] Salir")
    return lista_opciones_permitidas

def cargar_juego(opcion):
    ayuda_headers = 1
    listado = 0
    diccionario = {}
    lista_atributos = []
    with open("juegos.csv", "rt", encoding = "utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        for linea in lineas1:
            completo = linea.strip().split(",")
            if ayuda_headers == 1:
                for atributo in completo:
                    lista_atributos.append(atributo)
            
            elif ayuda_headers != 1:
                for a in range (len(completo)):
                    diccionario[lista_atributos[a]] = completo[a]
                if int(opcion) == int(listado):
                    juego = clases.Juego(diccionario['nombre'], diccionario['esperanza'], \
                        diccionario['apuesta minima'], diccionario['apuesta maxima'])
            listado += 1
            ayuda_headers += 1
    return juego

def carta_bebestibles():
    print("\n                   *** Bebestibles ***                   ")
    print("---------------------------------------------------------")
    print("  N°  |      Nombre      |        Tipo        |  Precio  ")
    print("---------------------------------------------------------")
    ayuda_headers = 1
    listado = 0
    lista_opciones_permitidas = []
    diccionario = {}
    lista_atributos = []
    with open("bebestibles.csv", "rt", encoding = "utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        for linea in lineas1:
            completo = linea.strip().split(",")
            if ayuda_headers == 1:
                for atributo in completo:
                    lista_atributos.append(atributo)
            
            elif ayuda_headers != 1:
                for a in range (len(completo)):
                    diccionario[lista_atributos[a]] = completo[a]
                print(f"[{listado: ^4}] {diccionario['nombre']: ^18} {diccionario['tipo']: ^20} \
{diccionario['precio']: ^10}")
            lista_opciones_permitidas.append(int(listado))
            listado += 1
            ayuda_headers += 1
    print("[ 0  ] Volver")
    print("[ X  ] Salir")
    return lista_opciones_permitidas


def cargar_bebestible(opcion):
    ayuda_headers = 1
    listado = 0
    diccionario = {}
    lista_atributos = []
    with open("bebestibles.csv", "rt", encoding = "utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        for linea in lineas1:
            completo = linea.strip().split(",")
            if ayuda_headers == 1:
                for atributo in completo:
                    lista_atributos.append(atributo)
            
            elif ayuda_headers != 1:
                for a in range (len(completo)):
                    diccionario[lista_atributos[a]] = completo[a]
                if int(opcion) == int(listado):
                    bebestible = clases.Bebestible(diccionario['nombre'], diccionario['tipo'], \
                        diccionario['precio'])
            listado += 1
            ayuda_headers += 1
    return bebestible

def ver_estado_del_jugador(jugador):
    jugador.actualizar_deuda()
    print("\n         *** Ver estado del Jugador ***         ")
    print("------------------------------------------------")
    print(f"Nombre: {jugador.nombre}")
    print(f"Personalidad: {jugador.personalidad}")
    print(f"Energía: {jugador.energia}")
    print(f"Suerte: {jugador.suerte}")
    print(f"Dinero: {jugador.dinero}")
    print(f"Frustración: {jugador.frustracion}")
    print(f"Ego: {jugador.ego}")
    print(f"Carisma: {jugador.carisma}")
    print(f"Confianza: {jugador.confianza}")
    print(f"Juego favorito: {jugador.juego_favorito}")
    print(f"Dinero faltante: {jugador.deuda}")
    print(f"[0] Volver")
    print(f"[X] Salir")

def bebestible_mas_barato():
    ayuda_headers = 1
    listado = 0
    diccionario = {}
    lista_atributos = []
    precios = []
    precio_mas_barato = 10000000000000000000000000
    with open("bebestibles.csv", "rt", encoding = "utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        for linea in lineas1:
            completo = linea.strip().split(",")
            if ayuda_headers == 1:
                for atributo in completo:
                    lista_atributos.append(atributo)
            
            elif ayuda_headers != 1:
                for a in range (len(completo)):
                    diccionario[lista_atributos[a]] = completo[a]
                precios.append(int(diccionario["precio"]))
            listado += 1
            ayuda_headers += 1
    for precio in precios:
        if precio < precio_mas_barato:
            precio_mas_barato = precio
    return precio_mas_barato


def bebestible_aleatorio():
    ayuda_headers = 1
    ayuda_numero = 1
    listado = 0
    diccionario = {}
    lista_atributos = []
    with open("bebestibles.csv", "rt", encoding = "utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        numero_aleatorio = randint(2, len(lineas1))
        for linea in lineas1:
            completo = linea.strip().split(",")
            if ayuda_headers == 1:
                for atributo in completo:
                    lista_atributos.append(atributo)
            
            elif ayuda_headers != 1:
                for a in range (len(completo)):
                    diccionario[lista_atributos[a]] = completo[a]
                if numero_aleatorio == ayuda_numero:
                    bebestible = clases.Bebestible(diccionario["nombre"], diccionario["tipo"],\
                        diccionario["precio"])
            listado += 1
            ayuda_headers += 1
            ayuda_numero += 1
    return bebestible
