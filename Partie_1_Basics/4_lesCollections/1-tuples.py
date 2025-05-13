# Les tuples

# Un tuple est une structure de données comme une liste, 
# mais contrairement à une liste, il ne peut pas être modifié une fois créé (il est "immuable").
# On le crée avec des parenthèses : ("valeur1", "valeur2", "valeur3")

personnes = ("Mélanie", "Jean", "Abdel", "Leo")  # Déclaration d'un tuple contenant 4 prénoms

# On affiche le nombre d'éléments dans le tuple
print(len(personnes))  # Résultat : 4

# On affiche le premier élément du tuple (indice 0)
print(personnes[0])  # Résultat : "Mélanie"

print("")  # Ligne vide pour aérer l'affichage

# On parcourt chaque prénom du tuple grâce à une boucle for
for i in personnes:
    print(i)           # Affiche le prénom
    print(len(i))      # Affiche le nombre de lettres du prénom
    print(i[1])        # Affiche la 2ème lettre du prénom (indice 1, car ça commence à 0)

##############################################
# Exercice : Les Tuples et l'accès aux caractères

# Vous avez un tuple nommé `animaux` contenant plusieurs noms d’animaux :
#    ("girafe", "tigre", "panda", "zèbre", "lion")

# Votre objectif est de faire un programme qui :

# - Affiche le nombre total d’animaux dans le tuple
# - Affiche chaque animal, un par un

# Pour chaque animal :
#   - Affiche son nom
#   - Affiche le nombre de lettres de son nom
#   - Affiche la dernière lettre de son nom

# Indice : Pour accéder à la dernière lettre d’un mot : soit `mot[-1]` soit `mot[len(mot)-1]`

##############################################
    