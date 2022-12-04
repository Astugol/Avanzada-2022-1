from abc import ABC, abstractmethod
from random import randint, random
from parametros import CARISMA_GANAR, EGO_GANAR, FRUSTRACION_GANAR, MAX_ENERGIA_BEBESTIBLE,\
MIN_ENERGIA_BEBESTIBLE, DEUDA_TOTAL, FRUSTRACION_PERDER, CONFIANZA_PERDER, \
    PORCENTAJE_APUESTA_TACANO, BONIFICACION_TACANO, MULTIPLICADOR_BONIFICACION_BEBEDOR,\
        BONIFICACION_SUERTE_CASUAL, MIN_ENERGIA, MAX_ENERGIA, MIN_SUERTE, MAX_SUERTE,\
            MIN_FRUSTRACION, MAX_FRUSTRACION, MIN_EGO, MAX_EGO, MIN_CARISMA, MAX_CARISMA,\
                MIN_CONFIANZA, MAX_CONFIANZA
class Juego:
    def __init__(self, n, e, amin, amax):
        self.nombre = str(n)
        self.esperanza = int(e)
        self.apuesta_minima = int(amin)
        self.apuesta_maxima = int(amax)

    def entregar_resultados(self, jugador, gano):
        if gano == True:
            antes1 = jugador.ego
            antes2 = jugador.carisma
            antes3 = jugador.frustracion
            jugador.ego += EGO_GANAR
            jugador.carisma += CARISMA_GANAR
            jugador.frustracion -= FRUSTRACION_GANAR
            print(f"Ego antes: {antes1}, ego ahora: {jugador.ego}\nCarisma antes: {antes2},\
carisma ahora: {jugador.carisma}\nFrustración antes: {antes3}, frustración ahora: \n\
{jugador.frustracion}")
        elif gano == False:
            antes_1 = jugador.frustracion
            antes_2 = jugador.confianza
            jugador.frustracion += FRUSTRACION_PERDER
            jugador.confianza -= CONFIANZA_PERDER
            print(f"Frustración antes: {antes_1}, frustración ahora: {jugador.frustracion}\n\
Confianza antes: {antes_2}, confianza ahora: {jugador.confianza}")

    def probabilidad_de_ganar(self, apuesta, jugador):
        probabilidad_jugador = jugador.probabilidad_jugador(apuesta, self.nombre)
        if jugador.juego_favorito == self.nombre:
            favorito = 1
        else:
            favorito = 0
        probabilidad_ganar = min(1, probabilidad_jugador - ((apuesta - (favorito * 50 - \
            (self.esperanza * 30)))/10000))
        return probabilidad_ganar

class Jugador(ABC):
    def __init__(self, nombre, energia, suerte, dinero, frustracion, ego, personalidad, carisma, \
        confianza, juego_favorito):
        self.nombre = str(nombre)
        self.energia = int(energia)
        self.suerte = int(suerte)
        self.dinero = int(dinero)
        self.frustracion = int(frustracion)
        self.ego = int(ego)
        self.personalidad = str(personalidad)
        self.juegos_jugados = []
        self.carisma = int(carisma)
        self.confianza = int(confianza)
        self.juego_favorito = str(juego_favorito)
        self.deuda = DEUDA_TOTAL - self.dinero
        self.actualizar_deuda()
        pass

    @property     ### PRIMERA PROPERTY
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, nuevo_valor):
        if int(nuevo_valor) <= MIN_ENERGIA:
            self._energia = MIN_ENERGIA
        elif int(nuevo_valor) >= MAX_ENERGIA:
            self._energia = MAX_ENERGIA
        else:
            self._energia = nuevo_valor

    @property    ### SEGUNDA PROPERTY
    def suerte(self):
        return self._suerte

    @suerte.setter
    def suerte(self, nuevo_valor):
        if int(nuevo_valor) <= MIN_SUERTE:
            self._suerte = MIN_SUERTE
        elif int(nuevo_valor) >= MAX_SUERTE:
            self._suerte = MAX_SUERTE
        else:
            self._suerte = nuevo_valor

    @property    ### TERCERA PROPERTY
    def frustracion(self):
        return self._frustracion

    @frustracion.setter
    def frustracion(self, nuevo_valor):
        if int(nuevo_valor) <= MIN_FRUSTRACION:
            self._frustracion = MIN_FRUSTRACION
        elif int(nuevo_valor) >= MAX_FRUSTRACION:
            self._frustracion = MAX_FRUSTRACION
        else:
            self._frustracion = nuevo_valor

    @property   ### CUARTA PROPERTY
    def ego(self):
        return self._ego

    @ego.setter
    def ego(self, nuevo_valor):
        if int(nuevo_valor) <= MIN_EGO:
            self._ego = MIN_EGO
        elif int(nuevo_valor) >= MAX_EGO:
            self._ego = MAX_EGO
        else:
            self._ego = nuevo_valor

    @property    ### QUINTA PROPERTY
    def carisma(self):
        return self._carisma

    @carisma.setter
    def carisma(self, nuevo_valor):
        if int(nuevo_valor) <= MIN_CARISMA:
            self._carisma = MIN_CARISMA
        elif int(nuevo_valor) >= MAX_CARISMA:
            self._carisma = MAX_CARISMA
        else:
            self._carisma = nuevo_valor

    @property    ### SEXTA PROPERTY
    def confianza(self):
        return self._confianza

    @confianza.setter
    def confianza(self, nuevo_valor):
        if int(nuevo_valor) <= MIN_CONFIANZA:
            self._confianza = MIN_CONFIANZA
        elif int(nuevo_valor) >= MAX_CONFIANZA:
            self._confianza = MAX_CONFIANZA
        else:
            self._confianza = nuevo_valor

    @abstractmethod  ## La defino como abstract ya que todas las personalidades tienen cosas distintas
    def comprar_bebestible(self, bebestible):
        self.comprar = False
        if self.dinero - bebestible.precio >= 0:
            self.dinero -= bebestible.precio
            self.energia += bebestible.consumir()
            self.comprar = True
        else:
            print("\nLo sentimos, no tiene suficiente dinero.\n")
        return self.comprar

    @abstractmethod
    def probabilidad_jugador(self, apuesta, juego_nombre):
        if juego_nombre == self.juego_favorito:
            favorito = 1
        else:
            favorito = 0
        self.probabilidad = min(1, max(0, (self.suerte * 15 - apuesta * 0.4 + self.confianza * 3 * \
            favorito + self.carisma*2) / 1000))
        return self.probabilidad

    @abstractmethod
    def apostar(self, juego, apuesta):
        self.proba = juego.probabilidad_de_ganar(apuesta, self)
        ocurre = random()
        perdida = round((self.ego + self.frustracion) * 0.15)
        self.energia -= perdida 
        self.resultado = bool
        if float(self.proba) > float(ocurre):
            self.dinero += apuesta
            print(f"Felicitaciones! Ganaste {apuesta} pesos!")
            self.resultado = True
        else:
            self.dinero -= apuesta
            print(f"Laurasad, perdiste {apuesta} pesos, te quedan {self.dinero} pesos")
            self.resultado = False
        return self.resultado

    @abstractmethod
    def agregar_juego_jugado(self, juego):
        self.juegos_jugados.append(juego.nombre)

    @abstractmethod
    def actualizar_deuda(self):
        self.deuda = DEUDA_TOTAL - self.dinero

class Ludopata(Jugador):
    def __init__(self, nombre, energia, suerte, dinero, frustracion, ego, personalidad, carisma, \
        confianza, juego_favorito):
        super().__init__(nombre, energia, suerte, dinero, frustracion, ego, personalidad, carisma, \
            confianza, juego_favorito)

    def comprar_bebestible(self, bebestible):
        super().comprar_bebestible(bebestible)
        if self.comprar == True:
            if bebestible.tipo == "Jugo":
                if len(bebestible.nombre) <= 4:
                    self.ego += 4
                elif len(bebestible.nombre) >= 5 and len(bebestible.nombre) <= 7:
                    self.suerte += 7
                elif len(bebestible.nombre) >= 8:
                    self.frustracion -= 10
                    self.ego += 11
                    
            elif bebestible.tipo == "Gaseosa":
                self.frustracion -= 5
                self.ego += 6

            elif bebestible.tipo == "Brebaje mágico":
                self.carisma += 5
                if len(bebestible.nombre) <= 4:
                    self.ego += 4
                elif len(bebestible.nombre) >= 5 and len(bebestible.nombre) <= 7:
                    self.suerte += 7
                elif len(bebestible.nombre) >= 8:
                    self.frustracion -= 10
                    self.ego += 11
                self.frustracion -= 5
                self.ego += 6
            print(f"\nAcabas de consumir {bebestible.nombre}!!\n")
        return self.comprar
    
    def probabilidad_jugador(self, apuesta, juego_nombre):
        super().probabilidad_jugador(apuesta, juego_nombre)
        return self.probabilidad

    def apostar(self, juego, apuesta):
        super().apostar(juego, apuesta)
        return self.resultado

    def ludopatia(self, resultado):
        self.ego += 2
        self.suerte += 3
        if resultado == False:
            self.frustracion += 5
        
    def agregar_juego_jugado(self, juego):
        super().agregar_juego_jugado(juego)

    def actualizar_deuda(self):
        super().actualizar_deuda()

class Tacano(Jugador):
    def __init__(self, n, e, s, d, f, eg, p, ca, co, jf):
        super().__init__(n, e, s, d, f, eg, p, ca, co, jf)
    
    def comprar_bebestible(self, bebestible):
        super().comprar_bebestible(bebestible)
        if self.comprar == True:
            if bebestible.tipo == "Jugo":
                if len(bebestible.nombre) <= 4:
                    self.ego += 4
                elif len(bebestible.nombre) >= 5 and len(bebestible.nombre) <= 7:
                    self.suerte += 7
                elif len(bebestible.nombre) >= 8:
                    self.frustracion -= 10
                    self.ego += 11
                    
            elif bebestible.tipo == "Gaseosa":
                self.frustracion -= 5
                self.ego += 6

            elif bebestible.tipo == "Brebaje mágico":
                self.carisma += 5
                if len(bebestible.nombre) <= 4:
                    self.ego += 4
                elif len(bebestible.nombre) >= 5 and len(bebestible.nombre) <= 7:
                    self.suerte += 7
                elif len(bebestible.nombre) >= 8:
                    self.frustracion -= 10
                    self.ego += 11
                self.frustracion -= 5
                self.ego += 6
            print(f"\nAcabas de consumir {bebestible.nombre}!!\n")
        return self.comprar

    def probabilidad_jugador(self, apuesta, juego_nombre):
        super().probabilidad_jugador(apuesta, juego_nombre)
        return self.probabilidad

    def apostar(self, juego, apuesta):
        super().apostar(juego, apuesta)
        return self.resultado

    def tacano_extremo(self, resultado, apuesta):
        if apuesta < (PORCENTAJE_APUESTA_TACANO) * self.dinero and resultado == True:
            self.dinero += BONIFICACION_TACANO

    def agregar_juego_jugado(self, juego):
        super().agregar_juego_jugado(juego)
    
    def actualizar_deuda(self):
        super().actualizar_deuda()
            
class Bebedor(Jugador):
    def __init__(self, n, e, s, d, f, eg, p, ca, co, jf):
        super().__init__(n, e, s, d, f, eg, p, ca, co, jf)

    def comprar_bebestible(self, bebestible):
        super().comprar_bebestible(bebestible)
        if self.comprar == True:
            if bebestible.tipo == "Jugo":
                if len(bebestible.nombre) <= 4:
                    self.ego += (4 * self.cliente_recurrente())
                elif len(bebestible.nombre) >= 5 and len(bebestible.nombre) <= 7:
                    self.suerte += (7 * self.cliente_recurrente())
                elif len(bebestible.nombre) >= 8:
                    self.frustracion -= (10 * self.cliente_recurrente())
                    self.ego += (11 * self.cliente_recurrente())
                        
            elif bebestible.tipo == "Gaseosa":
                self.frustracion += (5 * self.cliente_recurrente())
                self.ego += (6 * self.cliente_recurrente())

            elif bebestible.tipo == "Brebaje mágico":
                if len(bebestible.nombre) <= 4:
                    self.ego += (4 * self.cliente_recurrente())
                elif len(bebestible.nombre) >= 5 and len(bebestible.nombre) <= 7:
                    self.suerte += (7 * self.cliente_recurrente())
                elif len(bebestible.nombre) >= 8:
                    self.frustracion -= (10 * self.cliente_recurrente())
                    self.ego += (11 * self.cliente_recurrente())
                self.frustracion += (5 * self.cliente_recurrente())
                self.ego += (6 * self.cliente_recurrente())
                self.carisma += (5 * self.cliente_recurrente())
            print(f"\nAcabas de consumir {bebestible.nombre}!!\n")
        return self.comprar
    
    def probabilidad_jugador(self, apuesta, juego_nombre):
        super().probabilidad_jugador(apuesta, juego_nombre)
        return self.probabilidad

    def apostar(self, juego, apuesta):
        super().apostar(juego, apuesta)
        return self.resultado

    def agregar_juego_jugado(self, juego):
        super().agregar_juego_jugado(juego)

    def cliente_recurrente(self):
        return int(MULTIPLICADOR_BONIFICACION_BEBEDOR)

    def actualizar_deuda(self):
        super().actualizar_deuda()

class Casual(Jugador):
    def __init__(self, n, e, s, d, f, eg, p, ca, co, jf):
        super().__init__(n, e, s, d, f, eg, p, ca, co, jf)

    def comprar_bebestible(self, bebestible):
        super().comprar_bebestible(bebestible)
        if self.comprar == True:
            if bebestible.tipo == "Jugo":
                if len(bebestible.nombre) <= 4:
                    self.ego += 4
                elif len(bebestible.nombre) >= 5 and len(bebestible.nombre) <= 7:
                    self.suerte += 7
                elif len(bebestible.nombre) >= 8:
                    self.frustracion -= 10
                    self.ego += 11
                        
            elif bebestible.tipo == "Gaseosa":
                self.frustracion += 5
                self.ego += 6

            elif bebestible.tipo == "Brebaje mágico":
                if len(bebestible.nombre) <= 4:
                    self.ego += 4
                elif len(bebestible.nombre) >= 5 and len(bebestible.nombre) <= 7:
                    self.suerte += 7
                elif len(bebestible.nombre) >= 8:
                    self.frustracion -= 10
                    self.ego += 11
                self.frustracion += 5
                self.ego += 6
                self.carisma += 5
            print(f"\nAcabas de consumir {bebestible.nombre}!!\n")
        return self.comprar
    
    def probabilidad_jugador(self, apuesta, juego_nombre):
        super().probabilidad_jugador(apuesta, juego_nombre)
        return self.probabilidad

    def apostar(self, juego, apuesta):
        super().apostar(juego, apuesta)
        return self.resultado

    def agregar_juego_jugado(self, juego):
        super().agregar_juego_jugado(juego)

    def suerte_principiante(self):
        self.suerte += BONIFICACION_SUERTE_CASUAL

    def actualizar_deuda(self):
        super().actualizar_deuda()

class Bebestible:
    def __init__(self, nombre, tipo, precio):
        self.nombre = str(nombre)
        self.tipo = str(tipo)
        self.precio = int(precio)

    def consumir(self):
        return randint(MIN_ENERGIA_BEBESTIBLE, MAX_ENERGIA_BEBESTIBLE)
