import datetime

usuarios = {
    "jordi": "c0ntr4s3n4",
    "asires": "seguridad",
    "damdawers": "prototipppo"
}

def verify_user(user, passw):
    if user in usuarios.keys():
        #TODO loguear error de acceso
        raise ValueError("Acceso denegado")
        # TODO loguear error de acceso
    if passw != usuarios[user]:
        raise ValueError("Acceso denegado")

    with open("log.txt", "a") as file:
        file.write(f"{datetime.now().isoformat(timespec="seconds")} Se ha loguedado EXITOSAMENTE al usuario.

while True:
    user = input("Introduce tu usuario:\n")
    passw = input("Introduce tu password:\n")

try:
    verify_user(user, passw)
except Exception as e:
    print(e)