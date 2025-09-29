texto = input ("Introduce el texto\n").lower().split()
palabra = input("Introduce la palabra a buscar\n").strip()

print(f"El número de veces que aparece la palabra {palabra} en el texto es {texto.count(palabra)}")