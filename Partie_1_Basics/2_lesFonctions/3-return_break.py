# La différence entre break et return :
# - break : interrompt une boucle (comme un while ou un for) mais continue le reste du programme
# - return : quitte complètement une fonction. Tout ce qui est en dessous n’est plus exécuté

# Cette fonction vérifie si une personne est majeure ou non
# Elle prend l'âge en paramètre et retourne True (vrai) si l'âge est supérieur ou égal à 18
# Sinon, elle retourne False (faux)

def est_majeur(age):
    if age >= 18:
        return True  # Quitte la fonction et retourne True
    return False     # Sinon, retourne False

# Cette fonction affiche les informations d'une personne : son nom, son âge, et s’il est majeur ou mineur
def afficher_info_personne(nom="", age=0):
    
    # Si aucun nom n’est fourni
    if nom == "":
        print(f"Vous n'avez pas passé de nom. Mais son âge vaut {age}")
        
        # On vérifie si la personne est majeure ou mineure
        if est_majeur(age):
            print("Il est donc majeur")
        else:
            print("Il est donc mineur")

        return  # On sort de la fonction ici car il manque le nom, pas besoin d’aller plus loin

    # Si le nom est donné mais l’âge est inconnu
    if age == 0:
        print(f"La personne est {nom}, son âge n'est pas connu")
    else:
        # Si nom et âge sont disponibles
        print(f"La personne est {nom}, son âge est de {age} ans")

    # On affiche le nombre de lettres dans le nom
    print(f"Le nom comporte {len(nom)} caractères")

    # Encore une fois, on vérifie si la personne est majeure ou mineure
    if est_majeur(age):
        print("Il est majeur")
    else:
        print("Il est mineur")


# Début du programme principal
print("Début du programme")
print("")

# Appels de la fonction avec différentes situations
afficher_info_personne("toto", 20)   # Cas complet
afficher_info_personne("Joseph")     # Cas sans âge
afficher_info_personne(age = 46)     # Cas sans nom

print("")

##############################################
# Exercice : Déterminer si un animal est âgé

# Crée une fonction est_age_avancé(age) qui :
# - retourne True si l'âge est supérieur ou égal à 10, sinon False

# Ensuite, crée une fonction afficher_info_animal(nom, age) qui :
# - affiche "Nom de l'animal : [nom]"
# - indique si l’animal est âgé ou jeune (en utilisant est_age_avancé(age))

# Teste avec les animaux suivants :
# - "Rex", 12
# - "Milo", 4
# - "", 8 (cas sans nom)

##############################################