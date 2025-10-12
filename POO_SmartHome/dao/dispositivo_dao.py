# dao/dispositivo_dao.py
import mysql.connector
from dominio.dispositivo import Dispositivo

class DispositivoDAO:
    def __init__(self, conexion):
        self.conexion = conexion
    
    def obtener_todos(self) -> list:
        """Obtiene todos los dispositivos de la base de datos"""
        cursor = self.conexion.cursor()
        cursor.execute("SELECT nombre, estado, es_esencial FROM dispositivos")
        dispositivos = []
        for fila in cursor.fetchall():
            dispositivo = Dispositivo(fila[0], bool(fila[2]))
            if fila[1] == 1:
                dispositivo.encender()
            else:
                dispositivo.apagar()
            dispositivos.append(dispositivo)
        return dispositivos
    
    def obtener_por_nombre(self, nombre: str) -> Dispositivo:
        """Obtiene un dispositivo por su nombre"""
        cursor = self.conexion.cursor()
        cursor.execute("SELECT nombre, estado, es_esencial FROM dispositivos WHERE nombre = %s", (nombre,))
        fila = cursor.fetchone()
        
        if fila:
            dispositivo = Dispositivo(fila[0], bool(fila[2]))
            if fila[1] == 1:
                dispositivo.encender()
            return dispositivo
        return None
    
    def guardar(self, dispositivo: Dispositivo) -> bool:
        """Guarda un nuevo dispositivo en la base de datos"""
        try:
            cursor = self.conexion.cursor()
            estado = 1 if dispositivo.revisar_estado() == "encendido" else 0
            cursor.execute(
                "INSERT INTO dispositivos (nombre, estado, es_esencial) VALUES (%s, %s, %s)",
                (dispositivo.nombre, estado, dispositivo._es_esencial)
            )
            self.conexion.commit()
            return True
        except mysql.connector.IntegrityError:
            # Dispositivo ya existe
            return False
        except mysql.connector.Error as err:
            print(f"❌ Error guardando dispositivo: {err}")
            return False
    
    def actualizar_estado(self, nombre: str, estado: int) -> bool:
        """Actualiza el estado de un dispositivo"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                "UPDATE dispositivos SET estado = %s WHERE nombre = %s",
                (estado, nombre)
            )
            self.conexion.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as err:
            print(f"❌ Error actualizando estado: {err}")
            return False
    
    def eliminar(self, nombre: str) -> bool:
        """Elimina un dispositivo de la base de datos"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM dispositivos WHERE nombre = %s", (nombre,))
            self.conexion.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as err:
            print(f"❌ Error eliminando dispositivo: {err}")
            return False
    
    def obtener_no_esenciales(self) -> list:
        """Obtiene todos los dispositivos no esenciales"""
        cursor = self.conexion.cursor()
        cursor.execute("SELECT nombre, estado, es_esencial FROM dispositivos WHERE es_esencial = FALSE")
        dispositivos = []
        for fila in cursor.fetchall():
            dispositivo = Dispositivo(fila[0], bool(fila[2]))
            if fila[1] == 1:
                dispositivo.encender()
            dispositivos.append(dispositivo)
        return dispositivos