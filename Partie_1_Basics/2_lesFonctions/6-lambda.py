# Fonction générique qui effectue un calcul entre un nombre n et une série de valeurs de 1 à 9
# Elle prend trois arguments :
#  - n : le nombre avec lequel on fait les opérations
#  - opertaur_str : le symbole à afficher pour l'opération (ex: "+", "x", etc.)
#  - operation_callback : la fonction qui définit le calcul à effectuer

# Une lambda est une petite fonction anonyme (c’est-à-dire sans nom) que l’on peut écrire rapidement, directement dans l’appel.

def afficher_calcul(n, opertaur_str, operation_callback):
    for i in range(1, 10): # Boucle de 1 à 9 (exclus 10)
        # Pour chaque i, on affiche l'opération et son résultat
        print(f"{i} {opertaur_str} {n} = {operation_callback(i, n)}")
    
# Utilisation de la fonction avec une fonction lambda pour la multiplication
afficher_calcul(2, "x", lambda a, b : a * b)
print()

# Utilisation de la fonction avec une fonction lambda pour l'addition
afficher_calcul(2, "+", lambda a, b : a + b)
print()

# Utilisation de la fonction avec une fonction lambda pour la puissance (exponentiation)
afficher_calcul(2, "^", lambda a, b : pow(a, b))
print()

##############################################
# Exercice : Crée un programme qui affiche le résultat d’un calcul 

# Écris une fonction afficher_operations_personnalisees(n, callback) qui :
# - Affiche le résultat d’un calcul entre n et les entiers de 1 à 5
# - Ajoute un texte explicite pour chaque ligne

# Utilise cette fonction avec deux lambdas différentes :
# - Une qui calcule la soustraction a - b
# - Une autre qui calcule la division a / b (en gérant les erreurs de division si nécessaire)

##############################################