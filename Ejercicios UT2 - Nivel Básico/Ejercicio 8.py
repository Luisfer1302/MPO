##Escribe un programa que pida el nombre de un mes y
##muestre cuántos días tiene (puedes simplificar febrero a 28 días siempre).

mes = input("Introduzca el nombre de un mes: ").lower()
if mes in ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]:
    dias = 31
elif mes in ["abril", "junio", "septiembre", "noviembre"]:
    dias = 30
elif mes == "febrero":
    dias = 28
else:
    dias = "Mes no válido."

print(f"{mes.capitalize()} tiene {dias} días.")