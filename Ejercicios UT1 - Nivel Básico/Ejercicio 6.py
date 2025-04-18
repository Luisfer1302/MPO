##Escribe un programa que pida al usuario un número entero e imprima:

import math

num = int(input("Introduce un número entero: "))

##Su doble
doble = num * 2
print(f"Doble: {doble}")

##Su triple
triple = num * 3
print(f"Triple: {triple}")

##Su mitad
mitad = num / 2
print(f"Mitad: {mitad}")

##Su cuadrado
cuadrado = num ** 2
print(f"Cuadrado: {cuadrado}")

##Su raíz cuadrada
raiz_cuadrada = math.sqrt(num)
print(f"Raíz cuadrada: {raiz_cuadrada}")
