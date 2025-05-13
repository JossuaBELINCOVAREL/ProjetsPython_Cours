# Un dictionnaire est une **collection de données** sous forme de paires "clé : valeur"
# Exemple : une fiche d'identité d'une personne

# Création d'un dictionnaire avec les informations de base
personne = {'nom' : 'Julie', 'age' : 25, 'taille' : 1.60}
print(personne)  # Affiche tout le dictionnaire

# Accès à une valeur grâce à sa clé
print(personne['nom'])    # Affiche "Julie"
print(personne['age'])    # Affiche 25
print()

# Modification d'une valeur existante (la clé doit déjà exister)
personne['nom'] = "Claire"
print(personne)  # Le nom est maintenant "Claire"

# Ajout d'une nouvelle paire clé/valeur dans le dictionnaire
personne['poste'] = "développeur"
print(personne)
print()

# On peut aussi ajouter des types complexes comme des tuples ou des listes
achat = ("Chocolat", "beurre", "fromage")  # Tuple contenant des articles
personne['achats'] = achat  # Ajout du tuple dans le dictionnaire
print(personne)
print()

# On peut parcourir un dictionnaire avec une boucle
for i in personne:
    print(i)              # Affiche chaque **clé**
    print(personne[i])    # Affiche la **valeur associée à chaque clé**

##############################################
# Exercice : Gérer un carnet de notes avec un dictionnaire

# Crée un dictionnaire `eleve` contenant :
# - prénom : "Lucas"
# - age : 16
# - classe : "1ère"
# - notes : une liste contenant 4 notes de ton choix (par exemple [14, 12, 17, 15])

# - Affiche toutes les informations de l'élève
# - Modifie le prénom de l’élève par "Lucie"
# - Ajoute une nouvelle note à la liste de notes (exemple : 18)
# - Affiche la moyenne des notes de l’élève (addition des notes / nombre de notes)

##############################################
