'''

Ejercicio 3 - Mayor y menor elemento de una lista¶
Escribe un programa que pida al usuario una lista de números enteros separados
por comas y encuentre el mayor y el menor elemento de la lista.
El programa debe imprimir ambos resultados.

'''

lista_numeros = input("Introduce una lista de números enteros separados por comas: ").split(',')
lista_numeros = [int(num) for num in lista_numeros]
lista_numeros.sort()
print(f"menor: {lista_numeros[0]} mayor: {lista_numeros[-1]}")