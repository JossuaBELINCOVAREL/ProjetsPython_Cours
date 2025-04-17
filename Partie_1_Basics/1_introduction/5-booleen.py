# Fonction qui affiche des informations en fonction de l'âge de la personne

def afficher_info_personne(nom, age): # Affiche les informations de base (nom et âge actuel, âge de l'année prochaine)
    print("Vous vous appelez " + nom + ". Vous avez " + str(age) + " ans, l'année prochaine vous aurez " + str(age + 1) + " ans." )

    # Conditions qui affichent un message en fonction de l'âge de la personne
    if age == 17:
        print("Vous êtes encore mineur...")
    elif 12 <= age < 18: # Si l'âge est entre 12 et 18 ans, c'est un adolescent
        print("Vous êtes un ado")
    elif age == 1 or age == 2: # Si l'âge est 1 ou 2, c'est un bébé
        print("Vous êtes un tout petit bébé")
    elif age == 18:
        print("Vous êtes tout juste majeur")
    elif age > 68: # Si l'âge est plus grand que 68, la personne est sénior
        print("Vous êtes sénior")
    elif age < 10:
        print("Vous êtes un enfant")
    elif age > 18:
        print("Vous êtes majeur")
    else: # Si l'âge est inférieur à 18 (mais pas dans les autres catégories), la personne est mineure
        print("Vous êtes mineur")

# Fonction qui demande le nom de l'utilisateur
def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quel est ton nom ? ")
    return nom # Retourne le nom saisi

# Fonction qui demande l'âge de la personne et vérifie si c'est un nombre
def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age = input(nom_personne + " Quel est ton âge jeune ? ")
        try:
            age_int = int(age)
        except:
            print("ERREUR: Rentre un nombre !")
    return age_int # Retourne l'âge valide
    
# Demander le nom de la première personne
nom1 = demander_nom()
# Demander le nom de la deuxième personne
nom2 = demander_nom()

# Demander l'âge de la première personne
age1 = demander_age(nom1)
# Demander l'âge de la deuxième personne
age2 = demander_age(nom2)

# Afficher les informations de la première personne
afficher_info_personne(nom1, age1)
print()  # Ligne vide pour séparer les deux affichages

# Afficher les informations de la deuxième personne
afficher_info_personne(nom2, age2)

##############################################
# Exercice : Catégoriser les âges

# Écris un programme en Python qui :
# - Demande à l'utilisateur son prénom et son âge
# - En fonction de l'âge, affiche un message différent, en utilisant les catégories suivantes :
    # Moins de 13 ans : "Tu es un enfant !"
    # De 13 à 17 ans : "Tu es un adolescent !"
    # De 18 à 65 ans : "Tu es un adulte !"
    # Plus de 65 ans : "Tu es un senior !"
# - Utilise des fonctions pour organiser ton code (2 ou 3).

##############################################