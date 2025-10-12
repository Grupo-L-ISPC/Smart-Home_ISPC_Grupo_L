# conn/database.py (VERSIÓN MYSQL)
import mysql.connector

def obtener_conexion():
    """Crea y devuelve una conexión a MySQL"""
    try:
        conexion = mysql.connector.connect(
            host="localhost",          
            user="root",                 
            password="sql1234T",    
            database="smarthome"      
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"❌ Error conectando a MySQL: {err}")
        return None

def crear_tablas():
    """Crea las tablas necesarias en MySQL"""
    conexion = obtener_conexion()
    if conexion is None:
        return
    
    cursor = conexion.cursor()
    
    try:
        # Crear base de datos si no existe
        cursor.execute("CREATE DATABASE IF NOT EXISTS smarthome")
        cursor.execute("USE smarthome")
        
        # Tabla de usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) UNIQUE NOT NULL,
                contraseña VARCHAR(100) NOT NULL,
                es_admin BOOLEAN DEFAULT FALSE
            )
        ''')
        
        # Tabla de dispositivos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dispositivos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) UNIQUE NOT NULL,
                estado INT DEFAULT 0,
                es_esencial BOOLEAN DEFAULT FALSE,
                usuario_id INT,
                FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
            )
        ''')

           # Tabla de automatizaciones (NUEVA)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS automatizaciones (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) UNIQUE NOT NULL,
                tipo VARCHAR(50) NOT NULL
            )
        ''')
        
        conexion.commit()
        print("✅ Tablas creadas exitosamente en MySQL")
        
    except mysql.connector.Error as err:
        print(f"❌ Error creando tablas: {err}")
    finally:
        conexion.close()

# Crear tablas automáticamente
crear_tablas()