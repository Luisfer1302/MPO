#Ejercicio 1 - Contador
##Escribe un programa que pida al usuario un número entero positivo e
##imprima los números desde el 0 hasta ese número (incluido).
##El programa debe imprimir los números en cada iteración.

numero = int(input("Introduce un número entero positivo:\n"))
for i in range(0,numero+1):
    print(i)