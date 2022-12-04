import parametros
import funciones
from datetime import datetime

print("---- Bienvenid@ a DCCorreos de Chile ----\n")

funciones.menu_de_inicio()

opcion = int(input())

while opcion != 4:
    es_usuario = False
    es_administrador = False
    if opcion == 1:
        nombre_ingresado = str(input("Por favor, ingrese su nombre de usuario: "))
        contrasena_ingresada = str(input("Por favor, ingrese su contraseña: "))
        resultado_nombre = funciones.revisar_nombre(nombre_ingresado)
        resultado_contrasena = funciones.revisar_contrasena(contrasena_ingresada)
        
        if resultado_nombre == False:
            print("**ERROR** Nombre ingresado no existente\n")
        
        elif resultado_contrasena == False:
            print("**ERROR** Clave ingresada incorrecta\n")
        
        else:
            print("¡Bienvenido de vuelta!\n")
            es_usuario = True
            lista = []

    elif opcion == 2:
        nombre_ingresado = str(input("Ingrese el nombre de usuario que gustaría ocupar: "))
        contrasena_nueva = str(input("Por favor, ingrese su contraseña: "))
        resultado_nombre_nuevo = funciones.revisar_nombre_ocupado(nombre_ingresado)
        nombre_alfabetico = funciones.revisar_nombre_alfabetico(nombre_ingresado)
        contrasena_alfanumerica = funciones.revisar_contrasena_alfanumerica(contrasena_nueva)

        if len(nombre_ingresado) < parametros.MIN_CARACTERES:
            print(f"Su nombre tiene que tener {parametros.MIN_CARACTERES} caracteres mínimo\n")
        elif resultado_nombre_nuevo == False:
            print("**ERROR** Su nombre ingresado ya está ocupado\n")
        elif len(contrasena_nueva) < parametros.LARGO_CONTRASENA:
            print(f"Su contraseña debe tener {parametros.LARGO_CONTRASENA} caracteres mínimo\n")
        elif nombre_alfabetico == False:
            print("**ERROR** Solo se admiten caracteres alfabéticos en el nombre de usuario")
        elif len(nombre_ingresado) > 26:
            print("**ERROR** Nombre de usuario debe tener como máximo 26 caracteres")
        elif contrasena_alfanumerica == False:
            print("**ERROR** Solo se admiten caracteres alfanuméricos en la contraseña")
        else:
            funciones.agregar_nuevo_usuario(nombre_ingresado, contrasena_nueva)
            print("¡Felicitaciones, ya tiene su usuario registrado!\n")
            es_usuario = True
            lista = []
    
    elif opcion == 3:
        contrasena_admin = str(input("Por favor, ingrese su contraseña: "))
        if contrasena_admin != parametros.CONTRASENA_ADMIN:
            print("**ERROR** Contraseña incorrecta\n")
        else:
            es_administrador = True
            print("¡Bienvenido de vuelta, administrador!\n")

    while es_usuario == True:
        funciones.menu_de_usuario()
        opcion_usuario = int(input())
        if opcion_usuario == 1:
            print("* Ingresa los datos de tu encomienda a continuación *")
            seguir_articulo = True
            seguir_destinatario = True
            seguir_peso = True
            seguir_destino = True
            seguir = True
            while seguir == True and seguir_articulo == True:
                nombre_articulo = input("Nombre del artículo: ")
                coma1 = funciones.comprobar_formato_sin_comas(nombre_articulo)
                if coma1 == True:
                    print("**ERROR** No pueden haber comas en su nombre de artículo\n")
                    funciones.continuar_o_no()
                    continuar1 = int(input())
                    if continuar1 == 1:
                        pass
                    elif continuar1 == 2:
                        seguir = False
                        seguir_articulo = False
                elif len(nombre_articulo) > 57:
                    print("**ERROR** Nombre del artículo puede tener como máximo 57 caracteres")
                    funciones.continuar_o_no()
                    continuar1 = int(input())
                    if continuar1 == 1:
                        pass
                    elif continuar1 == 2:
                        seguir = False
                        seguir_articulo = False
                elif coma1 == False:
                    print("Nombre del artículo ingresado correctamente\n")
                    lista.append(nombre_articulo)
                    seguir_articulo = False
            
            while seguir == True and seguir_destinatario == True:
                nombre_destinatario = input("Nombre del destinatario: ")
                dest = funciones.comprobar_destinatario(nombre_destinatario)
                if dest == True:
                    print("Nombre del destinatario ingresado correctamente\n")
                    seguir_destinatario = False
                elif dest == False:
                    print("**ERROR** Nombre ingresado no registrado\n")
                    funciones.continuar_o_no()
                    continuar2 = int(input())
                    if continuar2 == 1:
                        pass
                    elif continuar2 == 2:
                        seguir = False
                        seguir_destinatario = False
            
            while seguir == True and seguir_peso == True:
                peso = float(input("Peso del artículo: "))
                if peso > parametros.MAX_PESO:
                    print(f"**ERROR** El peso máximo es de {parametros.MAX_PESO}kg\n")
                    funciones.continuar_o_no()
                    continuar3 = int(input())
                    if continuar3 == 1:
                        pass
                    elif continuar3 == 2:
                        seguir = False
                        seguir_peso = False
                elif peso <= parametros.MAX_PESO:
                    print("Peso del artículo ingresado correctamente\n")
                    seguir_peso = False

            while seguir == True and seguir_destino == True:
                destino = str(input("Nombre del destino: "))
                coma2 = funciones.comprobar_formato_sin_comas(destino)
                if coma2 == True:
                    print("**ERROR** No pueden haber comas en su nombre de destino\n")
                    funciones.continuar_o_no()
                    continuar4 = int(input())
                    if continuar4 == 1:
                        pass
                    elif continuar4 == 2:
                        seguir = False
                        seguir_destino = False
                elif len(destino) > 27:
                    print("**ERROR** El nombre del destino puede tener como máximo 27 caracteres")
                    funciones.continuar_o_no()
                    continuar4 = int(input())
                    if continuar4 == 1:
                        pass
                    elif continuar4 == 2:
                        seguir = False
                        seguir_destino = False
                elif coma2 == False:
                    estado = "Emitida"
                    print("Destino ingresado correctamente\n")
                    print("Registro existoso de la encomienda, ¡Felicitaciones!\n")
                    hora_exacta = datetime.now().strftime("%H:%M:%S")
                    dia = datetime.today().strftime('%Y/%m/%d')
                    todo = dia + " " + hora_exacta
                    funciones.agregar_nueva_encomienda(nombre_articulo,\
                        nombre_destinatario, peso, destino, todo, estado)
                    seguir = False

            pass
        elif opcion_usuario == 2:
            funciones.revisar_estado(lista)
            pass
        elif opcion_usuario == 3:
            titulo = str(input("Por favor, ingrese el título de su reclamo: "))
            descripcion = str(input("Por favor, ingrese una descripción del reclamo: "))
            funciones.ingresar_reclamo(nombre_ingresado, titulo, descripcion)
            print("Reclamo realizado")
            pass
        elif opcion_usuario == 4:
            funciones.ver_pedidos_personales(nombre_ingresado)
            pass
        elif opcion_usuario == 5:
            es_usuario = False
            pass
        pass

    while es_administrador == True:
        funciones.menu_de_administrador()
        opcion_administrador = int(input())
        if opcion_administrador == 1:
            actualizar = True
            funciones.mostrar_encomiendas()
            print("Por favor, seleccione una opción")
            decision = int(input())
            if decision != 0:
                funciones.actualizar_encomiendas(decision)
                pass
        elif opcion_administrador == 2:
            ver_reclamos = True
            while ver_reclamos == True:
                funciones.mostrar_titulos_reclamos()
                visualizacion = int(input())
                funciones.mostrar_descripcion_reclamo(visualizacion)
                print("Seleccione una de las siguientes opciones:")
                print("[1] Visualizar otro reclamo de la lista")
                print("[2] Volver al menú anterior")
                choice_admin = int(input())
                if choice_admin == 1:
                    pass
                elif choice_admin == 2:
                    ver_reclamos = False
            pass
        elif opcion_administrador == 3:
            es_administrador = False
            pass

    funciones.menu_de_inicio()
    opcion = int(input())
    pass

print("Haz salido del programa! Nos vemos pronto")