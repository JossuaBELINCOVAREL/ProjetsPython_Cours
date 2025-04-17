# Ce programme permet de demander à deux personnes leur nom et leur âge,
# puis d'afficher un message personnalisé pour chacune d'elles.



# Définition d'une fonction (utilisation du mot clé "def") : afficher les infos d'une personne 
def afficher_info_personne(nom, age):
    print("Vous vous appelez " + nom + ". Vous avez " + str(age) + " ans, l'année prochaine vous aurez " + str(age + 1) + " ans." )

# Quand tu définis une fonction avec def, ce que tu mets entre les parenthèses (ici nom, age) sont appelés paramètres.
# Quand tu appelles la fonction plus tard avec des valeurs concrètes, ces paramètres reçoivent ces valeurs qu'on appelle alors des arguments.

# Définition d'une fonction : demander le nom à l'utilisateur
def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quel est ton nom ? ")
    return nom # On retourne (renvoie) le nom saisi

# Avec return : la fonction produit une valeur qu'on peut réutiliser.
# Sans return : la fonction fait une action (ex : afficher), mais ne garde rien.

def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age = input(nom_personne + " Quel est ton âge jeune ? ")
        try:
            age_int = int(age)
        except:
            print("ERREUR: Rentre un nombre !")
    return age_int # On retourne l'âge validé

# --- Programme principal ---

# Les fonctions sont appelées avec le nom de la fonction suivi de parenthèses.
# Si la fonction prend des paramètres, tu les mets dans ces parenthèses.

    
# On demande le nom de la première personne
nom1 = demander_nom()
# On demande le nom de la deuxième personne
nom2 = demander_nom()

# On demande l'âge de la première personne
age1 = demander_age(nom1)
# On demande l'âge de la deuxième personne
age2 = demander_age(nom2)

# On affiche les informations des deux personnes
afficher_info_personne(nom1, age1)
afficher_info_personne(nom2, age2)

##############################################
# Exercice : Crée ton mini assistant personnel

# Crée un programme composé de 3 fonctions :
# - Une fonction demander_nom() qui demande le prénom d’une personne (ne rien laisser vide).
# - Une fonction demander_age() qui demande l'âge d'une personne, en s'assurant que ce soit bien un nombre.
# - Une fonction afficher_message() qui affiche : "Bonjour Prénom, dans 5 ans tu auras X ans !"
# - Le programme principal devra demander les infos pour une seule personne puis afficher le message personnalisé.

##############################################