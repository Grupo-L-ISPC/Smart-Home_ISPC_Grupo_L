# Script de Base de Datos - Sistema Smart Home

## 📋 Descripción
Script SQL **autocontenido** para la base de datos del sistema de domótica Smart Home. **Incluye creación de tablas**, inserciones de datos y consultas analíticas.



## 🚀 Cómo ejecutar el script

### Opción 1: OneCompiler (Recomendado)
1. Visitar [OneCompiler - MySQL](https://onecompiler.com/mysql)
2. **Pegar TODO el contenido** del archivo `script_bd.sql`
3. Hacer clic en **"Run"**
4. Ver todos los resultados en la pantalla

### Opción 2: MySQL Workbench
## Aclaracion!!: si va a usar esta opcion, copiar desde los insert y no desde la creacion de tablas, porque el codigo py ya crea las tablas automaticamente, tambien debe modificar el archivo database.py para poner su propia conexion, puerto, usuario, psw, etc.

1. Abrir MySQL Workbench
2. Conectarse al servidor MySQL
3. Crear nueva consulta
4. Pegar el script completo y ejecutar
