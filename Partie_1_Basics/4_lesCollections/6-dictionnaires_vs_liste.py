# Ce programme illustre la différence entre une liste et un dictionnaire pour rechercher des informations sur une personne

# ----------------------------------------
# Recherche avec une LISTE
# ----------------------------------------

# Fonction pour chercher une personne dans une liste de tuples
def obtenir_informations(nom, liste):
    for i in liste:                  # On parcourt chaque élément de la liste
        if i[0] == nom:              # Si le nom correspond à celui qu'on cherche
            return i                 # On retourne le tuple entier (nom, âge, taille)
    return None                      # Si on ne trouve pas, on retourne "None"

# Liste de personnes, chaque élément est un tuple (nom, âge, taille)
personnes = [("Julie", 25, 1.6), ("Eva", 20, 1.67), ("Tom", 45, 1.54), ("Léo", 19, 1.7)]

# On cherche les infos de "Eva"
infos = obtenir_informations("Eva", personnes)
print(infos)  # Affiche : ("Eva", 20, 1.67)

# ----------------------------------------
# Recherche avec un DICTIONNAIRE
# ----------------------------------------

# Dictionnaire de personnes : chaque nom est une clé, la valeur est un tuple (âge, taille)
personnes_dictionnaire = {
    "Julie": (25, 1.6),
    "Eva": (20, 1.67),
    "Tom": (45, 1.54),
    "Léo": (19, 1.7)
}

# On utilise .get() pour récupérer les infos associées à "Eva"
infos_dictionnaire = personnes_dictionnaire.get("Eva")

# Vérifie si le nom existe dans le dictionnaire
if infos_dictionnaire == None:
    print("La clef n'existe pas")  # Si le nom n'est pas trouvé
else:
    print(infos_dictionnaire)      # Sinon, on affiche le tuple trouvé

##############################################
# Exercice : Fiche contact

# Crée une liste de contacts, chaque contact étant un tuple contenant :
# - prénom
# - numéro de téléphone
# - ville

# Crée une fonction qui prend en paramètre un prénom et retourne les informations de ce contact à partir de la liste

# Reproduis ensuite la même logique mais avec un dictionnaire :
# - La clé sera le prénom
# - La valeur sera un tuple contenant le numéro et la ville

# Affiche les informations d’un contact (au choix) en utilisant les 2 méthodes

##############################################
