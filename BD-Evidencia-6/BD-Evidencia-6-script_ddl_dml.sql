
-- SISTEMA SMART HOME
-- CREACIÓN DE LA BASE DE DATOS Y TABLAS

-- Crear base de datos
CREATE DATABASE IF NOT EXISTS smarthome;
USE smarthome;

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

-- Mostrar confirmación
SELECT '✅ Base de datos y tablas creadas exitosamente' as '';

-- =============================================
-- 1. INSERCIÓN DE DATOS INICIALES 
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


-- 2. CONSULTAS SIMPLES POR TABLA


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


-- 3. CONSULTAS MULTITABLA (4 consultas útiles)

-- CONSULTA MULTITABLA 1: Dispositivos esenciales que están apagados
-- Propósito: Identificar dispositivos críticos que necesitan atención
-- Justificación: Para el modo de ahorro energético, es importante saber
-- qué dispositivos esenciales están apagados y podrían necesitar encenderse
SELECT '=== DISPOSITIVOS ESENCIALES APAGADOS (CRÍTICOS) ===' as '';
SELECT d.nombre, 
       'APAGADO' as estado,
       'REVISAR URGENTE' as accion
FROM dispositivos d
WHERE d.es_esencial = TRUE AND d.estado = 0;

-- CONSULTA MULTITABLA 2: Resumen estadístico del sistema
-- Propósito: Dashboard con métricas clave del sistema
-- Justificación: Para administradores que necesitan ver el estado general
SELECT '=== RESUMEN ESTADÍSTICO DEL SISTEMA ===' as '';
SELECT 
    'Total Usuarios' as metricas,
    (SELECT COUNT(*) FROM usuarios) as valor
UNION ALL
SELECT 
    'Administradores',
    (SELECT COUNT(*) FROM usuarios WHERE es_admin = TRUE)
UNION ALL
SELECT 
    'Total Dispositivos', 
    (SELECT COUNT(*) FROM dispositivos)
UNION ALL
SELECT 
    'Dispositivos Esenciales',
    (SELECT COUNT(*) FROM dispositivos WHERE es_esencial = TRUE)
UNION ALL
SELECT 
    'Dispositivos Encendidos',
    (SELECT COUNT(*) FROM dispositivos WHERE estado = 1)
UNION ALL
SELECT 
    'Eficiencia Energética',
    CONCAT(ROUND((SELECT COUNT(*) FROM dispositivos WHERE estado = 0) * 100.0 / 
          (SELECT COUNT(*) FROM dispositivos), 1), '%');

-- 🔗 CONSULTA MULTITABLA 3: Dispositivos no esenciales encendidos
-- Propósito: Identificar oportunidades de ahorro energético
-- Justificación: Para el modo de ahorro, apagar estos dispositivos reduce consumo
SELECT '=== DISPOSITIVOS NO ESENCIALES ENCENDIDOS (OPORTUNIDAD DE AHORRO) ===' as '';
SELECT d.nombre,
       'CONSUMIENDO ENERGÍA' as situacion,
       'CONSIDERAR APAGAR' as recomendacion
FROM dispositivos d
WHERE d.es_esencial = FALSE AND d.estado = 1;

-- 🔗 CONSULTA MULTITABLA 4: Análisis de eficiencia energética
-- Propósito: Reporte de eficiencia para toma de decisiones
-- Justificación: Los administradores necesitan métricas de eficiencia
SELECT '=== ANÁLISIS DE EFICIENCIA ENERGÉTICA ===' as '';
SELECT 
    'Dispositivos Esenciales' as categoria,
    COUNT(*) as total,
    SUM(CASE WHEN estado = 1 THEN 1 ELSE 0 END) as encendidos,
    ROUND(SUM(CASE WHEN estado = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as porcentaje_encendidos
FROM dispositivos WHERE es_esencial = TRUE
UNION ALL
SELECT 
    'Dispositivos No Esenciales',
    COUNT(*),
    SUM(CASE WHEN estado = 1 THEN 1 ELSE 0 END),
    ROUND(SUM(CASE WHEN estado = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2)
FROM dispositivos WHERE es_esencial = FALSE;

-- =============================================
-- 🔍 4. SUBCONSULTAS (2 subconsultas útiles)
-- =============================================

-- 🔍 SUBCONSULTA 1: Dispositivos con estado superior al promedio
-- Propósito: Identificar dispositivos que consumen más energía de lo normal
-- Justificación: Para optimizar el consumo energético del hogar
SELECT '=== DISPOSITIVOS CON ESTADO SUPERIOR AL PROMEDIO ===' as '';
SELECT nombre, 
       estado,
       'POR ENCIMA DEL PROMEDIO' as observacion
FROM dispositivos 
WHERE estado > (
    SELECT AVG(estado) 
    FROM dispositivos
    WHERE es_esencial = FALSE  -- Solo considerar no esenciales para el promedio
)
AND es_esencial = FALSE
ORDER BY estado DESC;

-- 🔍 SUBCONSULTA 2: Dispositivos esenciales que siempre deben estar encendidos
-- Propósito: Verificar dispositivos críticos que deberían estar activos
-- Justificación: Seguridad del hogar - algunos dispositivos son críticos
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
-- 🎯 CONSULTA EXTRA: Reporte ejecutivo consolidado
-- =============================================

SELECT '===  REPORTE EJECUTIVO - SISTEMA SMART HOME ===' as '';
SELECT 
    'Estado del Sistema' as seccion,
    'ÓPTIMO' as resultado
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
    'Eficiencia Energética',
    CONCAT(ROUND((SELECT COUNT(*) FROM dispositivos WHERE estado = 0) * 100.0 / 
          (SELECT COUNT(*) FROM dispositivos), 1), '% de ahorro potencial');

-- =============================================
-- ✅ RESUMEN FINAL
-- =============================================

SELECT 'SCRIPT EJECUTADO EXITOSAMENTE' as '';
SELECT 'Resumen final:' as '';
SELECT 
    (SELECT COUNT(*) FROM usuarios) as total_usuarios,
    (SELECT COUNT(*) FROM dispositivos) as total_dispositivos,
    (SELECT COUNT(*) FROM (SELECT 1 FROM usuarios UNION SELECT 1 FROM dispositivos) as t) as total_registros;