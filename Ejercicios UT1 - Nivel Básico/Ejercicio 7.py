##Escribe un programa que pida al usuario tres números enteros e
##imprima True si todos ellos son mayores que cero, False en caso contrario.

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))
num3 = int(input("Introduzca el tercer número: "))

print(num1 > 0 and num2 > 0 and num3 > 0)