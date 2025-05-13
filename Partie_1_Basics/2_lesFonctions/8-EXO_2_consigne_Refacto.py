""" 
def recuperer_afficher_info(numero_personne):
    print(f"--- Personne n°{numero_personne} ---")
    nom = input(f"Quel est le nom de la personne {numero_personne} ? ")
    prenom = input(f"Quel est le prénom de la personne {numero_personne} ? ")
    age = input(f"Quel est l'âge de {prenom} ? ")
    ville = input(f"Où habite {prenom} ? ")

    print(f"{prenom} {nom}, âgé de {age} ans, habite à {ville}.")
    print(f"Le prénom contient {len(prenom)} lettres, le nom {len(nom)} lettres, soit {len(prenom) + len(nom)} lettres au total.")
    print("")

print("Bienvenue dans le gestionnaire de fiches personnelles !")
print("")

recuperer_afficher_info(1)
recuperer_afficher_info(2)
recuperer_afficher_info(3)
recuperer_afficher_info(4)
recuperer_afficher_info(5)

"""

# EXERCICE : Refactorisation de code - Fiche personnelle

"""
Ce programme demande à l’utilisateur d’entrer des informations pour 5 personnes :
- leur nom
- leur prénom
- leur âge
- leur ville

Ensuite, le programme affiche les informations sous forme de phrase complète, 
et indique aussi combien de lettres composent leur prénom, leur nom, ainsi que le total.

EXEMPLE D’AFFICHAGE :

    --- Personne n°1 ---
    Quel est le nom de la personne 1 ? Dupont
    Quel est le prénom de la personne 1 ? Alice
    Quel est l'âge de Alice ? 29
    Où habite Alice ? Paris
    Alice Dupont, âgé de 29 ans, habite à Paris.
    Le prénom contient 5 lettres, le nom 6 lettres, soit 11 lettres au total.

OBJECTIF :

Refacto' le code pour qu’il soit plus clair, plus propre, et plus facile à modifier :
- Ajouter une boucle pour ne pas répéter 5 fois la même fonction
- Isoler la logique d'affichage et de calcul dans une autre fonction
- Penser à nommer les variables de manière claire

OPTION :
- Ajouter une vérification pour que l'âge soit bien un nombre entier
- Permettre à l'utilisateur de choisir le nombre de personnes à enregistrer

"""
