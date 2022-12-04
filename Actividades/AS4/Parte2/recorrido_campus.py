from Parte2.campus import Lugar
from collections import deque

def comprobar_chismoso(lugar: Lugar):
    # NO MODIFICAR
    for ayudante in lugar.ayudantes:
        if "Croak" in ayudante.frase:
            return True
    return False


def bfs_iterativo(inicio: Lugar, final: Lugar):
    # Completar
    visitados = []
    # La cola de siempre, comienza desde el nodo inicio.
    queue = deque([inicio])

    while len(queue) > 0:
        vertice = queue.popleft()


        if vertice in visitados:
            continue

        visitados.append(vertice)

        for vecino in vertice.vecinos:
            if comprobar_chismoso(vecino) == False:
                queue.append(vecino)
                if vecino == final:
                    return True
    return False


def dfs_iterativo(inicio: Lugar, final: Lugar):
    # Completar
    pass

def bfs_iterativo_largo(inicio: Lugar, final: Lugar):
    # Completar 
    pass


def dfs_iterativo_largo(inicio: Lugar, final: Lugar):
    # Completar 
    visitados = []
    camino = []
    print("INICIO ", inicio)
    print("FINAL ", final)
    # La cola de siempre, comienza desde el nodo inicio.
    queue = deque([inicio])

    while len(queue) > 0:
        vertice = queue.popleft()


        if vertice in visitados:
            print("Nombre del repetido" ,vertice.nombre)
            print("CAMINO MALO ", camino)
            continue

        visitados.append(vertice)

        for vecino in vertice.vecinos:
            if comprobar_chismoso(vecino) == False and vecino.nombre != "Pizza" and vecino.nombre\
                not in camino:
                camino.append(vecino)
                print("EL CAMINO HASTA AHORA ", camino)
                queue.append(vecino)
                if vecino == final:
                    return len(camino)
                continue
    pass


def bfs_iterativo_camino(inicio: Lugar, final: Lugar):
    # Utiliza este diccionario para implementar el camino. 
    # Las llaves del diccionario es UN nodo vecino (NO un listado de todos los nodos vecinos) 
    # y el valor el nodo en cuestion
    padres = dict()
    padres[inicio] = None

    # Completar
    pass
    

def dfs_iterativo_camino(inicio: Lugar, final: Lugar):
    # Utiliza este diccionario para implementar el camino. 
    # Las llaves del diccionario es UN nodo vecino (NO un listado de todos los nodos vecinos) 
    # y el valor el nodo en cuestion
    padres = dict()
    padres = dict()
    padres[inicio] = None

    # Completar
    pass
    
    
def creador_camino(diccionario_padres, final):
    # NO MODIFICAR
    camino = []
    camino.append(final)
    while diccionario_padres[final] is not None:
        camino.append(diccionario_padres[final])
        final = diccionario_padres[final]
    camino.reverse()
    return camino


def imprimir_camino(camino):
    # NO MODIFICAR
    recorrido = ""
    largo = len(camino)
    contador = 1
    for lugar in camino:
        if contador < largo:
            recorrido = recorrido + f"[{lugar.nombre}] -> "
        else:
            recorrido = recorrido + f"[{lugar.nombre}]."
        contador += 1
    print(recorrido)

if __name__ == "__main__":
    print("\nNO DEBES EJECUTAR AQUÍ EL PROGRAMA!!!!")
    print("Ejecuta el main.py\n")
    raise(ModuleNotFoundError)
