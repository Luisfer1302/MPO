import os

'''
1. Comprobar que existe el archivo
2. Comprobar que sea un archivo
3. Comprobar que exista la nueva ruta
4. Comprobar que la nueva ruta es un directorio
5. Comprobar que path y new_path no son iguales
6. Mover el archivo a new_path
'''


def move_file(path, new_path):
    if not os.path.isfile(path):

    pass

path = input("Introduce el archivo que quieres mover\n")
new_path = input("Introduce ela ruta donde quieres moverlo\n")

try:
    print(move_file(path, new_path))
except Exception as e:
    print(e)