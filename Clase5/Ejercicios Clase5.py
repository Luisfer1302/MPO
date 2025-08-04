#Ejercicio 1: Comparación de números y booleanos
#📌 Objetivo: Usar comparaciones con números y analizar los resultados booleanos.
#Crea tres variables numéricas con valores diferentes.
#Compara los valores entre sí (>, <, >=, <=, ==, !=).
#Almacena los resultados en nuevas variables booleanas y muéstralos.
from Clase1.Clase1 import multiplicacion

a = 13
b = 36
c= 21
igual = a==c
mayor = b>a
menor = a<c
diferente = c !=a
print(igual,mayor,menor,diferente)

#Ejercicio 2: Propiedades y manipulación de cadenas
#📌 Objetivo: Trabajar con cadenas y métodos integrados de Python.
#Crea una cadena con una frase corta.
#Muestra cuántos caracteres tiene la cadena.
#Convierte toda la cadena a mayúsculas y minúsculas.
#Cuenta cuántas veces aparece una letra específica en la cadena.

cadenita = "Estoy aprendiendo mucho"
print(len(cadenita))
print(cadenita.lower())
print(cadenita.upper())
print(cadenita.count("a"))

#Ejercicio 3.py: Operaciones matemáticas con números y booleanos
#📌 Objetivo: Realizar cálculos numéricos usando valores booleanos.
#Define dos variables booleanas (verdadero, falso) con los valores True y False.
#Realiza operaciones matemáticas con estos valores (+, *, -).
#Muestra los resultados y analiza qué sucede.

verdadero = True
falso = False

suma = verdadero + falso
resta = verdadero - falso
multiplicación = verdadero*15
multiplicacion2 = falso*18
print(suma,resta,multiplicación,multiplicacion2)

#Ejercicio 4: Extracción de caracteres en una cadena
#📌 Objetivo: Extraer partes de una cadena utilizando índices y slicing.
#Define una cadena con una palabra o nombre.
#Extrae y muestra los tres primeros caracteres.
#Extrae y muestra los tres últimos caracteres.
#Extrae los caracteres en posiciones impares de la cadena.

nombre = "Informática"
print(nombre[:3])
print(nombre[-3:])
print(nombre[::2])


#Ejercicio holaa.txt: Conversión de tipos y evaluación booleana
#📌 Objetivo: Convertir entre tipos básicos y analizar valores booleanos.
#Convierte un número en una cadena y muestra el tipo de dato.
#Convierte una cadena numérica en un número entero y muestra el tipo.
#Convierte diferentes valores ("", "Texto", 0, 1, -1, None) a booleanos y muestra los resultados.

numerazo = 258
numerazo_cadena = str(numerazo)
print(numerazo_cadena,type(numerazo_cadena))

cadena_numero = "30"
numero_convertir = int(cadena_numero)
print(numero_convertir, type(numero_convertir))

print(bool(""))
print(bool("Texto"))
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(None))