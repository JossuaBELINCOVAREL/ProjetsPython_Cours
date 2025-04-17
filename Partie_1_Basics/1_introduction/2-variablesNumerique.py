# Comprendre les variables numériques

# Premier programme : types de données et concaténation

nom = "admin" # Variable contenant une chaîne de caractères (string)
age = 20 # Variable contenant un entier (integer)
age_enfant = "30" # Variable contenant un chiffre mais sous forme de chaîne (string)

print(type(nom))
print(type(age))
print(type(age_enfant))

# Affichage d'une phrase avec transformation d'un nombre en texte grâce à str()
# Il est important de convertir les variables en texte pour pouvoir les concatener, sinon il y aura une erreur
print("Je m'appelle " + nom + " et j'ai actuellement " + str(age) + " ans. Mon fils lui à " + age_enfant + " ans.")

# Second programme : addition d'entiers et affichage

age_maintenant = 25
age_prochain = age_maintenant + 1 # On ajoute 1 à l'âge pour obtenir l'âge de l'année prochaine

# Affichage de l'âge actuel et futur avec transformation en chaîne de caractères
print("Vous avez actuellemennt " + str(age_maintenant) + " ans, l'année prochaine vous aurez " + str(age_prochain) + " ans.")

# Troisième programme : saisie utilisateur et gestion d'erreur

# Introduction de try/except :
    # Permet de tester une expression et de prendre des actions en cas d'erreur
    # Différent de if qui vérifie une condition, alors que try gère des exceptions (tenter une opération qui pourrait échouer)

age_la = input("Quel est ton âge jeune ? ") # On demande à l'utilisateur son âge et on le stocke (toujours en string)

try:
    age_pala = int(age_la) + 1 # On essaye de convertir la saisie en entier et d’ajouter 1
except:
    print("ERREUR: Rentre un nombre !") # Si la conversion échoue, on affiche une erreur
else:
    print("Vous avez actuellemennt " + str(age_la) + " ans, l'année dernière tu vous aurez " + str(age_pala) + " ans.")


##############################################
# Exercice : Mon âge, l'année dernière

# Écris un programme en Python qui :
# - Demande à l'utilisateur son âge actuel
# - Calcule son âge de l'année d'avant
# - Affiche une phrase comme : "Tu as 15 ans aujourd'hui, l'année dernière tu avais 14 ans !"
# - Si l'utilisateur ne rentre pas un nombre, affiche un message d'erreur clair.

##############################################