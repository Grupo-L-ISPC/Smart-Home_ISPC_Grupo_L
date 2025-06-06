dispositivos = {}

def agregar_dispositivos():
    nombre_dispositivo = input("Ingrese un dispositivo nuevo: ")

    while nombre_dispositivo.strip() == "":
        nombre_dispositivo = input("Vuelva a ingresar un dispositivo: ")

    if nombre_dispositivo in dispositivos:
        print("El dispositivo ya existe.")
    else:
        estado = int(input("Ingrese un estado (0/1): "))
        while estado not in (0, 1):
            estado = int(input("Vuelva a Ingresar un estado valido (0/1): "))
        esencial = input("¿Es esencial? (s/n): ").lower()
        while esencial not in ("s", "n"):
            esencial = input("Respuesta inválida. ¿Es esencial? (s/n): ").lower()
        dispositivos[nombre_dispositivo] = {
        "estado": estado,
        "esencial": esencial == "s"
    }
        
    
        
def ver_dispositivos():
    print(dispositivos)


def eliminar_dispositivos():
    print(dispositivos)
    borrar = input("Escriba el nombre del dispositivo a eliminar: ")
    while borrar.strip() == "":
        borrar = input("Vuelva a ingresar un dispositivo: ")
    while borrar not in dispositivos:
        print("No se encuentra ese dispositivo")
        borrar = input("Escriba el nombre del dispositivo a eliminar: ")
    del dispositivos[borrar]
    print(f"Se eliminó el dispositivo '{borrar}'.")


def modificar_dispositivos():
    print(dispositivos)
    nombre_dispositivo = input("Escriba el nombre del dispositivo a modificar: ")
    while nombre_dispositivo.strip() == "":
        nombre_dispositivo = input("Vuelva a ingresar un dispositivo: ")
    while nombre_dispositivo not in dispositivos:
        print("No se encuentra este dispositivo")
        nombre_dispositivo = input("Escriba el nombre del dispositivo a modificar: ")
    estado = int(input("Escriba un estado (0/1): "))
    while estado not in (0, 1):
            estado = int(input("Vuelva a Ingresar un estado valido (0/1): "))
    dispositivos[nombre_dispositivo]["estado"] = estado


def menu_dispositivos():
    print("1) Agregar Dispositivos")
    print("2) Ver dispostivos")
    print("3) Eliminar Dispositivos")
    print("4) Modificar Dispositivos")
    print("5) Automatizaciones")
    print("0) Salir")


def menu_automatizacion():
    print("1) Modo de ahorro")


def modo_ahorro():
    print("\nActivando modo ahorro...")
    for nombre, datos in dispositivos.items():
        if not datos["esencial"]:
            dispositivos[nombre]["estado"] = 0
            print(f"→ {nombre} no esencial puesto en estado inactivo.")






