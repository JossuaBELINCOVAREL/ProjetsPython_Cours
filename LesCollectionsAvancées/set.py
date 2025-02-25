# Dans un set, chaque élément doit être unique et immuable , c’est-à- dire qu'il ne peut pas être modifié. 
# En revanche, le set en lui-même peut être modifié
# Comme les dictionnaires, les sets sont des collections d'éléments non-ordonnées.
# Souvent utilisés pour contrôler les doublons et effectuer des opérations sur les ensembles comme les unions, les différences, etc.

'''noms = ["Marie", "Paul", "Jean", "Marc", "Emilie", "Marie"]
noms_sans_doublons = list(set(noms))
print(noms_sans_doublons)
print(noms_sans_doublons[0])'''

set_noms = { "Marie", "Paul", "Jean", "Marc", "Emilie", "Marie" }
print(set_noms)

# for s in set_noms:
#     print(s)