# Ejercicio 13 - Tabla de multiplicar
##Escribe un programa que pida al usuario un número entero positivo y
##muestre la tabla de multiplicar de ese número.

numero = int(input("Introduce un número entero positivo:\n"))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
