-- Insertar datos
INSERT INTO usuarios (nombre, password, es_admin) VALUES
('admin', 'admin123', TRUE),
('mauro', 'clave123', FALSE),
('agustin', 'clave456', FALSE);

INSERT INTO dispositivos (nombre, estado, es_esencial) VALUES
('Tele', 1, FALSE),
('Heladera', 1, TRUE),
('Computadora', 0, FALSE),
('Router', 1, TRUE),
('Lampara comedor', 1, FALSE),
('Lampara Pieza', 0, FALSE),
('Aire Acondicionado', 1, FALSE),
('Ventilador', 0, FALSE),
('Microondas', 0, FALSE),
('Estufa', 0, TRUE),
('Lavarropas', 1, FALSE),
('Secarropas', 0, FALSE),
('Aspiradora Robot', 1, FALSE),
('Cafetera', 0, FALSE),
('Horno Electrico', 1, FALSE),
('PlayStation', 0, FALSE),
('Impresora', 1, FALSE),
('Luz Patio', 0, TRUE),
('Calefactor', 1, TRUE);

INSERT INTO automatizaciones (nombre, tipo) VALUES
('Modo Ahorro', 'Energia');

INSERT INTO automatizacion_dispositivo (id_automatizacion, id_dispositivo) VALUES
(1, 1),
(1, 3),
(1, 5),
(1, 6),
(1, 7),
(1, 8),
(1, 9),
(1, 18);

-- Todas las tablas
SELECT * FROM usuarios;
SELECT * FROM dispositivos;
SELECT * FROM automatizaciones;
SELECT * FROM automatizacion_dispositivo;

-- Dispositivos Prendidos
SELECT nombre 
FROM dispositivos 
WHERE estado = 1 
ORDER BY nombre;

-- Dispositivos esenciales
SELECT nombre 
FROM dispositivos 
WHERE es_esencial = 1 
ORDER BY nombre;