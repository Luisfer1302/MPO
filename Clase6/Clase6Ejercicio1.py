#Ejercicio 1 - Siempre negatifo, nunca positifo
##Escribe un programa que pida al usuario un número entero
## y determine si es positivo o negativo.
## El programa debe imprimir un mensaje indicando el resultado.

numero = input("Introduce un número entero:")
numero = int(numero)
#Comprobar si un número es positivo
if numero >0:
    print("Positivo")
else:
    print("Negativo")