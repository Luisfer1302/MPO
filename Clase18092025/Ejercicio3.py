nombre = input("Cual es tu nombre?: ")
palabras = nombre.split()
iniciales = "".join([p[0].upper()for p in palabras])
#Lo de arriba es igual a :
    #iniciales = ""
        #for p in palabras:
            #iniciales += p[0].upper()
print(iniciales)