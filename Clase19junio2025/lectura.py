from Clase19junio2025.escritura import imprimir

'''' FUNCIONES PARA LEER DIFERENTES TIPOS DE DATOS CON CONTROL DE ERRORES'''

def leer_entero(mensaje, color=None):

    '''Esto deberia hacer un input, intentar castearlo a int, y devolver valor entero.
    Si al intentar castear la entrada no es un numero, capturar excepcion y elevarla'''

    try:
        imprimir(mensaje, color)
        entero = int(input())
    except:
        raise ValueError("Debes introducir un número entero")
    return entero
def leer_string(mensaje, color=None):
    imprimir(mensaje, color)
    return input()

def leer_string_en_lista(mensaje, color=None):
    imprimir(mensaje,color)
    return input(mensaje).split(" ")