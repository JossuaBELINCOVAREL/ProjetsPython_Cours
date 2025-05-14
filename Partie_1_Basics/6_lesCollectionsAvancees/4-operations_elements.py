# Quelques fonctions utiles sur les listes :
# min(), max(), in, sum()

# Liste de prénoms (chaînes de caractères)
noms = ["Jean", "Eva", "Sophie", "Martin"]

# Liste d'âges (nombres entiers)
ages = [21, 32, 4, 56]

# min() -> retourne la valeur la plus petite dans la liste
print("Âge minimum :", min(ages))  # ici : 4

# min() avec une liste de chaînes -> compare selon l’ordre alphabétique
print("Nom en premier (ordre alphabétique) :", min(noms))  # ici : "Eva"

# in -> permet de vérifier si une valeur est présente dans une liste

if "Eva" in noms:
    print("✅ Eva est présente dans la liste")
else:
    print("❌ Eva est absente")

# Attention : sensible à la casse (majuscule/minuscule)
if "eva" in noms:
    print("✅ eva est présente")
else:
    print("❌ eva est absente")  # ici c’est False car "eva" ≠ "Eva"

# sum() -> fait la somme de tous les éléments numériques d’une liste
print("Somme des âges :", sum(ages))  # ici : 113

# Fonctionne uniquement si tous les éléments sont des nombres !

##############################################
# Exercice : Statistiques sur des notes

# Tu disposes de la liste suivante : notes = [12, 15, 8, 19, 7, 14]

# Affiche la note minimale.
# Affiche la note maximale.
# Affiche la moyenne des notes.

# Demande à l’utilisateur de rentrer une note : 
#   - Vérifie si cette note est présente dans la liste.
#   - Affiche un message selon le cas.

##############################################
