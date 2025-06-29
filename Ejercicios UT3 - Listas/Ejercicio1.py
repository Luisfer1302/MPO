'''
Ejercicio 1 - Sumar elementos de una lista¶
Escribe un programa que pida al usuario una lista de números enteros
separados por comas y calcule la suma de todos los elementos de la lista.
El programa debe imprimir el resultado.

'''

lista_numeros = input("Introduce una lista de números enteros separados por comas: ").split(',')
resultado = 0

#['1', '2', '3', '4', '5', '6']
for i in range(len(lista_numeros)):
    resultado += int(lista_numeros[i])

print(f"Resultado: {resultado}")

