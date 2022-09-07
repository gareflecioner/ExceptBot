CREATE DATABASE bd;
CREATE TABLE books("Id" BIGSERIAL PRIMARY KEY,
"Title" VARCHAR(50) NOT NULL,
"Author" VARCHAR NOT NULL,
"Year" INTEGER);
INSERT INTO books(
Title, Author, Year)
VALUES ("War and peace","Tolstoy","1863"),
("Crime and punishment","Dostoevsky","1866"),
("Teresa Zboncak","Vandervort","1556"),
("Luis Tromp", "Mills","1756"),
("Wilhelm Romaguera","Harber","456"),
("Hans Mann","O'Keefe","1986"),
("Misael Ortiz","Mann","1256"),
("Genry Genius","About","1454");
SELECT * FROM books
