#Escribe un programa que pida al usuario dos números enteros e
#imprima la secuencia de números entre ellos (incluidos) en orden ascendente.
#El primer número siempre será menor que el segundo.

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

for i in range(numero1,numero2 + 1):
    print (i)