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


