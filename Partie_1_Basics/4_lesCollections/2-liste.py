# Les LISTES en Python

# Une liste (comme un tableau) peut contenir plusieurs valeurs
# Elle est "mutable" : on peut modifier son contenu (ajouter, supprimer, changer un élément)
# On la crée avec des crochets []

personnes = ["Mélanie", "Jean", "Abdel", "Leo"]  # Création d'une liste avec 4 prénoms
nv_personne = "David"  # Nouvelle personne à ajouter à la liste

# Affiche la liste actuelle
print(personnes)

# On ajoute une nouvelle personne à la fin de la liste
personnes.append(nv_personne)
print(personnes)

# On supprime la personne à l’indice 1 (deuxième élément → "Jean")
del personnes[1]
print(personnes)

print("")  # Ligne vide pour aérer l'affichage


# Fonction qui affiche les éléments d'une liste
def afficher_personnes(c):
    for i in c:
        print(i)


# Fonction qui modifie la première valeur d'une liste
def modifier_valeur(a):
    a[0] = 10  # Attention ! On modifie la valeur de la liste directement (car elle est mutable)

# Création d’une liste de chiffres
test = [1, 2, 3, 4, 5]
print(test)

# On modifie cette liste avec la fonction précédente
modifier_valeur(test)
print(test)  # La première valeur est maintenant 10

print("")  # Ligne vide pour aérer

# On affiche les prénoms de la liste "personnes"
afficher_personnes(personnes)

##############################################
# Exercice : Gestion d'une liste de nombres

# Vous devez créer un programme qui gère une liste de notes d’élèves.

# Le programme doit :

# - Créer une liste appelée `notes` contenant les valeurs suivantes : 12, 15, 9, 18, 13
# - Ajouter une note supplémentaire (demandez à l’utilisateur de la saisir)
# - Supprimer la première note (celle à l’indice 0)
# - Créer une fonction `afficher_notes` qui affiche toutes les notes une par une
# - Créer une fonction `modifier_note` qui modifie la dernière note en 20
# - Appeler les deux fonctions pour voir les résultats

# Indice : N’oubliez pas que les listes sont mutables : elles se modifient dans les fonctions directement

##############################################
    