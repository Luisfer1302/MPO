"""
Ejercicio 4 - Verificar cuantos números primos hay
Escribe un programa que pida al usuario un número entero y verifique cuantos primos hay hasta ese número.
El programa debe definir una función que reciba el número,
realice la verificación y luego imprima el número de primos.
"""
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2,numero):
        if numero%i == 0:
            return False
    return True

def cuantos_primos(numero):
    resultado = 0

    for i in range(2, numero+1):
        if es_primo(i):
            resultado +=1

    return resultado
numero = int(input("Escribe un número: "))
print(cuantos_primos(numero))