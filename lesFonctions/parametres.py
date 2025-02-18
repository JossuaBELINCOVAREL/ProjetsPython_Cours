# Les paramètres d'une fonction
# Return ici permet de sortir de la fonction si le nom = ""
# Permet de valider ou non les pré-fonctions (cas spécifiques d'une fonction, erreur, etc.)

def afficher_info_personne(nom="", age=0):
    if nom == "":
        print(f"Vous n'avez pas passez de nom. Mais son age vaut {age}")
        return
    
    if age == 0:
        print(f"La personn est {nom}, son age n'est pas connu")
    else:
        print(f"La personn est {nom}, son age est de {age} ans")
    print(f"Le nom comporte {len(nom)} caractères")

print("Début du programme")

afficher_info_personne("toto", 20)
afficher_info_personne("Joseph")
afficher_info_personne(age = 22)

print("Fin du programme")