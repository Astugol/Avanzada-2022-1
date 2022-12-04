from parametros import (AFINIDAD_HIT, AFINIDAD_INICIAL, AFINIDAD_PUBLICO_POP,
                        AFINIDAD_STAFF_POP, AFINIDAD_PUBLICO_ROCK,
                        AFINIDAD_STAFF_ROCK, AFINIDAD_PUBLICO_RAP,
                        AFINIDAD_STAFF_RAP, AFINIDAD_PUBLICO_REG,
                        AFINIDAD_STAFF_REG, AFINIDAD_ACCION_POP,
                        AFINIDAD_ACCION_ROCK, AFINIDAD_ACCION_RAP,
                        AFINIDAD_ACCION_REG, AFINIDAD_MIN, AFINIDAD_MAX)


class Artista:
    def __init__(self, nombre, genero, dia_presentacion,
                 hit_del_momento):
        self.nombre = nombre
        self.hit_del_momento = hit_del_momento
        self.genero = genero
        self.dia_presentacion = dia_presentacion
        self._afinidad_con_publico = AFINIDAD_INICIAL
        self._afinidad_con_staff = AFINIDAD_INICIAL
    
    @property
    def afinidad_con_publico(self):
        return self._afinidad_con_publico
    
    @afinidad_con_publico.setter
    def afinidad_con_publico(self, nuevo_valor):
        if nuevo_valor > 100:
            self._afinidad_con_publico = 100
        elif nuevo_valor < 0:
            self._afinidad_con_publico = 0
        else:
            self._afinidad_con_publico = nuevo_valor
        

    @property
    def afinidad_con_staff(self):
        return self._afinidad_con_staff

    @afinidad_con_staff.setter
    def afinidad_con_staff(self, nuevo_valor):
        if nuevo_valor > 100:
            self._afinidad_con_staff = 100
        elif nuevo_valor < 0:
            self._afinidad_con_staff = 0
        else:
            self._afinidad_con_staff = nuevo_valor


    @property
    def animo(self):
        animo1 = self.afinidad_con_publico * 0.5 + self.afinidad_con_staff * 0.5
        # COMPLETAR
        return animo1

    def recibir_suministros(self, suministro):
        if self.afinidad_con_staff + suministro.valor_de_satisfaccion > self.afinidad_con_staff:
            print(f"{self.nombre} recibió un {suministro.nombre} a tiempo!")
            self.afinidad_con_staff += suministro.valor_de_satisfaccion
        elif self.afinidad_con_staff + suministro.valor_de_satisfaccion < self.afinidad_con_staff:
            print(f"{self.nombre} recibió {suministro.nombre} en malas condiciones.")
            self.afinidad_con_staff += suministro.valor_de_satisfaccion         
        # COMPLETAR
        pass

    def cantar_hit(self):
        # COMPLETAR
        self.afinidad_con_publico += AFINIDAD_HIT
        print(f"{self.nombre} está tocando su hit: {self.hit_del_momento}!")
        pass

    def __str__(self):
        return(f"Nombre: {self.nombre}\nGenero: {self.genero}\nAnimo: {self.animo}")
        # COMPLETAR
        pass


class ArtistaPop(Artista):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.accion = "Cambio de vestuario"
        self.afinidad_con_publico = AFINIDAD_PUBLICO_POP
        self.afinidad_con_staff = AFINIDAD_STAFF_POP
        # COMPLETAR
        pass

    def accion_especial(self):
        # COMPLETAR
        print(f"{self.nombre} hará un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_POP
        pass

    @property
    def animo(self):
        # COMPLETAR
        variable = super().animo
        if variable < 10:
            print(f"ArtistaPop peligrando en el concierto. Animo: {self.animo}")
        return variable


class ArtistaRock (Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        super().__init__(*args,**kwargs)
        self.accion = "Solo de guitarra"
        self.afinidad_con_publico = AFINIDAD_PUBLICO_ROCK
        self.afinidad_con_staff = AFINIDAD_STAFF_ROCK
        pass

    def accion_especial(self):
        # COMPLETAR
        print(f"{self.nombre} hará un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_ROCK
        pass

    @property
    def animo(self):
        # COMPLETAR
        variable = super().animo
        if variable < 5:
            print(f"ArtistaRock peligrando en el concierto. Animo: {self.animo}")
        return variable


class ArtistaRap(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        super().__init__(*args,**kwargs)
        self.accion = "Doble tempo"
        self.afinidad_con_publico = AFINIDAD_PUBLICO_RAP
        self.afinidad_con_staff = AFINIDAD_STAFF_RAP
        pass

    def accion_especial(self):
        # COMPLETAR
        print(f"{self.nombre} hará un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_RAP
        pass

    @property
    def animo(self):
        # COMPLETAR
        variable = super().animo
        if variable < 20:
            print(f"ArtistaRap peligrando en el concierto. Animo: {self.animo}")
        return variable


class ArtistaReggaeton(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        super().__init__(*args,**kwargs)
        self.accion = "Perrear"
        self.afinidad_con_publico = AFINIDAD_PUBLICO_REG
        self.afinidad_con_staff = AFINIDAD_STAFF_REG
        pass

    def accion_especial(self):
        # COMPLETAR
        print(f"{self.nombre} hará un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_REG
        pass
    @property
    def animo(self):
        # COMPLETAR
        variable = super().animo
        if variable < 2:
            print(f"ArtistaReggaeton peligrando en el concierto. Animo: {self.animo}")
        return variable
