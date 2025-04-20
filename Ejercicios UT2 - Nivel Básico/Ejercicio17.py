#Escribe un programa que reciba un número entero positivo y una letra.
#El programa debe imprimir la letra tantas veces como el número introducido.

numero = int(input("Introduce un número entero positivo: "))
letra = input("Introduce una letra: ")
for i in range(numero):
    print(letra, end="")
print()
