#Ejercicio 8 - Cuadrado con cruz
##Escribe un programa que pida al usuario un número entero positivo impar y
##dibuje un cuadrado de x con una cruz en el medio.

dimension = int(input("Introduce un número positivo impar que indique la dimensión del cuadrado:\n"))

for i in range(dimension):
    for j in range(dimension):
        if i == 0 or i == dimension-1:
            print("x"*dimension,end="")
            break
        if j == 0 or j == dimension-1 or j == i or j+i == dimension-1:
            print("x",end="")
        else:
            print(" ",end="")
    print()

