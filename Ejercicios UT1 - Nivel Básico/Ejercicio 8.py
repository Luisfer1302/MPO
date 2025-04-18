##Escribe un programa que pida al usuario tres nombres e
##immprima True si alguno de los nombres es "Juan", False en caso contrario.

nombre1 = input("Introduzca el primer nombre: ")
nombre2 = input("Introduzca el segundo nombre: ")
nombre3 = input("Introduzca el tercer nombre: ")

print(nombre1 == "Juan" or nombre2 == "Juan" or nombre3 == "Juan")