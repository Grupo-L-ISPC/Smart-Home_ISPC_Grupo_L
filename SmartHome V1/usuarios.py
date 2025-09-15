usuarios = usuarios = {
    "admin": {
        "contraseña": "admin123",
        "es_admin": True
    }  
}



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
                usuario = input("Registro exitoso. Ingrese su usuario: ")
            else:
                return None

    
    contraseña = input("Ingrese su contraseña: ")
    while contraseña != usuarios[usuario]["contraseña"]:
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
        while contraseña_nueva == "":
            contraseña_nueva = input("La contraseña no puede estar vacía. Intente de nuevo: ").strip()
        usuarios[usuario_nuevo] = {
        "contraseña": contraseña_nueva,
        "es_admin": False
        }

    return usuario_nuevo

def ver_datos_personales(usuario):
    print("\n--- Datos personales ---")
    print("Nombre de usuario: " + usuario)
    if usuarios[usuario]["es_admin"]:
        print("Rol: Administrador")
    else:
        print("Rol: Usuario estándar")

#Funciones de admin

def ver_usuarios():
    print("\nUsuarios registrados:")
    for usuario in usuarios:
        print(f"- {usuario}")
        if usuarios[usuario]["es_admin"]:
            print("Rol: Administrador")
        else:
            print("Rol: Usuario estándar")


def eliminar_usuarios():
    ver_usuarios()
    usuario_a_eliminar = input("Ingrese el nombre de usuario a eliminar: ")
    if (usuario_a_eliminar in usuarios) and (usuario_a_eliminar != "admin"):
        del usuarios[usuario_a_eliminar]
        print(f"Usuario '{usuario_a_eliminar}' eliminado")

def modificar_rol():
    ver_usuarios()
    usuario_a_modificar = input("Ingrese el nombre de usuario a modificar el rol: ")
    if usuario_a_modificar not in usuarios:
        print("El usuario no existe.")
    elif usuario_a_modificar == "admin":
        print("No se puede modificar el rol del usuario admin.")
    else:
        nuevo_rol = input("¿Desea que sea administrador? (s/n): ").lower()
        while nuevo_rol not in ("s", "n"):
            nuevo_rol = input("Respuesta inválida. ¿Desea que sea administrador? (s/n): ").lower()
        if nuevo_rol == "s":
            usuarios[usuario_a_modificar]["es_admin"] = True
        else:
            usuarios[usuario_a_modificar]["es_admin"] = False
        print("Rol actualizado con exito")








