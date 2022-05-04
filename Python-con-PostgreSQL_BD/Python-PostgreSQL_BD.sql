create user usuario with encrypted password 'asdasd'; 
grant all privileges on database Proyecto-Python to usuario;

create database Proyecto-Python;
psql
\c Proyecto-Python

CREATE TABLE SOCIOS (
    DNI VARCHAR (10) PRIMARY KEY NOT NULL,
    Nombre VARCHAR (20) NOT NULL,
    Direccion VARCHAR (20)
);

CREATE TABLE PELICULAS (
    RefPelicula VARCHAR (10) PRIMARY KEY NOT NULL,
    NombrePelicula VARCHAR (20) NOT NULL,
    Genero VARCHAR (20) NOT NULL,
    Director VARCHAR (20),
    AnoEstreno VARCHAR(4),
    Nacionalidad VARCHAR (20) NOT NULL
);

CREATE TABLE PRESTAMOS (
    DNI_fk VARCHAR (10) NOT NULL,
    RefPelicula_fk VARCHAR (10) NOT NULL,
    FechaPrestamo DATE NOT NULL,
    Importe INTEGER NOT NULL DEFAULT 400,
    CONSTRAINT pri PRIMARY KEY (DNI_fk,RefPelicula_fk,FechaPrestamo),
    CONSTRAINT DNI_ajena FOREIGN KEY (DNI_fk) REFERENCES SOCIOS(DNI),
    CONSTRAINT RefPelicula_ajena FOREIGN KEY (RefPelicula_fk) REFERENCES PELICULAS(RefPelicula)
);

INSERT INTO SOCIOS VALUES ('111-A','David','Sevilla Este');
INSERT INTO SOCIOS VALUES ('222-B','Mariano','Los Remedios');
INSERT INTO SOCIOS VALUES ('333-C','Raul','Triana');
INSERT INTO SOCIOS VALUES ('444-D','Rocio','La Oliva');
INSERT INTO SOCIOS VALUES ('555-E','Marilo','Triana');
INSERT INTO SOCIOS VALUES ('666-F','Benjamin','Montequinto');
INSERT INTO SOCIOS VALUES ('777-G','Carlos','Los Remedios');
INSERT INTO SOCIOS VALUES ('888-H','Manolo','Montequinto');

INSERT INTO PELICULAS VALUES ('CF-1','Dune','Ciencia-ficcion','Edwards','1984','Estadounidense');
INSERT INTO PELICULAS VALUES ('D-1','Los Idiotas','Drama','Von Trier','1999','Sueca');
INSERT INTO PELICULAS VALUES ('D-2','Kramer vs Kramer','Drama','Smith','1978','Estadounidense');
INSERT INTO PELICULAS VALUES ('CF-2','Mision Imposible','Ciencia-ficcion','Johnson','1998','Estadounidense');
INSERT INTO PELICULAS VALUES ('D-3','Mi nombre es Joe','Drama','Loach','1995','Britanica');
INSERT INTO PELICULAS VALUES ('D-4','Rompiendo las olas','Drama','Von Trier','1997','Sueca');
INSERT INTO PELICULAS VALUES ('S-1','Los Otros','Suspense','Amenabar','2001','Española');

INSERT INTO PRESTAMOS VALUES ('111-A','CF-1','2018-10-01',350);
INSERT INTO PRESTAMOS VALUES ('333-C','D-1','2019-11-01',300);
INSERT INTO PRESTAMOS VALUES ('111-A','S-1','2020-11-01',400);
INSERT INTO PRESTAMOS VALUES ('444-D','S-1','2019-11-01',400);
INSERT INTO PRESTAMOS VALUES ('111-A','D-3','2014-11-01',300);
INSERT INTO PRESTAMOS VALUES ('777-G','S-1','2019-11-01',400);
INSERT INTO PRESTAMOS VALUES ('888-H','D-2','2016-11-01',500);
INSERT INTO PRESTAMOS VALUES ('222-B','CF-2','2015-11-01',400);
INSERT INTO PRESTAMOS VALUES ('555-E','D-4','2017-11-01',400);
INSERT INTO PRESTAMOS VALUES ('333-C','D-3','2020-11-01',400);
INSERT INTO PRESTAMOS VALUES ('333-C','D-4','2020-11-01',500);