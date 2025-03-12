# 📌 EJERCICIO PRÁCTICO 1️⃣:
# 📌 Crea dos números enteros y muestra la suma y la resta de ellos.
# 📌 Declara un número flotante y muestra su valor dividido entre 2.

suma = 15 + 25
resta = 15 - 25
print("Suma",suma, "|Resta", resta)

numero_decimal = 3.6
print("Número divido entre dos", numero_decimal/2)

# 📌 EJERCICIO PRÁCTICO 2️⃣:
# 📌 Declara una variable booleana que sea True si 15 es mayor que 8.
# 📌 Escribe una expresión que use "and" y otra que use "or" y muestra el resultado.

mayor_que = 15 > 8
print("15 es mayor que 8:", mayor_que)
and_logico = True and False
or_logico = True or False
print("True AND False:", and_logico)
print("True OR False:", or_logico)


# 📌 EJERCICIO PRÁCTICO 3️⃣:
# 📌 Crea una variable con tu nombre y apellidos y muestra su longitud.
# 📌 Concatena tu nombre con una frase de presentación.
# 📌 Convierte tu nombre en mayúsculas y minúsculas.
# 📌 Extrae los primeros 3 caracteres de tu nombre usando slicing.

nombre_completo="Luis Fernando Del Río Pérez"
print(nombre_completo)
print("Longitud del nombre completo:", len("nombre_completo"))

frase_presentacion = "Hola, mi nombre es " + nombre_completo
print(frase_presentacion)

print("Nombre en mayúsculas:", nombre_completo.upper())
print("Nombre en minúsculas:", nombre_completo.lower())

primer_nombre = nombre_completo.split()[0]
primeros_tres = primer_nombre[:3]
print("Primeros 3 caracteres del nombre:", primeros_tres)
