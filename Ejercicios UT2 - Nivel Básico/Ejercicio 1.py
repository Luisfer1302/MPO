##Escribe un programa que pida al usuario un número entero y determine si es par o impar.
##El programa debe imprimir un mensaje indicando el resultado.

numero = int(input("Introduzca un número entero: "))
if numero % 2 == 0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")