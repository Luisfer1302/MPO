#Longitud de una cadena

nombre = "Luis Del Río"
print("Longitud del nombre: " , len(nombre))

#Convertir texto a mayúsculas y minúsculas
#upper
print("Esto soy yo en mayúsculas: ", nombre.upper())
#lower
print("Esto soy yo en minúsculas: ", nombre.lower())

#Slicing
print("Primeros 3 caracteres: ", nombre[:3])
print("Últimos 4 caracteres: ", nombre[-4:])

#Reemplazar palabras en una cadena (old y new aparece al escribir las palabras entre comillas que queremos sustituir)
frase = "Me gusta Java"
print("Cambio la palabra: ", frase.replace("Java", "Python"))
print(frase)

#Verificar si una cadena existe en otra
print("Python" in frase)
nueva_frase= "Me gusta Python"
print("Python" in nueva_frase)

#Unir varias palabras en una cadena
palabras = ["Hola", "Mundo", "en", "Python"]
print("Frase completa con join: ", "".join(palabras))
print("Frase completa con join: ", " ".join(palabras))
print("Frase completa con join: ", "  ".join(palabras))
print("\nHola Mundo")

#Split
oracion = "Python es divertido"
palabritas = oracion.split()
print("Lista de palabras de mi grupo: ", palabritas)

#Redondear un número decimal
numero = 3.1416
print("Mi número redondeado es: ", round(numero,1))
print("Mi número redondeado es: ", round(numero,2))
print("Mi número redondeado es: ", round(numero,3))

#Formateo de números decimales
precio = 19.99
print("Precio con dos decimales: {:.5f}".format(precio))
print("Precio con dos decimales: {:.1f}".format(precio))
print("Precio con dos decimales: {:.0f}".format(precio))

#Obtener el valor ASCII de un carácter
print("Esto es el código ASCII de 'A': ", ord('A'))

#Elevar al cuadrado
numero_al_cuadrado = 100
print("holaa.txt al cuadrado es: ", numero_al_cuadrado ** 2)

#Elevar al cubo
numero_al_cubo = 5
print("holaa.txt al cubo es: ", numero_al_cubo **3)

#Raíz cuadrada
print("Raiz cuadrada de 25 es: ", 25** 0.5)

import math
numerito = 100
raiz = math.sqrt(numerito)
print("Raíz cuadrada de 100: ", raiz)

#Diviones enteras y resto
print("División normal: ", 10/3)
print("División entera: ", 10//3)
print("Resto: ", 10%3)

#Generar un numero aleatorio
import random
print("Número aleatorio entre 1 y 10: ", random.randint(1,10))  #a: y b: se generan, no hay que escribirlos

#Convertir números a cadenas y viceversa
numerajo = 300
texto = str(numerajo)
print("Convertido a texto: ", texto)

#Redondear hacia arriba
print("Redondeo hacia arriba del número 3.6: ", math.ceil(3.6))

#Redondear hacia abajo
print("Redondeo hacia arriba del número 3.2: ", math.floor(3.2))

#Convertir una lista en un conjunto (eliminar duplicados)
numeroides = [1,2,3,3,4,5,5]
sin_duplicados = set(numeroides)
print("La lista de numeroides sin duplicados es: ", sin_duplicados)

#######Prueba#######
cadena = "200"
numerajo = int(cadena)
texto = "Es el número"
print("Convertido a numero soy: ", numerajo)
print(str(numerajo)+texto)
#####################

#Repetir una cadena
print("Money!" * 3)

#Tipo de dato
dato = 3.14
print("El tipo de variable de dato es: ", type(dato))

#Combinar cadenas y variables en un print
name = "Luis"
edad = "26"
print(f"Hola, soy {name} y tengo {edad} años.")