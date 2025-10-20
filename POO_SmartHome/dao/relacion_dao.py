# dao/relacion_dao.py
import mysql.connector

class RelacionDAO:
    def __init__(self, conexion):
        self.conexion = conexion
    
    def asignar_dispositivo_usuario(self, usuario_id: int, dispositivo_id: int) -> bool:
        """Asigna un dispositivo a un usuario"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                "INSERT INTO usuario_dispositivo (usuario_id, dispositivo_id) VALUES (%s, %s)",
                (usuario_id, dispositivo_id)
            )
            self.conexion.commit()
            print(f"✅ Dispositivo {dispositivo_id} asignado al usuario {usuario_id}")
            return True
        except mysql.connector.IntegrityError:
            print("❌ Esta relación ya existe")
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
    
    def obtener_dispositivos_por_usuario(self, usuario_id: int) -> list:
        """Obtiene todos los dispositivos asignados a un usuario (CON JOIN REAL)"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                SELECT d.id, d.nombre, d.estado, d.es_esencial 
                FROM dispositivos d
                JOIN usuario_dispositivo ud ON d.id = ud.dispositivo_id
                WHERE ud.usuario_id = %s
            ''', (usuario_id,))
            return cursor.fetchall()  # Retorna lista de tuplas
        except mysql.connector.DataError as e:
            print(f"❌ Error de datos: {e}")
            return []
        except mysql.connector.OperationalError as e:
            print(f"❌ Error operacional: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
    
    def obtener_usuarios_por_dispositivo(self, dispositivo_id: int) -> list:
        """Obtiene todos los usuarios que tienen un dispositivo (CON JOIN REAL)"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                SELECT u.id, u.nombre, u.es_admin 
                FROM usuarios u
                JOIN usuario_dispositivo ud ON u.id = ud.usuario_id
                WHERE ud.dispositivo_id = %s
            ''', (dispositivo_id,))
            return cursor.fetchall()
        except mysql.connector.DataError as e:
            print(f"❌ Error de datos: {e}")
            return []
        except mysql.connector.OperationalError as e:
            print(f"❌ Error operacional: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
    
    def eliminar_asignacion(self, usuario_id: int, dispositivo_id: int) -> bool:
        """Elimina la relación entre usuario y dispositivo"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                "DELETE FROM usuario_dispositivo WHERE usuario_id = %s AND dispositivo_id = %s",
                (usuario_id, dispositivo_id)
            )
            self.conexion.commit()
            return cursor.rowcount > 0
        except mysql.connector.DataError as e:
            print(f"❌ Error de datos: {e}")
            return False
        except mysql.connector.OperationalError as e:
            print(f"❌ Error operacional: {e}")
            return False
        finally:
            if cursor:
                cursor.close()