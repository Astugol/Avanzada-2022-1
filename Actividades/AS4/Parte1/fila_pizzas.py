class Cliente:
    def __init__(self, nombre):
        # Completar
        self.nombre = nombre
        self.siguiente = None
        pass


    def __str__(self):
        # NO MODIFICAR
        return self.nombre

class FilaPizza:
    def __init__(self):
        # Completar
        self.primero = None
        self.ultimo = None
        self.largo = 0
        pass


    def llega_cliente(self, cliente: Cliente):
        # Completar

        if self.primero == None:
            self.primero = cliente
            self.ultimo = cliente

        else:
            self.ultimo.siguiente = cliente
            self.ultimo = cliente

        self.largo += 1
        pass

    def alguien_se_cuela(self, cliente: Cliente, posicion: int):
        # Completar

        if self.largo == 0:
            self.primero = cliente
            self.ultimo = cliente
            self.largo += 1

        elif posicion == 0:
            cliente.siguiente = self.primero
            self.primero = cliente
            self.largo += 1

        elif int(posicion) >= self.largo:
            self.ultimo.siguiente = cliente
            self.ultimo = cliente
            self.largo += 1

        else:
            nodo_actual = self.primero
            for _ in range(posicion - 1):
                if nodo_actual is not None:
                    nodo_actual = nodo_actual.siguiente

        
            if nodo_actual is not None:
                cliente.siguiente = nodo_actual.siguiente
                nodo_actual.siguiente = cliente
                self.largo += 1
        pass
    
    def cliente_atendido(self):
        # Completar
        if self.largo > 0:
            if self.largo > 1:
                retornar = self.primero
                self.primero = self.primero.siguiente
            else:
                retornar = self.primero
                self.primero = None
            self.largo -= 1
        return retornar

    def __str__(self):
        # Completar
        string = ""
        cliente_actual = self.primero
        for i in range(self.largo):
            if cliente_actual is not None:
                string += f"Cliente{i}: {cliente_actual.nombre}\n"
                cliente_actual = cliente_actual.siguiente
        return string
        pass


if __name__ == "__main__":
    print("\nNO DEBES EJECUTAR AQUÍ EL PROGRAMA!!!!")
    print("Ejecuta el main.py\n")
    raise(ModuleNotFoundError)