# dao/usuario_dao.py
import mysql.connector
from dominio.usuario import Usuario

class UsuarioDAO:
    def __init__(self, conexion):
        self.conexion = conexion
    
    def obtener_por_nombre(self, nombre: str) -> Usuario:
        """Busca un usuario por su nombre en la base de datos"""
        cursor = self.conexion.cursor()
        cursor.execute("SELECT id, nombre, contraseña, es_admin FROM usuarios WHERE nombre = %s", (nombre,))
        fila = cursor.fetchone()
        
        if fila:
            return Usuario(fila[1], fila[2], bool(fila[3]))  # nombre, contraseña, es_admin
        return None
    
    def guardar(self, usuario: Usuario) -> bool:
        """Guarda un nuevo usuario en la base de datos"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nombre, contraseña, es_admin) VALUES (%s, %s, %s)",
                (usuario._nombre, usuario._contraseña, usuario._es_admin)
            )
            self.conexion.commit()
            return True
        except mysql.connector.IntegrityError:
            # Usuario ya existe
            return False
        except mysql.connector.Error as err:
            print(f"❌ Error de base de datos: {err}")
            return False
    
    def obtener_todos(self) -> list:
        """Obtiene todos los usuarios de la base de datos"""
        cursor = self.conexion.cursor()
        cursor.execute("SELECT nombre, contraseña, es_admin FROM usuarios")
        usuarios = []
        for fila in cursor.fetchall():
            usuarios.append(Usuario(fila[0], fila[1], bool(fila[2])))
        return usuarios
    
    def actualizar_rol(self, nombre: str, es_admin: bool) -> bool:
        """Actualiza el rol de un usuario (solo admin puede hacer esto)"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                "UPDATE usuarios SET es_admin = %s WHERE nombre = %s",
                (es_admin, nombre)
            )
            self.conexion.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as err:
            print(f"❌ Error actualizando rol: {err}")
            return False
    
    def eliminar(self, nombre: str) -> bool:
        """Elimina un usuario de la base de datos"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM usuarios WHERE nombre = %s", (nombre,))
            self.conexion.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as err:
            print(f"❌ Error eliminando usuario: {err}")
            return False