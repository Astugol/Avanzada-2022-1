from abc import ABC, abstractmethod
from random import randint
from threading import Thread, Lock, Event, Timer
from time import sleep


class Persona(ABC, Thread):

    # Completar
    lock_bodega = Lock()
    lock_cola_pedidos = Lock()
    lock_cola_pedidos_listos = Lock()

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.disponible = True
        self.trabajando = True
        self.daemon = True

    @abstractmethod
    def run(self):
        pass


class Cocinero(Persona):

    def __init__(self, nombre, cocina):
        # Completar
        super().__init__(nombre)
        self.lugar_trabajo = cocina
        self.evento_plato_asignado = Event()

    def run(self):
        # Completar
        while self.trabajando == True:
            if self.disponible == True:
                self.evento_plato_asignado.wait()
                sleep(randint(1,3))
                self.cocinar()
        pass

    def cocinar(self):
        # Completar
        self.disponible = False
        plato = self.sacar_plato()
        print(f"{self.nombre} está cocinando {plato[0]}")
        self.buscar_ingredientes(plato, self.lugar_trabajo.bodega, self.lugar_trabajo.recetas)
        sleep(randint(1,3))
        self.agregar_plato(plato)
        self.evento_plato_asignado.clear()
        self.disponible = True
        pass

    def sacar_plato(self):
        # Completar
        with self.lock_cola_pedidos:
            plato = self.lugar_trabajo.cola_pedidos.popleft()
            return plato

    def buscar_ingredientes(self, plato, bodega, recetas):
        # Formato de los dicts entregados:
        # bodega = {
        #     "alimento_1": int cantidad_alimento_1,
        #     "alimento_2": int cantidad_alimento_2,
        # }
        # recetas = {
        #     "nombre_plato_1": [("ingrediente_1", "cantidad_ingrediente_1"),
        #                        ("ingrediente_2", "cantidad_ingrediente_2")],
        #     "nombre_plato_2": [("ingrediente_1", "cantidad_ingrediente_1"), 
        #                        ("ingrediente_2", "cantidad_ingrediente_2")]
        # }

        # Completar
        with self.lock_bodega:    
            print(f"{self.nombre} está buscando ingredientes para {plato[1]}")
            ingredientes = recetas[plato[1]]
            for ingrediente in ingredientes:
                nombre_ingrediente = ingrediente[0]
                cantidad_ingrediente = int(ingrediente[1])
                bodega[nombre_ingrediente] -= cantidad_ingrediente
        pass

    def agregar_plato(self, plato):
        # Completar
        with self.lock_cola_pedidos_listos:
            self.lugar_trabajo.cola_pedidos_listos.append(plato)
        pass


class Mesero(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
        # Completar
        self.evento_manejar_pedido = Event()

    def run(self):
        # Completar
        while self.disponible == True and self.trabajando == True:
            self.evento_manejar_pedido.set()
        pass

    def agregar_pedido(self, pedido, cocina):
        # Completar
        with self.lock_cola_pedidos:
            self.evento_manejar_pedido.clear()
            sleep(randint(1,2))
            cocina.cola_pedidos.append(pedido)
            self.evento_manejar_pedido.set()

        pass

    def entregar_pedido(self, cocina):
        # Completar
        with self.lock_cola_pedidos_listos:
            self.evento_manejar_pedido.clear()
            sleep(randint(1,3))
            pedido = cocina.cola_pedidos_listos.popleft()
            print(f"{self.nombre} está entregando un pedido a la mesa {pedido[0]}")
            self.pedido_entregado(pedido)
        pass

    def pedido_entregado(self, pedido):
        # Completar
        print(f"El plato {pedido[1]} fue entregado a la mesa {pedido[0]}")
        self.evento_manejar_pedido.set()
        pass
