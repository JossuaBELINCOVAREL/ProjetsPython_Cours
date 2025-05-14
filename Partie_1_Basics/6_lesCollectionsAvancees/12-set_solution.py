# Liste de films avec doublons
films = ["Avengers", "Batman", "Superman", "Spiderman", "Batman", "Avengers"]

# Étape 1 : Convertir la liste en un set pour supprimer les doublons
films_sans_doublons = set(films)

# Étape 2 : Afficher le set résultant
print("Films sans doublons :")
print(films_sans_doublons)

# Étape 3 : Créer un set avec les genres de films
genres = {"Action", "Science-fiction", "Animation", "Action", "Super-héros"}

# Afficher le set des genres de films
print("\nGenres de films :")
print(genres)

# Étape 4 : Utiliser une boucle for pour afficher chaque genre
print("\nAffichage des genres de films :")
for genre in genres:
    print(genre)
