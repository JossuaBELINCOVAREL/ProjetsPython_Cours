# Création d'un script pour créer la base de données

import sqlite3

# connexion = "albums2.db"
# executer / curseur
# commit
# fermer

connexion = sqlite3.connect("albums2.db")
curseur = connexion.cursor() # permet de passer par un objet intermédiaire pour communiquer avec la base de données

curseur.execute("""CREATE TABLE artistes (
    artiste_id INTEGER NOT NULL PRIMARY KEY,
    nom VARCHAR(50)
    );""") # Passage de la requête SQL

curseur.execute("""CREATE TABLE albums (
    album_id INTEGER NOT NULL PRIMARY KEY,
    artiste_id INTEGER REFERENCES artistes(artiste_id),
    titre VARCHAR(255),
    date_sortie INTEGER
);""")

curseur.execute("""INSERT INTO artistes (artiste_id, nom) VALUES (1, "Michael Jackson");""")
mj_id = curseur.lastrowid
curseur.execute("""INSERT INTO artistes (artiste_id, nom) VALUES (2, "Celine Dion");""")
cd_id = curseur.lastrowid

curseur.execute("INSERT INTO albums (album_id, artiste_id, titre, date_sortie) VALUES (?, ?, ?, ?);", 
                (1, mj_id, "Thriller", 1982))
curseur.execute("INSERT INTO albums (album_id, artiste_id, titre, date_sortie) VALUES (?, ?, ?, ?);", 
                (2, cd_id, "Let's Talk About Love", 1997))
curseur.execute("INSERT INTO albums (album_id, artiste_id, titre, date_sortie) VALUES (?, ?, ?, ?);", 
                (3, cd_id, "Falling into You", 1996))

# Utilisation de ? dans execute() : permet d'éviter les injections SQL et les erreurs de conversion.
# Les valeurs de type TEXT en SQL doivent être entre apostrophes ('), mais ici, SQLite s'en occupe automatiquement grâce aux ?.

connexion.commit() # Envoi de la requête SQL
connexion.close()

