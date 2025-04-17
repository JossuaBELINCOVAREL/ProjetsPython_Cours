# Déclaration d'une fonction qui multiplie deux nombres
def mult_callback(a, b):
    return a * b  # Retourne le résultat de a multiplié par b

# Déclaration d'une fonction qui additionne deux nombres
def add_callback(a, b):
    return a + b  # Retourne le résultat de a + b

# Déclaration d'une fonction qui élève a à la puissance b
def power_callback(a, b):
    return pow(a, b)  # pow(a, b) = a^b (a puissance b)

# Fonction principale qui affiche le résultat d’une opération entre n et les chiffres de 1 à 9
# Elle prend :
# - n : un nombre fixé
# - operateur_str : un symbole pour afficher l’opération (exemple : +, x, ^)
# - operation_callback : une fonction qu'on passe en paramètre (callback), à appliquer à chaque ligne
def afficher_calcul(n, operateur_str, operation_callback):
    for i in range(1, 10):  # Boucle de 1 à 9
        # À chaque tour, on applique la fonction "operation_callback" à i et n
        print(f"{i} {operateur_str} {n} = {operation_callback(i, n)}")

# Appel de la fonction afficher_calcul avec :
# - 2 comme nombre
# - "x" comme symbole
# - la fonction mult_callback pour faire les multiplications
afficher_calcul(2, "x", mult_callback)
print()

# Même chose, mais avec l’addition
afficher_calcul(2, "+", add_callback)
print()

# Même chose, mais avec la puissance
afficher_calcul(2, "^", power_callback)
print()


##############################################
# Exercice : Crée ton propre tableau de calcul avec soustraction et division

# Crée deux nouvelles fonctions :
# - soustraction_callback(a, b) → retourne a - b
# - division_callback(a, b) → retourne a / b

# Ensuite, appelle la fonction afficher_calcul() deux fois :
# - Une fois pour afficher les soustractions avec le nombre 10
# - Une autre fois pour afficher les divisions avec le nombre 2

# Indice : Attention à ne pas diviser par 0. La boucle commence à 1, donc c’est bon !

##############################################