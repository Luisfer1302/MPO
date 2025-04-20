##Escribe un programa que pida al usuario un número entero y determine si es positivo, negativo o cero.
##El programa debe imprimir un mensaje indicando el resultado.

numero = int(input("Introduce un número entero: "))
if numero > 0:
    print(f"{numero} es positivo.")
elif numero < 0:
    print(f"{numero} es negativo.")
else:
    print("El número es cero.")
