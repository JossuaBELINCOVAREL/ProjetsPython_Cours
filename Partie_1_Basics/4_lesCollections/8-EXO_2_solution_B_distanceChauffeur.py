# Version avancée : liste de tuples (nom, distance)

noms_distance = [("Julie", 1.6), ("Paul", 1.5), ("Eva", 2.3)]

result = noms_distance[0]
for nom_distance in noms_distance:
    if nom_distance[1] < result[1]:
        result = nom_distance

print(f"Distance minimale : {result[1]} et son nom est {result[0]}")


