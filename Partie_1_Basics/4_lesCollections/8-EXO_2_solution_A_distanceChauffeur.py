# Version simple : deux listes séparées

noms = ["Pierre", "Paul", "Eva", "Julie", "Léo"]
distance_chauffeurs = [1.6, 1.5, 0.3, 1.9, 3.8]

# On suppose au départ que le plus proche est le premier
index_min = 0
distance_min = distance_chauffeurs[0]

# On parcourt la liste pour trouver le plus petit
for index in range(len(distance_chauffeurs)):
    if distance_chauffeurs[index] < distance_chauffeurs[index_min]:
        index_min = index

# On récupère la distance minimale grâce à l’index trouvé
distance_min = distance_chauffeurs[index_min]

# On affiche le nom et la distance minimale
print(f"Le chauffeur le plus proche est {noms[index_min]} avec une distance de {distance_min} km")


