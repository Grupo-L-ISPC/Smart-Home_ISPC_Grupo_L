
usuarios = {}
    

def inicio_sesion():
    usuario = input("ingrese su usuario: ")
    cont = 0
    while usuario.strip() == "":
        usuario = input("Vuelva a ingresar su usuario, no puede dejar en blanco: ")
    
    while usuario not in usuarios:
        usuario = input("Usuario no válido. Intente de nuevo: ")
        cont += 1
        if  (cont >= 1):
            confirmacion = input("¿ Desea registrarse? (s/n): ").lower()
            while confirmacion not in ("s", "n"):
                confirmacion = input("Respuesta inválida. ¿Desea registrarse? (s/n): ").lower()
            if confirmacion == "s":
                registro()
            else:
                return None
            
    contraseña = input("Ingrese su contraseña: ")
    while contraseña != usuarios[usuario]:
        contraseña = input("Contraseña incorrecta. Intente de nuevo: ")
    
    print("¡Inicio de sesión exitoso!")
    return usuario

def registro():
    usuario_nuevo = input("ingrese un nuevo usuario: ")
    while usuario_nuevo.strip() == "":
        usuario_nuevo = input("Vuelva a ingresar su usuario: ")
    
    if usuario_nuevo in usuarios:
        print("El usuario ya existe.")
    else:
        contraseña_nueva = input("Ingrese una contraseña: ")
        usuarios[usuario_nuevo] = contraseña_nueva

    return usuario_nuevo

def menu_inicio():
    print("1)Inicie sesion")
    print("2)Registrese")
    print("0)Salir")


