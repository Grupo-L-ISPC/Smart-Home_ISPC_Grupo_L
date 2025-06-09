from funciones import *
from dispositivos import *

def principal():
    op = - 1
    
    while op != 0:
        menu_inicio()
        op = input("Ingrese una opcion valida: ")
            
        if op == "1":
            inicio = inicio_sesion()
            if inicio is None:
                continue
            if usuarios[inicio]["es_admin"]:
                op_admin = "-1"
                while op_admin != "0" :
                    menu_admin()
                    op_admin = input("Ingrese una opcion valida: ")
                    if op_admin == "1": 
                        ver_usuarios()
                    elif op_admin == "2":
                        eliminar_usuarios()
                    elif op_admin == "3":
                        modificar_rol()
                    elif op_admin == "0":
                        break


            op1 = -1
            while op1 != 0:
                menu_dispositivos()
                op1 = input("Ingrese una opcion valida: ")
                if op1 == "1":
                    agregar_dispositivos()
                elif op1 == "2":
                    ver_dispositivos()
                elif op1 == "3":
                    eliminar_dispositivos()
                elif op1 == "4":
                    modificar_dispositivos()
                elif op1 == "5":
                    op2 = -1
                    menu_automatizacion()
                    while op2 != "0":
                        op2 = input("Ingrese una opcion valida: ")
                        if op2 == "1":
                            modo_ahorro()
                        elif op2 == "0":
                            print("Saliendo del menu de automatizaciones...")
                elif op1 == "6":
                    ver_datos_personales(inicio)
                elif op1 == "0":
                    print("Saliendo del menu de dispositivos...")
                    break
           
        elif op == "2":
            reg = registro()
            print("Usuario creado exitosamente", reg)
        elif op == "0":
            print("Adios")
            break

if __name__ == "__main__":
    principal()
