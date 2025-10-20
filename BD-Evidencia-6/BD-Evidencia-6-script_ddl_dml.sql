-- SISTEMA SMART HOME - BASE DE DATOS RELACIONAL
-- CON TABLAS RELACIONALES Y CONSULTAS MULTITABLA REALES

-- =============================================
-- 1. CREACIÓN DE TABLAS (INCLUYENDO TABLA RELACIONAL)
-- =============================================

-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(100) NOT NULL,
    es_admin BOOLEAN DEFAULT FALSE
);

-- Crear tabla de dispositivos
CREATE TABLE IF NOT EXISTS dispositivos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL,
    estado INT DEFAULT 0,
    es_esencial BOOLEAN DEFAULT FALSE
);

-- Crear tabla relacional usuario_dispositivo (NUEVA - CLAVE PARA SER RELACIONAL)
CREATE TABLE IF NOT EXISTS usuario_dispositivo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    dispositivo_id INT NOT NULL,
    fecha_asignacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (dispositivo_id) REFERENCES dispositivos(id) ON DELETE CASCADE,
    UNIQUE KEY unique_usuario_dispositivo (usuario_id, dispositivo_id)
);

-- Mostrar confirmación
SELECT 'Base de datos relacional y tablas creadas exitosamente' as '';

-- =============================================
-- 2. INSERCIÓN DE DATOS INICIALES 
-- =============================================

-- TABLA USUARIOS (12 inserts)
INSERT IGNORE INTO usuarios (nombre, contraseña, es_admin) VALUES
-- Usuarios administradores
('admin', 'admin123', TRUE),
('carlos_admin', 'clave123', TRUE),
('mauro_admin', 'admin123', TRUE),

-- Usuarios estándar
('ana_user', 'ana2024', FALSE),
('miguel_user', 'miguelpsw', FALSE),
('sofia_user', 'sofiaaaaa222', FALSE),
('juan_user', 'juanClave', FALSE),
('maria_user', 'maria1234', FALSE),
('pedro_user', 'pedroasd', FALSE),
('lucia_user', 'luciaxd', FALSE),
('diego_user', 'diegosss', FALSE),
('elena_user', 'elena321', FALSE);

-- Mostrar usuarios insertados
SELECT '✅ 12 usuarios insertados' as '';
SELECT COUNT(*) as total_usuarios FROM usuarios;

-- TABLA DISPOSITIVOS (12 inserts)
INSERT IGNORE INTO dispositivos (nombre, estado, es_esencial) VALUES
-- Dispositivos esenciales (críticos para el hogar)
('Alarma Principal', 1, TRUE),
('Cerradura Inteligente', 1, TRUE),
('Sensor Incendio', 0, TRUE),
('Sistema Agua', 0, TRUE),
('Calefacción Central', 0, TRUE),

-- Dispositivos no esenciales (confort)
('Luz Sala', 1, FALSE),
('Luz Cocina', 0, FALSE),
('Aire Acondicionado', 0, FALSE),
('TV Living', 1, FALSE),
('Aspiradora Robot', 0, FALSE),
('Cafetera Inteligente', 0, FALSE),
('Ventilador Dormitorio', 0, FALSE);

-- Mostrar dispositivos insertados
SELECT '✅ 12 dispositivos insertados' as '';
SELECT COUNT(*) as total_dispositivos FROM dispositivos;

-- TABLA RELACIONAL usuario_dispositivo (Asignaciones entre usuarios y dispositivos)
INSERT IGNORE INTO usuario_dispositivo (usuario_id, dispositivo_id) VALUES
-- Usuario admin tiene todos los dispositivos
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12),
-- Otros usuarios tienen dispositivos específicos
(2, 1), (2, 2), (2, 6), (2, 9),
(3, 3), (3, 4), (3, 7),
(4, 5), (4, 8), (4, 10),
(5, 6), (5, 11), (5, 12);

-- Mostrar relaciones insertadas
SELECT '✅ Relaciones usuario-dispositivo insertadas' as '';
SELECT COUNT(*) as total_relaciones FROM usuario_dispositivo;

-- =============================================
-- 3. CONSULTAS MULTITABLA REALES CON JOIN (4 CONSULTAS)
-- =============================================

-- CONSULTA MULTITABLA 1: Usuarios con sus dispositivos asignados (JOIN entre 3 tablas)
-- ESTA ES UNA CONSULTA MULTITABLA REAL CON JOIN
SELECT '=== CONSULTA MULTITABLA 1: USUARIOS Y SUS DISPOSITIVOS (JOIN REAL) ===' as '';
SELECT u.nombre as Usuario, d.nombre as Dispositivo, 
       CASE WHEN d.estado = 1 THEN '🟢 Encendido' ELSE '🔴 Apagado' END as Estado,
       ud.fecha_asignacion as 'Fecha Asignación'
FROM usuario_dispositivo ud
JOIN usuarios u ON ud.usuario_id = u.id
JOIN dispositivos d ON ud.dispositivo_id = d.id
ORDER BY u.nombre, d.nombre;

-- CONSULTA MULTITABLA 2: Dispositivos y los usuarios que los tienen (JOIN REAL)
-- ESTA ES UNA CONSULTA MULTITABLA REAL CON JOIN
SELECT '=== CONSULTA MULTITABLA 2: DISPOSITIVOS Y SUS USUARIOS (JOIN REAL) ===' as '';
SELECT d.nombre as Dispositivo, 
       COUNT(ud.usuario_id) as 'Total Usuarios',
       GROUP_CONCAT(u.nombre) as Usuarios
FROM dispositivos d
LEFT JOIN usuario_dispositivo ud ON d.id = ud.dispositivo_id
LEFT JOIN usuarios u ON ud.usuario_id = u.id
GROUP BY d.nombre
ORDER BY COUNT(ud.usuario_id) DESC;

-- CONSULTA MULTITABLA 3: Usuarios y cantidad de dispositivos que tienen (JOIN REAL)
-- ESTA ES UNA CONSULTA MULTITABLA REAL CON JOIN
SELECT '=== CONSULTA MULTITABLA 3: USUARIOS Y CANTIDAD DE DISPOSITIVOS (JOIN REAL) ===' as '';
SELECT u.nombre as Usuario, 
       COUNT(ud.dispositivo_id) as 'Total Dispositivos',
       CASE WHEN u.es_admin = 1 THEN '👑 Administrador' ELSE '👤 Usuario' END as Rol
FROM usuarios u
LEFT JOIN usuario_dispositivo ud ON u.id = ud.usuario_id
GROUP BY u.nombre, u.es_admin
ORDER BY COUNT(ud.dispositivo_id) DESC;

-- CONSULTA MULTITABLA 4: Dispositivos no asignados a ningún usuario (JOIN REAL)
-- ESTA ES UNA CONSULTA MULTITABLA REAL CON JOIN
SELECT '=== CONSULTA MULTITABLA 4: DISPOSITIVOS SIN ASIGNAR (JOIN REAL) ===' as '';
SELECT d.nombre as 'Dispositivos Sin Asignar',
       CASE WHEN d.estado = 1 THEN '🟢 Encendido' ELSE '🔴 Apagado' END as Estado
FROM dispositivos d
LEFT JOIN usuario_dispositivo ud ON d.id = ud.dispositivo_id
WHERE ud.id IS NULL;

-- =============================================
-- 4. CONSULTAS SIMPLES POR TABLA (2 CONSULTAS)
-- =============================================

-- CONSULTA 1: Lista todos los usuarios
SELECT '=== LISTA COMPLETA DE USUARIOS ===' as '';
SELECT id, nombre, 
       CASE WHEN es_admin = 1 THEN '👑 Administrador' ELSE '👤 Usuario Estándar' END as rol
FROM usuarios
ORDER BY es_admin DESC, nombre;

-- CONSULTA 2: Lista todos los dispositivos con su estado
SELECT '=== INVENTARIO DE DISPOSITIVOS ===' as '';
SELECT id, nombre, 
       CASE WHEN estado = 1 THEN '🟢 ENCENDIDO' ELSE '🔴 APAGADO' END as estado,
       CASE WHEN es_esencial = 1 THEN 'SÍ' ELSE 'NO' END as esencial
FROM dispositivos
ORDER BY es_esencial DESC, estado DESC, nombre;

-- =============================================
-- 5. SUBCONSULTAS (2 SUBCONSULTAS)
-- =============================================

-- SUBCONSULTA 1: Dispositivos con estado superior al promedio
SELECT '=== DISPOSITIVOS CON ESTADO SUPERIOR AL PROMEDIO ===' as '';
SELECT nombre, 
       estado,
       'POR ENCIMA DEL PROMEDIO' as observacion
FROM dispositivos 
WHERE estado > (
    SELECT AVG(estado) 
    FROM dispositivos
    WHERE es_esencial = FALSE
)
AND es_esencial = FALSE
ORDER BY estado DESC;

-- SUBCONSULTA 2: Dispositivos esenciales que siempre deben estar encendidos
SELECT '=== DISPOSITIVOS CRÍTICOS QUE DEBEN ESTAR ACTIVOS ===' as '';
SELECT nombre, 
       CASE WHEN estado = 1 THEN 'CORRECTO' ELSE 'REVISAR URGENTE' END as estado_actual,
       '🔐 SEGURIDAD' as prioridad
FROM dispositivos 
WHERE es_esencial = TRUE 
AND nombre IN (
    SELECT nombre 
    FROM dispositivos 
    WHERE nombre LIKE '%Alarma%' OR nombre LIKE '%Sensor%' OR nombre LIKE '%Cerradura%'
);

-- =============================================
-- 6. REPORTE EJECUTIVO CON DATOS RELACIONALES
-- =============================================

SELECT '=== REPORTE EJECUTIVO - SISTEMA SMART HOME RELACIONAL ===' as '';
SELECT 
    'Estado del Sistema' as seccion,
    'BASE DE DATOS RELACIONAL ACTIVA' as resultado
UNION ALL
SELECT 
    'Usuarios Registrados',
    CONCAT((SELECT COUNT(*) FROM usuarios), ' usuarios')
UNION ALL
SELECT 
    'Dispositivos Activos', 
    CONCAT((SELECT COUNT(*) FROM dispositivos WHERE estado = 1), '/', (SELECT COUNT(*) FROM dispositivos), ' encendidos')
UNION ALL
SELECT 
    'Relaciones Usuario-Dispositivo',
    CONCAT((SELECT COUNT(*) FROM usuario_dispositivo), ' asignaciones activas')
UNION ALL
SELECT 
    'Promedio Dispositivos por Usuario',
    CONCAT(ROUND((SELECT COUNT(*) FROM usuario_dispositivo) * 1.0 / (SELECT COUNT(*) FROM usuarios), 1), ' dispositivos/usuario');

-- =============================================
-- ✅ RESUMEN FINAL - BASE DE DATOS RELACIONAL
-- =============================================

SELECT 'SCRIPT DE BASE DE DATOS RELACIONAL EJECUTADO EXITOSAMENTE' as '';
SELECT 'Resumen final del sistema relacional:' as '';
SELECT 
    (SELECT COUNT(*) FROM usuarios) as total_usuarios,
    (SELECT COUNT(*) FROM dispositivos) as total_dispositivos,
    (SELECT COUNT(*) FROM usuario_dispositivo) as total_relaciones,
    (SELECT COUNT(*) FROM (SELECT 1 FROM usuarios UNION SELECT 1 FROM dispositivos UNION SELECT 1 FROM usuario_dispositivo) as t) as total_registros;