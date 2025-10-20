# dao/usuario_dao.py
import mysql.connector
from dominio.usuario import Usuario

class UsuarioDAO:
    def __init__(self, conexion):
        self.conexion = conexion
    
    def obtener_por_nombre(self, nombre: str):
        """Busca un usuario por su nombre en la base de datos"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT id, nombre, contraseña, es_admin FROM usuarios WHERE nombre = %s", (nombre,))
            return cursor.fetchone()  # Retorna la fila directa
        except mysql.connector.IntegrityError as e:
            print(f"❌ Error de integridad: {e}")
            return None
        except mysql.connector.DataError as e:
            print(f"❌ Error de datos: {e}")
            return None
        except mysql.connector.OperationalError as e:
            print(f"❌ Error operacional: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
    
    def guardar(self, usuario: Usuario) -> bool:
        """Guarda un nuevo usuario en la base de datos"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nombre, contraseña, es_admin) VALUES (%s, %s, %s)",
                (usuario.nombre, usuario.contraseña, usuario.es_admin)
            )
            self.conexion.commit()
            return True
        except mysql.connector.IntegrityError:
            # Usuario ya existe
            return False
        except mysql.connector.DataError as e:
            print(f"❌ Error de datos: {e}")
            return False
        except mysql.connector.OperationalError as e:
            print(f"❌ Error operacional: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    def obtener_todos(self) -> list:
        """Obtiene todos los usuarios de la base de datos"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT nombre, contraseña, es_admin FROM usuarios")
            return cursor.fetchall()  # Retorna las filas directamente
        except mysql.connector.DataError as e:
            print(f"❌ Error de datos: {e}")
            return []
        except mysql.connector.OperationalError as e:
            print(f"❌ Error operacional: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
    
    def actualizar_rol(self, nombre: str, es_admin: bool) -> bool:
        """Actualiza el rol de un usuario (solo admin puede hacer esto)"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                "UPDATE usuarios SET es_admin = %s WHERE nombre = %s",
                (es_admin, nombre)
            )
            self.conexion.commit()
            return cursor.rowcount > 0
        except mysql.connector.IntegrityError as e:
            print(f"❌ Error de integridad: {e}")
            return False
        except mysql.connector.DataError as e:
            print(f"❌ Error de datos: {e}")
            return False
        except mysql.connector.OperationalError as e:
            print(f"❌ Error operacional: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    def eliminar(self, nombre: str) -> bool:
        """Elimina un usuario de la base de datos"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM usuarios WHERE nombre = %s", (nombre,))
            self.conexion.commit()
            return cursor.rowcount > 0
        except mysql.connector.IntegrityError as e:
            print(f"❌ Error de integridad: {e}")
            return False
        except mysql.connector.DataError as e:
            print(f"❌ Error de datos: {e}")
            return False
        except mysql.connector.OperationalError as e:
            print(f"❌ Error operacional: {e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def obtener_id_por_nombre(self, nombre: str) -> int:
        """Obtiene el ID de un usuario por su nombre"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT id FROM usuarios WHERE nombre = %s", (nombre,))
            fila = cursor.fetchone()
            return fila[0] if fila else None
        except mysql.connector.DataError as e:
            print(f"❌ Error de datos: {e}")
            return None
        except mysql.connector.OperationalError as e:
            print(f"❌ Error operacional: {e}")
            return None
        finally:
            if cursor:
                cursor.close()