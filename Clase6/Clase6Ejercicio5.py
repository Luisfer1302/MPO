#Ejercicio holaa.txt - Puede entrar en el servidor de Discord?
##Escribe un programa que pida un rol y una academia de estudios,
##si el rol es "alumno" y la academia es "Prometeo" el programa debe darle acceso al servidor de Discord oficial y al de los alumnos, donde se critica a los profes.
##Si el rol es "profesor" y la academia es "Prometeo" el programa debe darle acceso al servidor de Discord oficial, pero no al de los alumnos.
##En cualquier otro caso, el programa debe imprimir "No tienes acceso al servidor de Discord".

rol = input("Dime el rol del usuario: ").lower()
academia = input("En que academia estudias/trabajas? ").lower()

if rol == "estudiante" and academia == "prometeo":
    print("Access granted to: Official and Chill Discord")
elif rol == "profesor" and academia == "prometeo":
    print("Access granted to: Official Discord")
else:
    print("Enroll Prometeo to access to the best Discord servers")