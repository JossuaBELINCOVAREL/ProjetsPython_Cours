# Les return

def est_majeur(age):
    if age >= 18:
        return True
    return False

def afficher_info_personne(nom="", age=0):
    if nom == "":
        print(f"Vous n'avez pas passez de nom. Mais son age vaut {age}")
        if est_majeur(age):
            print("Il est donc majeur")
        else:
            print("Il est donc mineur")
        return
    
    if age == 0:
        print(f"La personn est {nom}, son age n'est pas connu")
    else:
        print(f"La personn est {nom}, son age est de {age} ans")
    print(f"Le nom comporte {len(nom)} caractères")

    if est_majeur(age):
        print("Il est majeur")
    else:
        print("Il est mineur")

print("Début du programme")
print("")

afficher_info_personne("toto", 20)
afficher_info_personne("Joseph")
afficher_info_personne(age = 46)

print("")
print("Fin du programme")