import os
from colorama import Fore, Style
from Clase19junio2025.lectura import leer_entero, leer_string, leer_string_en_lista
from Clase19junio2025.escritura import imprimir

def listar_archivos(ruta):
    try:
        return os.listdir(ruta)
    except FileNotFoundError:
        raise FileNotFoundError

def existe_archivo(archivo):
    return os.path.exists(archivo)

def crear_archivo(nombre):
    return open(nombre, "x")

def crear_directorio(nombre):
    try:
        os.mkdir(nombre)
    except FileExistsError:
        raise FileExistsError
    return nombre

def color_segun_extension(ruta, archivo):
    if os.path.isdir(ruta+"/"+archivo):
        return "orange"
    elif len(archivo.split(".")) == 1:
        return "white"
    elif archivo.split(".")[-1] == "txt":
        return "green"
    elif archivo.split(".")[-1] in ["jpg", "png"]:
        return "blue"
    elif archivo.split(".")[-1] in ["mp3", "wav"]:
        return "yellow"
    return "white"

def colorear(color):
    if color == "orange":
        return Fore.MAGENTA
    elif color == "blue":
        return Fore.BLUE
    elif color == "yellow":
        return Fore.YELLOW
    elif color == "green":
        return Fore.GREEN
    return None


def main():
    opcion = -1
    while opcion != 5:
        imprimir("### MENU ###", Fore.REDS)
        imprimir("1. Listar archivos", Fore.BLUE)
        imprimir("2. Verificar existencia archivo", Fore.BLUE)
        imprimir("3. Crear archivo", Fore.BLUE)
        imprimir("4. Crear directorio", Fore.BLUE)
        imprimir("5. Salir", Fore.BLUE)

        opcion = leer_entero("Introduce una opción:\n")

        if opcion == 1:
            ruta = leer_string("Introduce la ruta que quieres consultar:\n")
            try:
                archivos = listar_archivos(ruta)
                for archivo in archivos:
                    print(colorear(color_segun_extension(ruta, archivo)) + archivo + Style.RESET_ALL)
            except FileNotFoundError:
                print(f"La ruta {ruta} no existe")
            except:
                print(f"Error al consultar la ruta, inténtelo de nuevo")

        elif opcion == 2:
            archivo = leer_string("Qué archivo quieres comprobar?\n")
            if existe_archivo(archivo):
                print("✅Archivo existe")
            else:
                print("❌ El archivo no existe")
        elif opcion == 3:
            nombre = leer_string("Qué nombre quieres ponerle al archivo?\n")
            if existe_archivo(nombre):
                print("Este archivo ya existe")
            else:
                archivo = crear_archivo(nombre)
                print(f"Archivo {archivo.name} creado con éxito")
        elif opcion == 4:
            nombre = leer_string("Qué nombre quieres ponerle al directorio?\n")
            try:
                crear_directorio(nombre)
                print(f"Directorio {nombre} creado con éxito")
            except FileExistsError:
                print(f"El directorio {nombre} ya existe")
        elif opcion > 5:
            print("Opción no válida")

if __name__ == '__main__':
    main()