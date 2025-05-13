animaux = ("girafe", "tigre", "panda", "zèbre", "lion")

# 1. Affiche le nombre total d’animaux
print(f"Nombre d’animaux : {len(animaux)}")
print("")

# 2. Boucle sur chaque animal
for animal in animaux:
    print(f"Nom de l’animal : {animal}")
    print(f"Nombre de lettres : {len(animal)}")
    print(f"Dernière lettre : {animal[-1]}")
    print("")  # Ligne vide pour séparer les affichages
