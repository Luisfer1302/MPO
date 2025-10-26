'''
Vamos a realizar un programa que lea el archivo sistema_og_extenso.txt e imprima por pantalla todos los mensajes del tipo Error(ERR).
'''

log = open("Clase02102025/sistema_log_extenso.txt", "r") #Referencia al archivo

log_data = log.readlines() #Lista con todas las líneas en String
for line in log_data:
    if "ERR" in line:
        print(line)

