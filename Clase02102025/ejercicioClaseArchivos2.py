'''
Vamos a realizar un programa que lea el archivo sistema_og_extenso.txt e imprima y copie todos los mensajes del tipo Error(ERR).
'''

log = open("Clase02102025/sistema_log_extenso.txt", "r") #Referencia al archivo
log_errores = open("errores.txt","w")
log_data = log.readlines() #Lista con todas las líneas en String
for line in log_data:
    if "ERROR" in line:
        log_errores.write(line)
