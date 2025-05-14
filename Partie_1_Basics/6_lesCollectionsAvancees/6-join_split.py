# Join & Split : Coller et Séparer des chaînes

# Liste de prénoms
noms = ["Jean", "Eva", "Sophie", "Martin"]

# JOIN -> Permet de "coller" tous les éléments d'une liste avec un séparateur

# On colle les prénoms avec un tiret "-"
noms_join = "-".join(noms)
print(noms_join)  # Résultat : Jean-Eva-Sophie-Martin

# On colle les prénoms avec " et "
noms_join = " et ".join(noms)
print(noms_join)  # Résultat : Jean et Eva et Sophie et Martin

# SPLIT -> Permet de "séparer" une chaîne de caractères en une liste, selon un séparateur

# Exemple 1 : séparer une chaîne où les éléments sont séparés par une virgule et un espace
a = "Paul, Marc, Emilie"
a_split = a.split(", ")
print(a_split)  # Résultat : ['Paul', 'Marc', 'Emilie']

# Exemple 2 : séparer une chaîne où les éléments sont séparés par un tiret "-"
a = "Paul-Marc-Emilie"
a_split = a.split("-")
print(a_split)  # Résultat : ['Paul', 'Marc', 'Emilie']

##############################################
# Exercice : Reformater une liste d'éléments

# Demande à l'utilisateur d'écrire plusieurs prénoms séparés par une virgule.
# Transforme cette chaîne en une liste (avec .split).
# Affiche la liste.
# Recolle la liste avec " / " comme séparateur (avec .join).
# Affiche le résultat.


##############################################
