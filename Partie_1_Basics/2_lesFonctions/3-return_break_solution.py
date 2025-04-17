# Fonction qui vérifie si l’âge d’un animal est élevé
def est_age_avancé(age):
    if age >= 10:
        return True
    return False

# Fonction qui affiche les informations de l’animal
def afficher_info_animal(nom="", age=0):
    if nom == "":
        print(f"Aucun nom d'animal fourni. Âge : {age}")
        if est_age_avancé(age):
            print("C'est un animal âgé.")
        else:
            print("C'est un animal jeune.")
        return

    print(f"Nom de l'animal : {nom}")
    print(f"Âge : {age} ans")

    if est_age_avancé(age):
        print("C'est un animal âgé.")
    else:
        print("C'est un animal jeune.")

# Appels de la fonction avec différents animaux
afficher_info_animal("Rex", 12)
print()
afficher_info_animal("Milo", 4)
print()
afficher_info_animal(age=8)
