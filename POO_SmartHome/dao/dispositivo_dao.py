# dao/dispositivo_dao.py
import mysql.connector
from dominio.dispositivo import Dispositivo

class DispositivoDAO:
    def __init__(self, conexion):
        self.conexion = conexion
    
    def obtener_todos(self) -> list:
        """Obtiene todos los dispositivos de la base de datos"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT nombre, estado, es_esencial FROM dispositivos")
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
    
    def obtener_por_nombre(self, nombre: str):
        """Obtiene un dispositivo por su nombre"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT nombre, estado, es_esencial FROM dispositivos WHERE nombre = %s", (nombre,))
            return cursor.fetchone()  # Retorna la fila directa
        except mysql.connector.DataError as e:
            print(f"❌ Error de datos: {e}")
            return None
        except mysql.connector.OperationalError as e:
            print(f"❌ Error operacional: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
    
    def guardar(self, dispositivo: Dispositivo) -> bool:
        """Guarda un nuevo dispositivo en la base de datos"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            estado = 1 if dispositivo.revisar_estado() == "encendido" else 0
            cursor.execute(
                "INSERT INTO dispositivos (nombre, estado, es_esencial) VALUES (%s, %s, %s)",
                (dispositivo.nombre, estado, dispositivo.es_esencial)
            )
            self.conexion.commit()
            return True
        except mysql.connector.IntegrityError:
            # Dispositivo ya existe
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
    
    def actualizar_estado(self, nombre: str, estado: int) -> bool:
        """Actualiza el estado de un dispositivo"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                "UPDATE dispositivos SET estado = %s WHERE nombre = %s",
                (estado, nombre)
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
        
    def eliminar(self, nombre: str) -> bool:
        """Elimina un dispositivo de la base de datos"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM dispositivos WHERE nombre = %s", (nombre,))
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
    
    def obtener_no_esenciales(self) -> list:
        """Obtiene todos los dispositivos no esenciales"""
        cursor = None
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT nombre, estado, es_esencial FROM dispositivos WHERE es_esencial = FALSE")
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