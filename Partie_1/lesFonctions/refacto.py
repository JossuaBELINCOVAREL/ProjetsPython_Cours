""" Refacto de ce code pour qu'il soit maintenable

def recuperer_afficher_info(numero_personne):
    nom = input(f"Le nom de la personne {numero_personne} est : ")
    age = input(f"L'age de la personne {numero_personne} est :")
    print(f"La personne {numero_personne} est {nom}, elle à {age} ans.")
    print(f"Son nom comporte {len(nom)} caractères")

print("Bienvenu !")
print("")

recuperer_afficher_info(1)
recuperer_afficher_info(2)
recuperer_afficher_info(3)
recuperer_afficher_info(4)
recuperer_afficher_info(5)

"""

def recuperer_info(numero_personne):
    nom_personne = input(f"Le nom de la personne {numero_personne} est : ")
    age_personne = input(f"L'age de la personne {numero_personne} est :")
    return nom_personne, age_personne

def afficher_info(numero_personne, nom, age):
    print(f"La personne {numero_personne} est {nom}, elle à {age} ans.")
    print(f"Son nom comporte {len(nom)} caractères")

def recuperer_afficher_info(numero_personne):
    nom, age = recuperer_info(numero_personne)
    afficher_info(numero_personne, nom, age)


print("Bienvenu !")
print("")

nb_personne = 4
for i in range(nb_personne):
    recuperer_afficher_info(i+1)

afficher_info("007", "James", 40)