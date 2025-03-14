#GENERADOR DE NOMBRES DE USUARIO
#Pide al usuario su nombre y apellido.
#Genera un nombre de usuario en minúsculas, sin espacios.
#Añade un número aleatorio al final.
#Muestra el nombre de usuario generado.

import random
nombre = input("Ingresa tu nombre: ").strip().lower()
apellido = input("Ingresa tu apellido: ").strip().lower()
numero = random.randint(10,99)
usuario_final = f"{nombre}{apellido}{numero}"
print(f"Tu nombre de usuario generado es: {usuario_final}")


#ANALIZADOR DE FRASES
#Pide al usuario que ingrese una frase.
#Muestra la cantidad de caracteres de la frase.
#Indica si la frase contiene la palabra "Python".
#Convierte la frase a mayúsculas.
#Muestra la frase invertida.

frase = input("Escribe una frase: ")
print("Longitud de la frase:", len(frase))
print("¿Contiene 'Python'?:", "Python" in frase)
print("Frase en mayúsculas:", frase.upper())
print("Frase invertida:", frase[::-1])

#CÁLCULO DE DESCUENTOS
#Pide al usuario el precio de un producto.
#Aplica un 15% de descuento.
#Muestra el precio final con dos decimales.
#Muestra el precio redondeado hacia arriba.

import math
precio = float(input("Escribe el precio del producto: "))
descuento = precio * 0.15
precio_final = precio - descuento
print(f"Precio con descuento: ${precio_final:.2f}")
print(f"Redondeado hacia arriba: ${math.ceil(precio_final)}")

#GENERADOS DE ETIQUETAS DE PRODUCTOS
#Pide el nombre de un producto y su precio.
#Convierte el nombre del producto a mayúsculas.
#Muestra el precio con dos decimales.
#Genera un código basado en el valor ASCII de la primera letra del producto.

producto = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
etiqueta = f"PRODUCTO: {producto.upper()} - PRECIO: ${precio:.2f} - CÓDIGO: {ord(producto[0])}"
print(etiqueta)

#CONVERSIÓN DE TIPOS Y MANIPULACIÓN DE LISTAS
#Pide al usuario una lista de números separados por comas.
#Convierte cada número a entero.
#Elimina los números repetidos.
#Muestra la lista ordenada sin duplicados.

numeros = input("Escribe números separados por comas: ")
lista_numeros = list(set(map(int, numeros.split(","))))
print("Lista sin duplicados y ordenada:", sorted(lista_numeros))

#CREACIÓN DE MENSAJES PERSONALIZADOS
#Pide al usuario su nombre, edad y ciudad.
#Muestra un mensaje con toda la información.
#Si la edad es menor de 18, redondea hacia arriba hasta la mayoría de edad.

nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))
ciudad = input("Escribe tu ciudad: ")
edad_redondeada = math.ceil(edad / 18) * 18
mensaje = f"Hola {nombre}, tienes {edad} años y vives en {ciudad}. Edad mínima adulta: {edad_redondeada}."

#GENERADOS DE CONTRASEÑAS ALEATORIAS
#Pide al usuario su nombre.
#Genera una contraseña segura con la primera letra en mayúscula, un número aleatorio y un símbolo especial.
#Muestra la contraseña generada.

nombre = input("Escribe tu nombre: ")
contraseña = f"{nombre[0].upper()}-{random.randint(100, 999)}-*"
print(f"Tu nueva contraseña es: {contraseña}")

#VERIFICACIÓN DE NOMBRES EN LISTAS
#Pide al usuario su nombre y verifica si está en una lista de invitados.
#Muestra su posición en la lista.

invitados = ["Luis", "Fernando", "Sergio", "Maria", "Paula"]
nombre = input("Escribe tu nombre: ")
if nombre in invitados:
    print(f"Bienvenido, {nombre}! Estás en la posición {invitados.index(nombre) + 1}.")
else:
    print("Lo siento, no estás en la lista.")

#MANIPULACIÓN DE NOMBRES
#Pide al usuario su nombre y apellido.
#Convierte el nombre a minúsculas, el apellido a mayúsculas
#Genera un alias combinando las primeras 3 letras de cada uno.

nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
alias = nombre[:3].lower() + apellido[:3].upper()
print(f"Tu alias es: {alias}")

#FORMATEAR Y MOSTRAR DATOS MATEMÁTICOS
#Pide al usuario un número flotante.
#Muestra el número redondeado, su cuadrado y su raíz cuadrada.

numero = float(input("Escribe un número decimal: "))
print(f"Número redondeado: {round(numero, 2)}")
print(f"Cuadrado: {numero ** 2}")
print(f"Raíz cuadrada: {numero ** 0.5}")



