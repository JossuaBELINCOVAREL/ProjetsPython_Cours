# Cette fonction affiche des informations sur une personne : son nom et son âge
# Elle accepte 2 paramètres : nom (chaîne de caractères), age (nombre entier)
# On leur donne une valeur par défaut : nom = "" et age = 0

def afficher_info_personne(nom="", age=0):

    # Si aucun nom n’a été fourni, on affiche un message spécial
    if nom == "":
        print(f"Vous n'avez pas passé de nom. Mais son âge vaut {age}")
        return  # On quitte la fonction immédiatement (rien d'autre ne s’exécutera)

    # Si le nom est présent mais pas l'âge
    if age == 0:
        print(f"La personne est {nom}, son âge n'est pas connu")
    else:
        # Si nom et âge sont connus
        print(f"La personne est {nom}, son âge est de {age} ans")

    # Affiche combien de lettres il y a dans le nom
    print(f"Le nom comporte {len(nom)} caractères")


# Début du programme principal
print("Début du programme")

# Appels de la fonction avec différentes situations

# Cas 1 : nom et âge sont donnés
afficher_info_personne("toto", 20)

# Cas 2 : seul le nom est donné
afficher_info_personne("Joseph")

# Cas 3 : seul l’âge est donné
afficher_info_personne(age=22)

# Fin du programme principal
print("Fin du programme")

##############################################
# Exercice : Prénom obligatoire et message d’accueil

# Écris une fonction appelée saluer_utilisateur() qui :
# - prend en paramètre un prénom (prenom)
# - affiche "Bonjour [prenom] !", uniquement si le prénom est fourni
# - sinon, elle affiche : "Erreur : prénom manquant" et quitte la fonction avec return

# Appelle cette fonction 3 fois :
# - Une fois avec "Alice"
# - Une fois avec ""
# - Une fois avec "Lucas"

##############################################