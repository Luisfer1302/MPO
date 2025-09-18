'''

Ejercicio holaa.txt - Invertir una lista¶
Escribe un programa que pida al usuario
una lista de números enteros separados por espacios y la invierta.
El programa debe imprimir la lista invertida.

'''

lista = input("Escribe números enteros separados por espacios: ").split()
lista.reverse()
print(lista)

'''
OTRA FORMA:

lista = input("Escribe números enteros separados por espacios: ").split()
lista_reversa = []

for i in range(len(lista)):
    lista_reversa.append(lista.pop())

print(lista)

'''