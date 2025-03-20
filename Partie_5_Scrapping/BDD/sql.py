"""
LEs bases de données SQL 
Possibilité de stocker, organiser, associé et y accéder
Utilisiation de serveurs

Organisation des données :
-> Création de tables (Artiste et Albums)
-> Création des associations via des ID
-> Création des relations entre les tables (One to many ou Many to many)
    -> On to many : un artiste peut avoir plusieurs albums
    -> Many to many : Un étudiant peut s'inscrire à plusieurs cours et chaque cours est suvi par un ou plusieurs étudiants
    -> One to one : Une personne à un casier judiciaire et chaque casier est personnel

Utilisation du langage SQL :
-> Création de la base de données -> CREATE DATABASE
-> Création des tables -> CREATE TABLE
-> Ajout des données -> INSERT INTO
-> Modification des données -> UPDATE
-> Suppression des données -> DELETE
-> Récupérer les données -> SELECT

-> VARCHAR correspond au texte (str)
-> INTEGER correspond au nombre (int)


Exemple avec Artistes et Albums :
artiste : artiste_id, nom
album : album_id, artiste_id,titre, date_sortie 

CREATE TABLE artistes (
    artiste_id INTEGER NOT NULL PRIMARY KEY,
    nom VARCHAR(255)
);

CREATE TABLE albums (
    album_id INTEGER NOT NULL PRIMARY KEY,
    artiste_id INTEGER REFERENCES artistes(artiste_id),
    titre VARCHAR(255),
    date_sortie INTEGER
);

INSERT INTO artiste (nom) VALUES ("Michael Jackson");
INSERT INTO albums (artiste_id, titre, date_sortie) VALUES (1, "Thriller", 1982);

UPDATE album SET date_sortie = 1986 WHERE titre = "Thriller"; -> Modifier la date de sortie de Thriller

DELETE FROM albums WHERE nom = "Michael Jackson"; -> Supprimer tous les albums de Michael Jackson
DELETE FROME albums WHERE titre = "Thriller"; -> Supprimer Thriller

SELECT * FROM artistes
SELECT nom FROM artistes
SELECT * FROM artistes WHERE date_sortie > 1990

SELECT nom, titre FROM albums var1 JOIN artistes var2 ON var1.artiste_id = var2.artiste_id  -> Jointure pour associer les deux tables (afficher le nom de l'artiste et le titre de l'album)
SELECT titre FROM albums var1 JOIN artistes var2 ON var1.artiste_id = var2.artiste_id AND var2.nom = "Michael Jackson" -> Afficher tous les albums de Michael Jackson

"""