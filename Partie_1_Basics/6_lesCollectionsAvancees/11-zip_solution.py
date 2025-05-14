# Liste des films et des notes
films = ["Inception", "Avatar", "Titanic", "The Dark Knight"]
notes = [8.8, 7.8, 7.5, 9.0]

# Étape 1 : Créer une liste de tuples avec zip
films_notes = list(zip(films, notes))

# Étape 2 : Afficher chaque film avec sa note
for (titre, note) in films_notes:
    print(f"{titre} - {note}/10")

print()  # Ligne vide pour plus de clarté

# Étape 3 : Dézipper les films et les notes
films_dézip, notes_dézip = zip(*films_notes)

# Afficher les deux nouvelles listes
print("Films:", films_dézip)
print("Notes:", notes_dézip)
