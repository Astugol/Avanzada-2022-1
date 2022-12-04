"""
Módulo principal del servidor
"""
from servidor import Servidor

if __name__ == "__main__":
    servidor = Servidor()

    try:
        while True:
            input("[Presione Ctrl+C para cerrar]".center(82, "+") + "\n")

    except KeyboardInterrupt:
        print("\n\n")
        print("Cerrando servidor...".center(80, " "))
        print("".center(82, "-"))
        print("".center(82, "-") + "\n")
        servidor.cerrar_servidor()