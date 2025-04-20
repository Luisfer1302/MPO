#Ejercicio 6 - Triángulo de asteriscos
##Escribe un programa que pida al usuario un número entero positivo y
##dibuje un triángulo de asteriscos con la altura especificada.

altura = int(input("Introduce la altura del triángulo:\n"))
for i in range(1,altura+1):
    print("*"*i)

