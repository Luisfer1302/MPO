"""
Ejercicio 4 - Verificar si un número es primo
Escribe un programa que pida al usuario un número entero y verifique si es primo.
El programa debe definir una función que reciba el número,
realice la verificación y luego imprima si el número es primo o no.
"""

def es_primo(numero):
    for i in range(2,numero):
        if numero < 2:
            return False
        if numero%i == 0:
            return False
    return True
numero = int(input("Escribe un número: "))
print(es_primo(numero))