#Ejercicio 1: Evaluación de Expresiones Booleanas
#📌 Objetivo: Evaluar expresiones numéricas que devuelvan valores booleanos.
#Crea variables con expresiones matemáticas y convierte los resultados en booleanos.
#Muestra el valor booleano de cada una.

expresion1 = 10>5
expresion2 = 7+3==10
expresion3 = 4+2==9
expresion4 = 20<15
print(expresion1,expresion2,expresion3,expresion4)

#Ejercicio 2: Operaciones Matemáticas con Booleanos
#📌Objetivo: Descubrir cómo Python trata los valores True y False en operaciones matemáticas.
#Suma True + True y False + True.
#Multiplica True * 10 y False * 50.
#Muestra los resultados y explica qué ocurre.

    #True es igual a 1; false es igual a 0
print(True+True)
print(True-True)
print(False+True)
print(False+False)
print(False-False)
print(True*10)
print(False*50)

#Ejercicio 3.py: Conversión entre Tipos Básicos
#📌 Objetivo: Convertir entre tipos de datos (números, cadenas y booleanos).
#Convierte un número en cadena y muéstralo.
#Convierte una cadena numérica en un entero.
#Convierte un booleano en un número.

numero = 123
cadena = str(numero)
print(cadena)  # "123"
    # convierto una cadena numérica en entero
cadena_numerica = "456"
numero_convertido = int(cadena_numerica)
print(numero_convertido)  # 456
    # convierto un booleano en número
print(int(True))  # 1
print(int(False))  # 0

#Ejercicio 4: Propiedades de las Cadenas
#📌 Objetivo: Manipular cadenas y explorar sus propiedades.
#Crea una cadena con tu nombre.
#Muestra el primer y último carácter.
#Muestra la longitud de la cadena.
#Convierte la cadena a mayúsculas y minúsculas.

    # creo una cadena con un nombre
nombre = "Luis"
    # muestro el primer y último carácter
print(nombre[0])
print(nombre[-1])
    # muestro la longitud de la cadena
print(len(nombre))
    # convierto la cadena a mayúsculas y minúsculas
print(nombre.upper())
print(nombre.lower())

#Ejercicio 5: Operaciones con Cadenas y Números
#📌 Objetivo: Realizar operaciones matemáticas con cadenas y números.
#Concatenar cadenas con números usando str().
#Multiplicar una cadena para repetirla varias veces.

    # concatenar un número con una cadena usando str()
edad = 26
mensaje = "Tengo " + str(edad) + " años."
print(mensaje)
    # repetir una cadena varias veces
repetido = "Hola " * 3
print(repetido)

#Ejercicio 6: Operaciones con Caracteres y Códigos ASCII
#📌 Objetivo: Explorar caracteres y su representación en ASCII.
#Obtén el código ASCII de la letra 'A'.
#Convierte un número en su carácter ASCII correspondiente.

    # obtengo el código ASCII de una letra
codigo = ord('A')
print(codigo)
    # convierto un número en un carácter
letra = chr(66)
print(letra)

#Ejercicio 7: Evaluación de Expresiones Lógicas
#📌 Objetivo: Trabajar con operadores lógicos (and, or, not).
#Evalúa expresiones lógicas combinando números y operadores lógicos.
#Muestra los resultados.

print(10>5 and 3<8)
print(5==5 or 2>10)
print(not(4==4 and 3>1))
