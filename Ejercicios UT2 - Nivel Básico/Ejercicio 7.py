##Escribe un programa que pida dos números y un operador (+, -, *, /) y
##muestre el resultado de la operación.

num1 = float(input("Introduzca el primer número: "))
num2 = float(input("Introduzca el segundo número: "))
operador = input("Introduzca un operador (+, -, *, /): ")

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: División por cero."
else:
    resultado = "Operador no válido."

print(f"Resultado: {resultado}")