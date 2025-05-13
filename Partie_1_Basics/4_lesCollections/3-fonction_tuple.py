# Fonction qui retourne plusieurs informations sous forme de tuple
def obtenir_info():
    # On retourne 3 valeurs : nom (str), âge (int), taille (float)
    return "Julie", 25, 1.60

# On récupère le tuple retourné par la fonction dans une variable
infos = obtenir_info()
print(infos)  # Affiche le tuple complet : ('Julie', 25, 1.6)
print()

# On peut accéder à chaque valeur du tuple grâce à son indice
print("nom : " + infos[0])
print("age : " + str(infos[1]))
print("taille : " + str(infos[2]))
print()

# Décomposition directe du tuple en 3 variables (nom, age, taille)
nom, age, taille = obtenir_info()
print(f"Informations : Son nom est {nom}, son age est de {age} ans et elle mesure {taille}")
print()

# Fonction qui prend en paramètre un nom, un âge et une taille
def afficher_informations(nom, age, taille):
    print(f"Informations : Son nom est {nom}, son age est de {age} ans et elle mesure {taille}")

# On réutilise la fonction qui retourne le tuple, et on le décompose pour passer les valeurs à la fonction
nom, age, taille = obtenir_info()
afficher_informations(nom, age, taille)

# Même appel, mais plus rapide : on utilise l'opérateur * pour "décompresser" le tuple
# Cela revient à écrire : afficher_informations(infos[0], infos[1], infos[2])
afficher_informations(*infos)

# Affiche le tuple normalement
print(infos)

# Affiche les éléments du tuple séparément (sans parenthèses)
print(*infos)

##############################################
# Exercice : Système d'information d'étudiant

# Écrivez une fonction `obtenir_etudiant()` qui retourne :
# - Le prénom d’un étudiant (ex: "Lucas")
# - Sa moyenne générale (ex: 14.2)
# - S’il est admis ou non (True ou False)

# - Affichez les valeurs retournées une à une (en utilisant l’index du tuple)
# - Utilisez une affectation multiple pour stocker les 3 valeurs dans des variables distinctes
# - Écrivez une fonction qui affiche : "Lucas a une moyenne de 14.2. Admis : True"
# - Appelez la fonction en utilisant l’opérateur * avec le tuple retourné par `obtenir_etudiant()`

##############################################
