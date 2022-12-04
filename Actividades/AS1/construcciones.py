from abc import ABC, abstractmethod
from ast import arg
from random import choice, randint, random
from unidades import Guerrero, Mago, MagoGuerrero
from parametros import PROB_CRITICO_MURO, PROB_CRITICO_CATAPULTA, \
                       HP_MUROCATAPULTA, PROB_CRITICO_MURO_CATAPULTA, \
                       HP_BARRACAS, HP_MURO, HP_CATAPULTA


# Recuerda que es una clase abstracta
class Estructura(ABC):

    def __init__(self, edad, *args):
        # No modificar
        super().__init__(*args)
        self.edad = str(edad)
        self.asignar_atributos_segun_edad()

    # ---------------
    # Completar los métodos abstractos aquí
    @abstractmethod
    def asignar_atributos_segun_edad(self):
        pass

    @abstractmethod
    def accion(self):
        pass

    @abstractmethod
    def avanzar_edad(self):
        pass
    # ---------------


# Recuerda completar la herencia
class Barracas(Estructura):

    def __init__(self, *args):
        # Completar
        self.hp = HP_BARRACAS
        super().__init__(*args)
        pass

    # ---------------
    # Completar los métodos aquí
    def asignar_atributos_segun_edad(self):
        if self.edad == "Media":
            self.unidades = ["Guerrero", "Mago"]
        elif self.edad == "Moderna":
            self.unidades = ["Guerrero", "Mago", "MagoGuerrero"]
    
    def avanzar_edad(self):
        if self.edad == "Media":
            self.edad = "Moderna"
            self.unidades.append("MagoGuerrero")
        pass

    # ---------------

    def accion(self):
        # No modificar
        elegido = choice(self.unidades)
        suerte = choice((True, False))
        experiencia = choice([1, 2, 3, 4, 5, 6])
        energia = choice([1, 2, 3, 4, 5, 6])
        if elegido == "Guerrero":
            return elegido, Guerrero(suerte, xp=experiencia, stamina=energia)
        elif elegido == "Mago":
            return elegido, Mago(suerte, xp=experiencia, stamina=energia)
        elif elegido == "MagoGuerrero":
            atributos = {"bendito": suerte, "armado": suerte, "xp": experiencia,
                         "stamina": energia}
            return elegido, MagoGuerrero(**atributos)


# Recuerda completar la herencia
class Muro(Estructura):

    def __init__(self, *args):
        # Completar
        self.hp = HP_MURO
        super().__init__(*args)
        pass

    # ---------------
    # Completar los métodos aquí
    def asignar_atributos_segun_edad(self):
        if self.edad == "Media":
            self.reparacion = [20,80]
        elif self.edad == "Moderna":
            self.reparacion = [40,100]

    def accion(self):
        a = int(self.reparacion[0])
        b = int(self.reparacion[1])
        reconstruccion = randint(a, b)
        numero = random()
        if numero < PROB_CRITICO_MURO:
            reconstruccion * 2
        return reconstruccion
        
    def avanzar_edad(self):
        if self.edad == "Media":
            self.edad = "Moderna"
            self.reparacion = [40, 100]
        pass

    # ---------------


# Recuerda completar la herencia
class Catapulta(Estructura):

    def __init__(self, *args):
        # Completar
        self.hp = HP_CATAPULTA
        super().__init__(*args)
        pass

    # ---------------
    # Completar los métodos aquí
    def asignar_atributos_segun_edad(self):
        if self.edad == "Media":
            self.ataque = [40, 100]
        elif self.edad == "Moderna":
            self.ataque = [80, 140]

    def accion(self):
        a = int(self.ataque[0])
        b = int(self.ataque[1])
        ataque = randint(a, b)
        numero = random()
        if numero < PROB_CRITICO_CATAPULTA:
            ataque = ataque * 2
        return ataque

    def avanzar_edad(self):
        if self.edad == "Media":
            self.edad = "Moderna"
            self.ataque = [80, 140]
        pass

    # ---------------


# Recuerda completar la herencia
class MuroCatapulta(Muro, Catapulta):

    def __init__(self, *args):
        # Completar
        self.hp = HP_MUROCATAPULTA
        super().__init__(*args)
        pass

    # ---------------
    # Completar los métodos aquí
    def asignar_atributos_segun_edad(self):
        Muro.asignar_atributos_segun_edad(self)
        Catapulta.asignar_atributos_segun_edad(self)

    def accion(self):
        a1 = int(self.reparacion[0])
        b1 = int(self.reparacion[1])
        a2 = int(self.ataque[0])
        b2 = int(self.ataque[1])
        reparacion = randint(a1, b1)
        ataque = randint(a2, b2)
        numero = random()
        if numero < PROB_CRITICO_MURO_CATAPULTA:
            reparacion = round(reparacion * 2.5)
            ataque = round(ataque * 2.5)
        return reparacion, ataque

    def avanzar_edad(self):
        if self.edad == "Media":
            self.edad = "Moderna"
            self.reparacion = [40, 100]
            self.ataque = [80, 140]
        pass
    # ---------------


if __name__ == "__main__":
    # ---------------
    # En esta sección puedes probar tu codigo
    # ---------------
    pass
