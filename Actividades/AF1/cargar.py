# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,categoria,tiempo_preparacion,precio,ingrediente_1,...,ingrediente_n
from collections import namedtuple


def cargar_platos(ruta_archivo: str) -> list:
    platos = []
    Plato = namedtuple('Plato', ["nombre", "categoria", "tiempo", "precio", "ingredientes"])
    with open(ruta_archivo, "rt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            alimento = linea.strip().split(",")
            ingredientes = set(alimento[4].split(";"))
            d5 = Plato(str(alimento[0]),str(alimento[1]),int(alimento[2]),int(alimento[3]),ingredientes)
            platos.append(d5)
    return platos
    pass

# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,cantidad
def cargar_ingredientes(ruta_archivo: str) -> dict:
    diccionario = {}
    with open(ruta_archivo, "rt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            lista = linea.strip().split(",")
            diccionario[str(lista[0])] = int(lista[1])
    return diccionario
    pass
