# conn/database.py
import mysql.connector

def obtener_conexion():
    """Crea y devuelve una conexión a MySQL"""
    try:

        conexion = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="sql1234T",  
            database="mysql"  
        )
        print("✅ Conexión a MySQL exitosa")
        return conexion
    except mysql.connector.Error as err:
        print(f"❌ Error conectando a MySQL: {err}")
        return None

def crear_tablas():
    """Crea la base de datos y tablas necesarias"""
    conexion = obtener_conexion()
    if conexion is None:
        print("❌ No se pudo conectar a MySQL")
        return False
    
    cursor = conexion.cursor()
    
    try:
        # 1. CREAR LA BASE DE DATOS si no existe
        cursor.execute("CREATE DATABASE IF NOT EXISTS smarthome")
        print("✅ Base de datos 'smarthome' creada/verificada")
        
        # 2. Usar la base de datos
        cursor.execute("USE smarthome")
        
        # 3. Crear tabla de usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) UNIQUE NOT NULL,
                contraseña VARCHAR(100) NOT NULL,
                es_admin BOOLEAN DEFAULT FALSE
            )
        ''')
        print("✅ Tabla 'usuarios' creada/verificada")
        
        # 4. Crear tabla de dispositivos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dispositivos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) UNIQUE NOT NULL,
                estado INT DEFAULT 0,
                es_esencial BOOLEAN DEFAULT FALSE
            )
        ''')
        print("✅ Tabla 'dispositivos' creada/verificada")
        
        # 5. Insertar usuario admin por defecto
        try:
            cursor.execute(
                "INSERT INTO usuarios (nombre, contraseña, es_admin) VALUES (%s, %s, %s)",
                ('admin', 'admin123', True)
            )
            print("✅ Usuario admin creado: admin/admin123")
        except mysql.connector.IntegrityError:
            print("ℹ️ Usuario admin ya existe")
        
        conexion.commit()
        print("🎉 ¡Base de datos y tablas configuradas correctamente!")
        return True
        
    except mysql.connector.Error as err:
        print(f"❌ Error creando base de datos: {err}")
        return False
    finally:
        conexion.close()

# funcion q se conecta a smarthome
def obtener_conexion_smarthome():
    """Crea y devuelve una conexión a la base de datos smarthome"""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sql1234T",  
            database="smarthome"
        )
        print("✅ Conexión a base de datos 'smarthome' exitosa")
        return conexion
    except mysql.connector.Error as err:
        print(f"❌ Error conectando a smarthome: {err}")
        return None

# Crear tablas automáticamente
crear_tablas()