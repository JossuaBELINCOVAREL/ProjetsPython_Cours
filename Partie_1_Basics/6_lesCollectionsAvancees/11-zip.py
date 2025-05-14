# Utilisation de `zip` pour combiner des listes

# On a deux tuples avec des informations sur des pizzas : le nom et le prix
pizza_nom = ("4 Fromages", "Végétarienne", "Hawai", "Calzone")
pizza_prix = (10.50, 11, 7, 12)

# La fonction zip permet de regrouper les éléments de plusieurs listes en tuples
# Ici, on crée une nouvelle liste où chaque élément est un tuple contenant (nom, prix)
noms_prix = list(zip(pizza_nom, pizza_prix))

# On affiche la liste des tuples (nom de la pizza, prix)
print(noms_prix)
print()  # On ajoute une ligne vide pour plus de lisibilité

# Alternative : On peut aussi utiliser `zip` directement dans une boucle
for (nom, prix) in zip(pizza_nom, pizza_prix):
    print(f"{nom} - {prix}$")
# Cela affiche chaque pizza avec son prix, en les récupérant directement depuis les deux listes

print()  # Une autre ligne vide pour séparer les résultats

# Pour faire l'inverse : si on a une liste de tuples (nom, prix), on peut décompresser cette liste
# Cela permet de recréer les listes de noms et de prix séparément
nom, prix = list(zip(*noms_prix))

# On affiche les deux nouvelles listes obtenues après avoir "dézipé" les tuples
print(nom, prix)

##############################################
# Exercice : Listes de films et de notes

# Tu as deux listes :
#   - Les titres des films : ["Inception", "Avatar", "Titanic", "The Dark Knight"]
#   - Les notes des films : [8.8, 7.8, 7.5, 9.0]

# Crée une liste de tuples avec `zip`, où chaque tuple contient un titre de film et sa note.
# Affiche chaque film avec sa note sous la forme "Titre - Note/10".
# Utilise `zip(*noms_prix)` pour "dézipper" les films et les notes en deux listes séparées, puis affiche-les.

# Indice : Pour afficher chaque film, utilise une boucle `for` avec `zip`.

##############################################