noms = ["Jean", "Eva", "Sophie", "Martin"]

print(noms[0:3])
print(noms[:3])

# intégralité de la liste : 

print(noms[:])

# Attention, différent avec ou sans [] même s'il ressort la liste complète
# Si il y a changement, ça modifie avec [] et pas sans

slice_noms = noms[:]

slice_noms[0] = "Abdul"

print(slice_noms)
print(noms)

# slice_noms fait une copie, le changhemennt de la liste "noms" ne sera pas altéré


