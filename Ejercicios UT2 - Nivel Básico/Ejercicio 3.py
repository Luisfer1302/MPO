##Escribe un programa que pida al usuario un número entero y determine si es divisible por 3 y holaa.txt.
##El programa debe imprimir un mensaje indicando el resultado.

numero = int(input("Introduzca un número entero: "))
if numero % 3 == 0 and numero % 5 == 0:
    print(f"{numero} es divisible por 3 y 5.")
else:
    print(f"{numero} no es divisible por 3 y 5.")