# Trouver la valeur la plus petite
# Afficher le noms associé
# Sans changer la liste, ce qui est aussi possible.

# Version simple

noms = ["Pierre", "Paul", "Eva", "Julie", "Léo"]
distance_chauffeurs = [1.6, 1.5, 0.3, 1.9, 3.8]

index_min = 0
distance_min = distance_chauffeurs[0]

for index in range(len(distance_chauffeurs)):
    if distance_chauffeurs[index] < distance_chauffeurs[index_min]:
        index_min = index

for distance in distance_chauffeurs:
    if distance < distance_min:
        distance_min = distance

print(f"L'index minimum est le : {index_min}")
print(f"La distance minimum est de : {distance_min}")
print(f"Le chauffeur le plus proche est : {noms[index_min]}")


# Version avancée
""" 

noms_distance = [("Pierre", 1.6), ("Paul", 1.5), ("Eva", 2.3)]

result = noms_distance[0]
for nom_distance in noms_distance:
    if nom_distance[1] < result[1]:
        result = nom_distance

print(f"Distance minimale : {result[1]} et son nom est {result[0]}")


"""

