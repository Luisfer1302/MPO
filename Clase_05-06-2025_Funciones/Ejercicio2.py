"""
Ejercicio 2 - Configura un mensaje de bienvenida
Escribe un programa que pida al usuario un nombre, un apellido y una edad.
El programa debe definir una función que reciba estos datos y
luego imprima un mensaje de bienvenida personalizado.
"""

def configurar_mensaje(nombre, apellido, edad):
    print(f"Bienvenid@ {nombre} {apellido}, tienes {edad} años")

nombre = input("Intrduce tu nombre: ")
apellido = input("Intrduce tu apellido: ")
edad = int(input("Intrduce tu edad: "))

configurar_mensaje(nombre, apellido, edad)
