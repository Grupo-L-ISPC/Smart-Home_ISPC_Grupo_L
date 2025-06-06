from funciones import *
from dispositivos import *

def principal():
    op = -1
    
    while op != 0:
        menu_inicio()
        op = int(input("Ingrese una opcion valida: "))

        if op == 1:
            inicio = inicio_sesion()
            while (inicio != None):
                menu_dispositivos()
                op1 = int(input("Ingrese una opcion valida: "))
                if op1 == 1:
                    agregar_dispositivos()
                elif op1 == 2:
                    ver_dispositivos()
                elif op1 == 3:
                    eliminar_dispositivos()
                elif op1 == 4:
                    modificar_dispositivos()
                elif op1 == 5:
                    menu_automatizacion()
                    op2 = int(input("Ingrese una opcion valida: "))
                    if op2 == 1:
                        modo_ahorro()
                elif op1 == 0:
                    break
           
        elif op == 2:
            reg = registro()
            print("Usuario creado exitosamente", reg)
        elif op == 0:
            print("Adios")

principal()