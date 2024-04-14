DELETE FROM Corporation;
DELETE FROM Software;
DELETE FROM Versions;

-- Вставка данных в таблицу Corporation
INSERT INTO Corporation (id_c, name, year) VALUES
(1, 'Microsoft', 1975),
(2, 'Apple Inc.', 1976),
(3, 'Google', 1998);

-- Вставка данных в таблицу Software
INSERT INTO Software (id_s, name, developer) VALUES
(1, 'Windows', 1),
(2, 'Office', 1),
(3, 'macOS', 2),
(4, 'iOS', 2),
(5, 'Android', 3);

-- Вставка данных в таблицу Versions
INSERT INTO Versions (id_v, version, soft_name) VALUES
(1, '10.0', 1),
(2, '11.0', 1),
(3, '12.0', 2),
(4, '13.0', 2),
(5, '11.0', 3),
(6, '12.0', 3),
(7, '14.0', 4),
(8, '15.0', 4),
(9, '11.0', 5),
(10, '12.0', 5);