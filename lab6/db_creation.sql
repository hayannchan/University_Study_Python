CREATE TABLE IF NOT EXISTS Corporation (
id_c INTEGER PRIMARY KEY,
name TEXT NOT NULL,
year INTEGER NOT NULL
);
               
CREATE TABLE IF NOT EXISTS Software (
id_s INTEGER PRIMARY KEY,
name TEXT NOT NULL,
developer INTEGER NOT NULL,
FOREIGN KEY(developer) REFERENCES Corporation(id_c)
);
               
CREATE TABLE IF NOT EXISTS Versions (
id_v INTEGER PRIMARY KEY,
version TEXT NOT NULL,
soft_name INTEGER NOT NULL,
FOREIGN KEY(soft_name) REFERENCES Software(id_s)
);