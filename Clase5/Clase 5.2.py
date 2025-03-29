#Creame un diccionario
persona = {
    "nombre" : "Luis",
    "edad" : 26,
    "registrado" : True
}
print(persona)
#Accedeme a un valor por su clave
print(persona["edad"])

#Añadir una nueva clave-valor
persona["ciudad"] = "Vurgos"
persona["Número de hijos"] = 0
print(persona)

#Cambiar el valor de una clave
persona["ciudad"] = "Burgos"
persona["Número de hijos"] = 1
print(persona)

#Eliminar una clave
#+del persona["registrado"]
#print(persona)

#Comprobar si una clave ya existe
existe_nombre = "nombre" in persona
existe_luis = "Luis" in persona["nombre"]
print(existe_nombre)
print(existe_luis)

#Comparar dos valores booleanos
es_menor_y_registrado = persona["edad"]<18 and persona["registrado"]
print(es_menor_y_registrado)

#Usar NOT con un booleano
no_veo_registro = not persona["registrado"]
print(no_veo_registro)

#Creame un conjunto a partir de una lista con duplicados
numeritos = [7,8,4,7,1,2,3,5,7,2,6,8,4]
conjunto = set(numeritos) #Convierto a conjunto porque ASÍ ELIMINO DUPLICIDADES
print(conjunto)

#Comparar si dos colecciones tienen los mismos elementos unicos
coleccion_a =set([1,2,2,3,4])
coleccion_b =set([3,4,2,1])
mismos_elementos = coleccion_a == coleccion_b
print(mismos_elementos)
