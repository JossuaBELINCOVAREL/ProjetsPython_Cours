# La boucle While (tant que)

# Premier programme : Compter de 0 à 9

n = 0 # On initialise une variable n à 0

while n < 10: # Tant que n est inférieur à 10, on exécute ce bloc
    print("Valeur de n: " + str(n)) # On affiche la valeur de n en le transformant en texte
    n = n + 1 # On ajoute 1 à n à chaque tour de boucle

print("Fin de la boucle") # Ce message s'affiche une fois la boucle terminée
print()

# Second programme : Demander un mot de passe jusqu'à ce qu'il soit correct

mot_de_passe = "" # On initialise une variable vide

while not mot_de_passe == "admin": # Tant que le mot de passe n'est pas "admin"
    mot_de_passe = input("Entre le mot de passe : ")

print("Bienvenue sur ton compte") # Affiché quand le bon mot de passe est saisi
print()

# Troisième programme : Demander un âge valide (nombre) et afficher l'âge + 1

age_prochain = 0

while age_prochain == 0:
    age = input("Quel est ton âge jeune ? ")
    try:
        age_prochain = int(age) + 1 # On essaye de convertir et ajouter 1
    except:
        print("ERREUR: Rentre un nombre !") # Si ça ne marche pas, message d'erreur et on recommence la boucle 
print("Vous avez actuellemennt " + age + " ans, l'année prochaine vous aurez " + str(age_prochain) + " ans.")
print()

# Quatrième programme : Demander un nom et un âge valides

nom = ""
while nom == "": # Tant que nom est vide, on redemande
    nom = input("Quel est ton nom ? ")

age_bientot = 0
while age_bientot == 0:
    age_la = input("Quel est ton âge jeune ? ")
    try:
        age_bientot = int(age_la) + 1 # Essaye de convertir et ajouter 1
    except:
        print("ERREUR: Rentre un nombre !")
        
print("Vous vous appelez " + nom+ ".")
print("Vous avez actuellemennt " + age_la + " ans, l'année prochaine vous aurez " + str(age_bientot) + " ans.")

##############################################
# Exercice : Système de connexion sécurisé

# Écris un programme en Python qui :
# - Demande à l’utilisateur de saisir un identifiant (ex : "admin")
# - Puis demande un mot de passe (ex : "1234")
# - Tant que l’un des deux est incorrect, il redemande les deux.
# - Une fois que les deux sont corrects, affiche : "Connexion réussie, bienvenue 'identifiant' !"

##############################################