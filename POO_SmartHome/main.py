# main.py
from conn.database import obtener_conexion_smarthome
from dao.usuarios_dao import UsuarioDAO
from dao.dispositivo_dao import DispositivoDAO
from dominio.dispositivo import Dispositivo
from dominio.usuario import Usuario

def menu_principal():
    """Menú principal del sistema"""
    print("\n=== SISTEMA SMART HOME ===")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("0. Salir")

def menu_usuario_estandar(usuario_actual, usuario_dao, dispositivo_dao):
    """Menú para usuarios estándar - Ahora con gestión completa de dispositivos"""
    while True:
        print(f"\n--- Bienvenido {usuario_actual._nombre} ---")
        print("1. Ver mis datos")
        print("2. Gestionar dispositivos")
        print("0. Cerrar sesión")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            datos = usuario_actual.ver_datos()
            print(f"\n--- Mis Datos ---")
            print(f"Nombre: {datos['nombre']}")
            print(f"Rol: {'Administrador' if datos['es_admin'] else 'Usuario estándar'}")
        
        elif opcion == "2":
            gestionar_dispositivos(dispositivo_dao)
        
        elif opcion == "0":
            print("Sesión cerrada correctamente")
            break
        else:
            print("❌ Opción inválida")

def menu_admin(usuario_actual, usuario_dao, dispositivo_dao):
    """Menú para administradores"""
    while True:
        print(f"\n--- Panel Administrador ---")
        print("1. Gestionar dispositivos")
        print("2. Gestionar usuarios")
        print("0. Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            gestionar_dispositivos(dispositivo_dao)
        elif opcion == "2":
            gestionar_usuarios(usuario_dao)
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida")

def gestionar_dispositivos(dispositivo_dao):
    """Gestión completa de dispositivos - Accesible para todos los usuarios"""
    while True:
        print("\n--- GESTIÓN DE DISPOSITIVOS ---")
        print("1. Ver todos los dispositivos")
        print("2. Agregar dispositivo")
        print("3. Eliminar dispositivo")
        print("4. Modificar estado")
        print("0. Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ver_dispositivos(dispositivo_dao)
        elif opcion == "2":
            agregar_dispositivo(dispositivo_dao)
        elif opcion == "3":
            eliminar_dispositivo(dispositivo_dao)
        elif opcion == "4":
            modificar_estado_dispositivo(dispositivo_dao)
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida")

def ver_dispositivos(dispositivo_dao):
    """Mostrar todos los dispositivos"""
    dispositivos = dispositivo_dao.obtener_todos()
    
    if not dispositivos:
        print("\nNo hay dispositivos registrados")
        return
    
    print(f"\n--- Dispositivos ({len(dispositivos)}) ---")
    for i, dispositivo in enumerate(dispositivos, 1):
        estado = "🟢 ENCENDIDO" if dispositivo.revisar_estado() == "encendido" else "🔴 APAGADO"
        tipo = "ESENCIAL" if dispositivo._es_esencial else "Normal"
        print(f"{i}. {dispositivo.nombre} | {estado} | Tipo: {tipo}")

def agregar_dispositivo(dispositivo_dao):
    """Agregar nuevo dispositivo - Accesible para todos los usuarios"""
    print("\n--- AGREGAR DISPOSITIVO ---")
    nombre = input("Nombre del dispositivo: ").strip()
    
    if not nombre:
        print("❌ El nombre no puede estar vacío")
        return
    
    # Validar si ya existe
    existente = dispositivo_dao.obtener_por_nombre(nombre)
    if existente:
        print("❌ El dispositivo ya existe")
        return
    
    # Preguntar si es esencial
    while True:
        esencial_input = input("¿Es esencial? (s/n): ").lower()
        if esencial_input in ['s', 'n']:
            es_esencial = (esencial_input == 's')
            break
        else:
            print("❌ Por favor ingrese 's' o 'n'")
    
    # Crear y guardar dispositivo
    try:
        nuevo_dispositivo = Dispositivo(nombre, es_esencial)
        if dispositivo_dao.guardar(nuevo_dispositivo):
            print("✅ Dispositivo agregado exitosamente")
        else:
            print("❌ Error al agregar dispositivo")
    except Exception as e:
        print(f"❌ Error al crear dispositivo: {e}")

def eliminar_dispositivo(dispositivo_dao):
    """Eliminar dispositivo existente - Accesible para todos los usuarios"""
    print("\n--- ELIMINAR DISPOSITIVO ---")
    dispositivos = dispositivo_dao.obtener_todos()
    
    if not dispositivos:
        print("No hay dispositivos para eliminar")
        return
    
    ver_dispositivos(dispositivo_dao)
    
    try:
        seleccion = int(input("\nSeleccione dispositivo a eliminar (número): ")) - 1
        if 0 <= seleccion < len(dispositivos):
            dispositivo = dispositivos[seleccion]
            
            # Confirmar eliminación
            confirmar = input(f"¿Está seguro de eliminar '{dispositivo.nombre}'? (s/n): ").lower()
            if confirmar == 's':
                if dispositivo_dao.eliminar(dispositivo.nombre):
                    print("✅ Dispositivo eliminado")
                else:
                    print("❌ Error al eliminar")
            else:
                print("❌ Eliminación cancelada")
        else:
            print("❌ Selección inválida")
    except ValueError:
        print("❌ Ingrese un número válido")

def modificar_estado_dispositivo(dispositivo_dao):
    """Cambiar estado de dispositivo - Accesible para todos los usuarios"""
    print("\n--- MODIFICAR ESTADO ---")
    dispositivos = dispositivo_dao.obtener_todos()
    
    if not dispositivos:
        print("No hay dispositivos")
        return
    
    ver_dispositivos(dispositivo_dao)
    
    try:
        seleccion = int(input("\nSeleccione dispositivo (número): ")) - 1
        if 0 <= seleccion < len(dispositivos):
            dispositivo = dispositivos[seleccion]
            
            print(f"\nDispositivo: {dispositivo.nombre}")
            print(f"Estado actual: {dispositivo.revisar_estado()}")
            
            while True:
                nuevo_estado = input("Nuevo estado (1=encender, 0=apagar): ")
                if nuevo_estado in ['0', '1']:
                    if dispositivo_dao.actualizar_estado(dispositivo.nombre, int(nuevo_estado)):
                        print("✅ Estado actualizado")
                    else:
                        print("❌ Error al actualizar")
                    break
                else:
                    print("❌ Estado debe ser 0 o 1")
        else:
            print("❌ Selección inválida")
    except ValueError:
        print("❌ Ingrese un número válido")

def gestionar_usuarios(usuario_dao):
    """Gestión de usuarios - SOLO para administradores"""
    while True:
        print("\n--- GESTIÓN DE USUARIOS ---")
        print("1. Ver todos los usuarios")
        print("2. Cambiar rol de usuario")
        print("0. Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ver_usuarios(usuario_dao)
        elif opcion == "2":
            cambiar_rol_usuario(usuario_dao)
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida")

def ver_usuarios(usuario_dao):
    """Mostrar todos los usuarios - SOLO para administradores"""
    usuarios = usuario_dao.obtener_todos()
    
    if not usuarios:
        print("\nNo hay usuarios registrados")
        return
    
    print("\n--- USUARIOS REGISTRADOS ---")
    for i, usuario in enumerate(usuarios, 1):
        rol = "👑 Administrador" if usuario._es_admin else "👤 Usuario Estándar"
        print(f"{i}. {usuario._nombre} - {rol}")

def cambiar_rol_usuario(usuario_dao):
    """Cambiar rol de usuario entre admin y usuario estándar - SOLO para administradores"""
    usuarios = usuario_dao.obtener_todos()
    
    if not usuarios:
        print("No hay usuarios registrados")
        return
    
    print("\n--- CAMBIAR ROL DE USUARIO ---")
    ver_usuarios(usuario_dao)
    
    try:
        seleccion = int(input("\nSeleccione usuario (número): ")) - 1
        if 0 <= seleccion < len(usuarios):
            usuario = usuarios[seleccion]
            
            nuevo_rol_input = input("¿Hacer administrador? (s/n): ").lower()
            if nuevo_rol_input in ['s', 'n']:
                nuevo_rol = (nuevo_rol_input == 's')
                
                if usuario_dao.actualizar_rol(usuario._nombre, nuevo_rol):
                    print("✅ Rol actualizado correctamente")
                else:
                    print("❌ Error al actualizar rol")
            else:
                print("❌ Por favor ingrese 's' o 'n'")
        else:
            print("❌ Selección inválida")
    except (ValueError, IndexError):
        print("❌ Ingrese un número válido")

def main():
    """Función principal del programa"""
    try:
        conexion = obtener_conexion_smarthome()
        usuario_dao = UsuarioDAO(conexion)
        dispositivo_dao = DispositivoDAO(conexion)
        
        print("🔌 Conectado a la base de datos")
        
        while True:
            menu_principal()
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":  # Iniciar sesión
                nombre = input("Usuario: ").strip()
                contraseña = input("Contraseña: ")
                
                if not nombre:
                    print("❌ El usuario no puede estar vacío")
                    continue
                
                usuario = usuario_dao.obtener_por_nombre(nombre)
                if usuario and usuario.iniciar_sesion(nombre, contraseña):
                    print("✅ ¡Inicio de sesión exitoso!")
                    
                    if usuario._es_admin:
                        menu_admin(usuario, usuario_dao, dispositivo_dao)
                    else:
                        menu_usuario_estandar(usuario, usuario_dao, dispositivo_dao)
                else:
                    print("❌ Credenciales incorrectas")
            
            elif opcion == "2":  # Registrarse
                nombre = input("Nuevo usuario: ").strip()
                contraseña = input("Contraseña: ")
                
                if not nombre:
                    print("❌ El usuario no puede estar vacío")
                    continue
                
                if len(contraseña) < 3:
                    print("❌ La contraseña debe tener al menos 3 caracteres")
                    continue
                
                nuevo_usuario = Usuario(nombre, contraseña, False)
                if usuario_dao.guardar(nuevo_usuario):
                    print("✅ ¡Usuario registrado exitosamente!")
                else:
                    print("❌ El usuario ya existe")
            
            elif opcion == "0":
                print("Adios")
                break
            else:
                print("❌ Opción inválida")
    
    except Exception as e:
        print(f"❌ Error al conectar con la base de datos: {e}")
    finally:
        if 'conexion' in locals():
            conexion.close()
            print("🔌 Conexión cerrada")

if __name__ == "__main__":
    main()