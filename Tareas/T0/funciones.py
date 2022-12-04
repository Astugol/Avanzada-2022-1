def revisar_nombre(nombre_ingresado):
    with open("usuarios.csv", "rt", encoding="utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        correcto = False
        for linea in lineas1:
            completo = linea.strip().split(",")
            if str(completo[0]) != str(nombre_ingresado):
                correcto = False
            else:
                correcto = True
                break
    return correcto

def revisar_contrasena(contrasena_ingresada):
    with open("usuarios.csv", "rt", encoding="utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        correcto = False
        for linea in lineas1:
            completo = linea.strip().split(",")
            if str(completo[1]) != str(contrasena_ingresada):
                correcto = False
            else:
                correcto = True
                break
    return correcto

def revisar_nombre_ocupado(nombre_nuevo):
    with open("usuarios.csv", "rt", encoding="utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        correcto = False
        for linea in lineas1:
            completo = linea.strip().split(",")
            if str(completo[0]) != str(nombre_nuevo):
                correcto = True
            else:
                correcto = False
                break
    return correcto

def revisar_nombre_alfabetico(nombre_nuevo):
    correcto = True
    for letra in nombre_nuevo:
        if letra not in "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM":
            correcto = False
            pass
    return correcto

def revisar_contrasena_alfanumerica(contrasena_nueva):
    correcto = True
    for letra in contrasena_nueva:
        if letra not in "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM0123456789":
            correcto = False
            pass
    return correcto

def agregar_nuevo_usuario(nombre_nuevo, contrasena_nueva):
    with open("usuarios.csv", "a", encoding="utf-8") as archivo1:
        archivo1.write(f"\n{nombre_nuevo},{contrasena_nueva}")


def menu_de_inicio():
    print("** Menú de Inicio **\n")
    print("Selecciona una de las siguientes opciones:\n")
    print("[1] Iniciar sesión como usuario")
    print("[2] Registrarse como usuario")
    print("[3] Iniciar sesión como administrador")
    print("[4] Salir del programa\n")
    print("Indique la opción elegida:")

def menu_de_usuario():
    print("** Menú de usuario **\n")
    print("Selecciona una de las siguientes opciones\n")
    print("[1] Hacer encomienda")
    print("[2] Revisar estado de encomiendas realizadas")
    print("[3] Realizar reclamos")
    print("[4] Ver el estado de los pedidos personales")
    print("[5] Cerrar sesión\n")
    print("Indique la opción elegida:")

def comprobar_formato_sin_comas(nombre_articulo):
    coma = False
    for letra in nombre_articulo:
        if letra == ",":
            coma = True
    return coma

def comprobar_destinatario(nombre_destinatario):
    with open("usuarios.csv", "rt", encoding="utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        correcto = False
        for linea in lineas1:
            completo = linea.strip().split(",")
            if str(completo[0]) == str(nombre_destinatario):
                correcto = True
                break
            else:
                correcto = False
    return correcto

def continuar_o_no():
    print("Seleccione una de las siguientes opciones:\n")
    print("[1] Continuar con la encomienda")
    print("[2] Cancelar encomienda")

def agregar_nueva_encomienda(nombre_articulo, nombre_destinatario, peso, destino, fecha, estado):
    with open("encomiendas.csv", "a", encoding="utf-8") as archivo1:
        archivo1.write(f"\n{nombre_articulo},{nombre_destinatario},{peso},{destino},\
{fecha},{estado}")

def revisar_estado(lista):
    with open("encomiendas.csv", "rt", encoding="utf-8") as archivo1:
        a = 0
        lineas1 = archivo1.readlines()
        for linea in lineas1:
            completo = linea.strip().split(",")
            for nombre in lista:
                if completo[0] == nombre:
                    print(f"Nombre del artículo: {completo[0]}; estado del artículo: {completo[5]}")
                    a += 1
                    pass
    if a == 0:
        print("Lo sentimos, no tiene encomiendas realizadas durante esta sesión.\n")  

def ingresar_reclamo(nombre_ingresado, titulo, descripcion):
    with open("reclamos.csv", "a", encoding="utf-8") as archivo1:
        archivo1.write(f"\n{nombre_ingresado},{titulo},{descripcion}")

def ver_pedidos_personales(nombre_ingresado):
    with open("encomiendas.csv", "rt", encoding = "utf-8") as archivo1:
        a = 0
        lineas1 = archivo1.readlines()
        for linea in lineas1:
            completo = linea.strip().split(",")
            if str(completo[1]) == str(nombre_ingresado):
                print(f"Nombre artículo: {completo[0]}")
                print(f"Destinatario del artículo: {completo[1]}")
                print(f"Peso del artículo: {completo[2]}")
                print(f"Destino: {completo[3]}")
                print(f"Fecha en la que se recepcionó: {completo[4]}")
                print(f"Estado del artículo: {completo[5]}\n")
                a += 1
    if a == 0:
        print("Lo sentimos, no tiene pedidos personales asignados a su nombre.\n")

def menu_de_administrador():
    print("** Menú de administrador **\n")
    print("[1] Actualizar encomiendas")
    print("[2] Revisar reclamos")
    print("[3] Cerrar sesión\n")
    print("Indique la opción elegida: ")


def mostrar_encomiendas():
    print("      |                     Nombre artículo                     |         \
Receptor         |  Peso  |          Destino          |           Estado           |")
    with open("encomiendas.csv", "rt", encoding="utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        cte = 1
        for linea in lineas1:
            completo = linea.strip().split(",")
            if completo[0] != "nombre_articulo":
                if cte == 1:
                    print("")
                print(f"[{cte: ^4}] {completo[0]: ^57} {completo[1]: ^26} \
{float(completo[2]): ^8.2f} {completo[3]: ^27} {completo[5]: ^28}")
                cte += 1
    print("")
    print("[ 0  ] Volver\n")

def actualizar_encomiendas(decision):
    a = 0
    lista = []
    actualizado = False
    with open("encomiendas.csv", "rt", encoding="utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        for linea in lineas1:
            completo = linea.strip().split(",")
            lista.append(completo)

    with open("encomiendas.csv", "w", encoding = "utf-8") as archivo2:
        for hola in lista:
            if a != int(decision) and a == 0:
                archivo2.write(f"{str(hola[0])},{str(hola[1])},{str(hola[2])},\
{str(hola[3])},{str(hola[4])},{str(hola[5])}")
                pass
            
            elif a == int(decision):
                if str(hola[5]) == "Emitida":
                    archivo2.write(f"\n{hola[0]},{hola[1]},{hola[2]},{hola[3]},\
{hola[4]},Revisada por agencia")
                    actualizado = True
                elif str(hola[5]) == "Revisada por agencia":
                    archivo2.write(f"\n{hola[0]},{hola[1]},{hola[2]},{hola[3]},\
{hola[4]},En camino")
                    actualizado = True
                elif str(hola[5]) == "En camino":
                    archivo2.write(f"\n{hola[0]},{hola[1]},{hola[2]},{hola[3]},\
{hola[4]},Llegada al destino")
                    actualizado = True
                elif str(hola[5]) == "Llegada al destino" or str(hola[5]) == "En destino":
                    archivo2.write(f"\n{hola[0]},{hola[1]},{hola[2]},{hola[3]},\
{hola[4]},{hola[5]}")
                    actualizado = False
                pass

            elif a != int(decision):
                archivo2.write(f"\n{hola[0]},{hola[1]},{hola[2]},{hola[3]},\
{hola[4]},{hola[5]}")
                pass
            a += 1
    if actualizado == True:    
        print(f"Encomienda número {decision} actualizada")
    else:
        print(f"La encomienda número {decision} no puede ser actualizada, ya llegó a su destino")

def mostrar_titulos_reclamos():
    print("Títulos de los reclamos:\n")
    with open("reclamos.csv", "rt", encoding="utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        a = 1
        for linea in lineas1:
            completo = linea.strip().split(",")
            if completo[1] != "titulo":
                print(f"[{a}] {completo[1]}")
                a += 1
        print("")
    print("Escoja el reclamo que quiera revisar:")

def mostrar_descripcion_reclamo(visualizacion):
    with open("reclamos.csv", "rt", encoding="utf-8") as archivo1:
        lineas1 = archivo1.readlines()
        a = 0
        b = 1
        for linea in lineas1:
            completo = linea.strip().split(",")
            if a == int(visualizacion):
                print(f"[{a}] {completo[1]}")
                print(f"Descripción: {completo[2]}")
            a += 1
            b += 1
    print("")