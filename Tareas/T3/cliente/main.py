import sys
from PyQt5.QtWidgets import QApplication
from backend.cliente import Cliente

if __name__ == "__main__":
    try:
         # =========> Instanciamos la APP <==========
        app = QApplication(sys.argv)

        # =========> Iniciamos el cliente <==========
        cliente = Cliente()

        sys.exit(app.exec_())

    except ConnectionError as e:
        print("Ocurrió un error: ", e)

    except KeyboardInterrupt:
        print("\nCerrando cliente...")
        cliente.salir()
        sys.exit()