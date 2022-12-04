from collections import namedtuple, defaultdict
from functools import reduce


Plato = namedtuple('nombre', 'nombre ingredientes')

class Ayudante:
    def __init__(self, nombre, platos, dinero):
        self.nombre = nombre
        self.platos = platos # lista con namedtuples de platos
        self.dinero = dinero

    def obtener_ingredientes_platos(self):
        # Completar
        ingredientes_para_plato = list(map(lambda x: x.ingredientes, self.platos))
        return ingredientes_para_plato

    def cantidad_ingredientes(self, lista_ingredientes_platos):
        # Completar
        cantidad_ingredientes = {}
        for plato in lista_ingredientes_platos:
            for ingrediente in plato:
                if ingrediente[0] not in cantidad_ingredientes:
                    cantidad_ingredientes[ingrediente[0]] = int(ingrediente[1])
                else:
                    cantidad_ingredientes[ingrediente[0]] += int(ingrediente[1])
        for ingrediente in cantidad_ingredientes:
            yield(ingrediente, cantidad_ingredientes[ingrediente])
    
    def total_compra(self, ingredientes_platos, supermercado):
        # Completar
        ingredientes = reduce(lambda x, y: x + y, ingredientes_platos)
        precios_por_ingrediente = map(lambda x: supermercado.consulta_precio(x[0]) * int(x[1]), \
            ingredientes)
        precio_total = reduce(lambda x, y: x + y, precios_por_ingrediente)
        return precio_total

