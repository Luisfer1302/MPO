##Escribe un programa que pida el nombre de un día de la semana y muestre si es "laborable" o "fin de semana".

dia = input("Introduzca el nombre de un día de la semana: ").lower()
if dia in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
    print(f"{dia.capitalize()} es un día laborable.")
elif dia in ["sábado", "domingo"]:
    print(f"{dia.capitalize()} es fin de semana.")
else:
    print("Día no válido.")