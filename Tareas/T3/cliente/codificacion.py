from math import ceil, trunc
import pickle
from utils import data_json

"""
Modulo para funciones de codificacion y decodificacion para envio de mensajes.
"""

def encriptacion(mensaje):
    A = bytearray(b"")
    bytes_centrales_A = bytearray(b"")
    B = bytearray(b"")
    bytes_centrales_B = bytearray(b"")
    contador = 0
    
    for k in mensaje:
        if contador == 0:
            A.append(k)
            bytes_centrales_A.append(k)
            contador += 1

        elif contador == 1:
            B.append(k)
            bytes_centrales_B.append(k)
            contador += 1

        elif contador == 2 or contador == 3:
            A.append(k)
            bytes_centrales_A.append(k)
            contador += 1

        elif contador == 4 or contador == 5:
            B.append(k)
            bytes_centrales_B.append(k)
            if contador == 5:
                contador = 0
            else:
                contador += 1

    if len(A) % 2 == 0:
        seguir_A = True
        while seguir_A == True:
            bytes_centrales_A.pop(0)
            bytes_centrales_A.pop()
            if len(bytes_centrales_A) == 2:
                seguir_A = False
                suma_bytes_A = 0
                for k in bytes_centrales_A:
                    suma_bytes_A += k
    
    else:
        seguir_A = True
        while seguir_A == True:
            bytes_centrales_A.pop(0)
            bytes_centrales_A.pop()
            if len(bytes_centrales_A) == 3:
                seguir_A = False
                suma_bytes_A = 0
                num_izquierda = bytes_centrales_A.pop(0)
                num_derecha = bytes_centrales_A.pop()
                promedio_num = (num_izquierda + num_derecha) / 2
                suma_bytes_A += promedio_num
                suma_bytes_A += bytes_centrales_A.pop()
    
    if len(B) % 2 == 0:
        seguir_B = True
        while seguir_B == True:
            bytes_centrales_B.pop(0)
            bytes_centrales_B.pop()
            if len(bytes_centrales_B) == 2:
                seguir_B = False
                suma_bytes_B = 0
                for k in bytes_centrales_B:
                    suma_bytes_B += k
    
    else:
        seguir_B = True
        while seguir_B == True:
            bytes_centrales_B.pop(0)
            bytes_centrales_B.pop()
            if len(bytes_centrales_B) == 3:
                seguir_B = False
                suma_bytes_B = 0
                num_izquierda = bytes_centrales_B.pop(0)
                num_derecha = bytes_centrales_B.pop()
                promedio_num = (num_izquierda + num_derecha) / 2
                suma_bytes_B += promedio_num
                suma_bytes_B += bytes_centrales_B.pop()

    #print(A)
    #print(B)

    if suma_bytes_A > suma_bytes_B:
        n = b"\x00"
        retorno = bytearray(b"")
        retorno += n
        retorno += B
        retorno += A
        return retorno

    elif suma_bytes_A <= suma_bytes_B:
        n = b"\x01"
        retorno = bytearray(b"")
        retorno += n
        retorno += A
        retorno += B
        return retorno
    
def desencriptar(mensaje):
    
    msj = bytearray(b"")
    A_encriptado = bytearray(b"")
    B_encriptado = bytearray(b"")
    retornar = bytearray(b"")
    msj += mensaje
    largo_mensaje = len(msj) - 1
    sobrante = largo_mensaje % 6

    indicador = msj.pop(0)
    ciclos_cumplidos = trunc(largo_mensaje / 6)
 
    if sobrante == 0:
        largo_A = largo_B = int(len(msj) / 2)
        
    elif sobrante == 1:
        largo_A = ciclos_cumplidos * 3 + 1
        largo_B = ciclos_cumplidos * 3

    elif sobrante == 2:
        largo_A = ciclos_cumplidos * 3 + 1
        largo_B = ciclos_cumplidos * 3 + 1

    elif sobrante == 3:
        largo_A = ciclos_cumplidos * 3 + 2
        largo_B = ciclos_cumplidos * 3 + 1

    elif sobrante == 4:
        largo_A = ciclos_cumplidos * 3 + 3
        largo_B = ciclos_cumplidos * 3 + 1

    elif sobrante == 5:
        largo_A = ciclos_cumplidos * 3 + 3
        largo_B = ciclos_cumplidos * 3 + 2

    contador = 0

    if indicador == 1:
        #print("ok, en este caso el B le ganó a A")
        for k in msj:
            if 0 <= contador < largo_A:
                A_encriptado.append(k)
            else:
                B_encriptado.append(k)
            contador += 1

    else:
        #print("ok, en este caso el A le ganó a B")
        for k in msj:
            if 0 <= contador < largo_B:
                B_encriptado.append(k)
            else:
                A_encriptado.append(k)
            contador += 1

    ### Ahora desencriptaremos a A y B

    contador = 1

    while largo_mensaje > 0:
        
        if contador == 1:
            k = A_encriptado.pop(0)
            retornar.append(k)
            contador += 1

        elif contador == 2:
            k = B_encriptado.pop(0)
            retornar.append(k)
            contador += 1

        elif contador == 3 or contador == 4:
            k = A_encriptado.pop(0)
            retornar.append(k)
            contador += 1

        elif contador == 5 or contador == 6:
            k = B_encriptado.pop(0)
            retornar.append(k)
            if contador == 6:
                contador = 1
            else:
                contador += 1

        largo_mensaje -= 1
    
    return retornar


def codificar(mensaje):

    ## Lo hice con la función "len" pero a veces me daba resultados erróneos, por lo que me aseguré
    ## haciéndolo de esta manera
    largo_mensaje = 0
    for k in mensaje:
        largo_mensaje += 1
    
    cantidad_bloques = ceil(largo_mensaje / 20)
    
    cantidad_bloques_en_bytes = cantidad_bloques.to_bytes(4, byteorder = "little")

    bytes_contenido = b""
    numero_bloque = 0

    while cantidad_bloques > 0:
        contenido = b""
        numero_bloque_en_bytes = numero_bloque.to_bytes(4, byteorder = "big")
        if largo_mensaje >= 20:
            se_uso_totalidad = b"\x01"
            largo = 20
            cuantos_bytes_se_mandaran = largo.to_bytes(1, byteorder = "little")
            for k in range(0, 20):
                num = int(mensaje.pop(0))
                contenido += num.to_bytes(1, byteorder = "little")
                largo_mensaje -= 1

        else:
            se_uso_totalidad = b"\x00"
            cuantos_bytes_se_mandaran = largo_mensaje.to_bytes(1, byteorder = "little")
            for k in range(0, largo_mensaje):
                num = int(mensaje.pop(0))
                contenido += num.to_bytes(1, byteorder = "little")
                largo_mensaje -= 1

        bytes_contenido += numero_bloque_en_bytes
        #print("1: ", bytes_contenido)
        bytes_contenido += se_uso_totalidad
        #print("2: ", bytes_contenido)
        bytes_contenido += cuantos_bytes_se_mandaran
        #print("3: ", bytes_contenido)
        bytes_contenido += contenido
        #print("4: ", bytes_contenido)
        cantidad_bloques -= 1
    
    return bytearray(cantidad_bloques_en_bytes + bytes_contenido)






#mensaje = b"\x05\x08\x03\x02\x04\x03\x05\x09\x04"
# print(mensaje)
#encriptado = encriptacion(mensaje)
#print(encriptado)
# desencriptado = desencriptar(encriptado)
# print(desencriptado)

#mensaje = b'\x80\x04\x95\x13\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x04name\x94\x8c\x05Diego\x94s.'
#print("Mensaje original ------->          ", mensaje)
#print("Mensaje encriptado ----->", encriptacion(mensaje))
#print("Mensaje desencriptado -->", desencriptar(encriptacion(mensaje)))
#bytearray(b'\x01\x80\x95\x13\x00\x00\x00\x94\x04ne\x8c\x05eo\x94\x04\x00\x00\x00\x00}\x8cam\x94Digs.')
#bytearray(b'n\x04am\x95\x13e\x00\x94\x8c\x00\x00\x05\x00Di\x00\x00e\x00go}\x94\x94\x8cs.\x04')


#mensaje = {"nombre": "Diego"}
#bytes = pickle.dumps(mensaje)
#encriptado = encriptacion(bytes)
#print("Encriptado --> ", encriptado)
#codificado = codificar(encriptado)
#print("Codificado --> ", codificado)
