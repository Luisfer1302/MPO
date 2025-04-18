##Escribe un programa que, dados dos números enteros, imprima su división decimal, si división entera y su resto.
##El segundo número no puede ser cero.

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))

division_decimal = num1 / num2
division_entera = num1 // num2
resto = num1 % num2

print(f"División decimal: {division_decimal}")
print(f"División entera: {division_entera}")
print(f"Resto: {resto}")