#Escribe un programa que pida al usuario un número entero positivo y
#calcules la suma de la potencia de 3 de cada número desde 1 hasta el número introducido.
#El programa debe imprimir el resultado.

numero = int(input("Introduce un número entero positivo: "))
suma = 0
for i in range(1, numero + 1):
    suma += i ** 3
print(f"La suma de la potencia de 3 de los números desde 1 hasta {numero} es: {suma}")
