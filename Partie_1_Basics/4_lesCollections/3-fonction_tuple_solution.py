# Étape 1 : La fonction retourne un tuple avec 3 infos
def obtenir_etudiant():
    return "Lucas", 14.2, True

# Étape 2 : On stocke le tuple et on affiche chaque élément avec son index
etudiant = obtenir_etudiant()
print("Prénom :", etudiant[0])
print("Moyenne :", etudiant[1])
print("Admis :", etudiant[2])
print()

# Étape 3 : Affectation multiple (décomposition du tuple)
prenom, moyenne, admission = obtenir_etudiant()

# Étape 4 : Fonction pour afficher les infos
def afficher_etudiant(prenom, moyenne, admission):
    print(f"{prenom} a une moyenne de {moyenne}. Admis : {admission}")

# Étape 5 : Appel de la fonction avec l’opérateur *
afficher_etudiant(*etudiant)
