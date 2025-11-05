import csv

data = list()

''' 
1. Leer el archivvo
2. Coger la fila del encabezado
3. Generamos un iterable con todas las filas del archivo csv
4. Vamos recogiendo cada fila del iterable
    4.1 Generamos un item -> diccionario con la clave = posicion encabezado
    4.2 Agregamos el item a la lista data
'''

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    print(header)
    for row in reader:
        item = dict()
        for i in range(len(header)):
            item[header[i]] = row[i]
        data.append(item)

print(data)