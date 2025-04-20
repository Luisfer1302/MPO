##Escribe un programa que pida el precio de un producto y,
##si supera los 100€, aplique un descuento del 10%.
##Muestra el precio final.

precio = float(input("Introduzca el precio del producto: "))
if precio > 100:
    descuento = precio * 0.10
    precio_final = precio - descuento
else:
    precio_final = precio

print(f"El precio final es: {precio_final}€")