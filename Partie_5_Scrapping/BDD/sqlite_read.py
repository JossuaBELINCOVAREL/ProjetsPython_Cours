import sqlite3

connexion = sqlite3.connect("albums2.db")
curseur = connexion.cursor()

curseur.execute("SELECT * FROM artistes")
var_artistes = curseur.fetchall() # -> Récupérer tous les enregistrements (ici listes des artistes) dans une variable
print(var_artistes)

# équivalent :
    # for artistes in curseur.execute("SELECT * FROM artistes"):
    #     print(artistes)

# Autre possibilité aussi :
albums_cd = curseur.execute('SELECT titre FROM albums var1 JOIN artistes var2 ON var1.artiste_id = var2.artiste_id AND var2.nom = "Celine Dion"').fetchall()
print(albums_cd)

connexion.close()