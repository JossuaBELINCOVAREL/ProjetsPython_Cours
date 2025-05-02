# --- Fonction récursive simple ---

# Cette fonction affiche les valeurs successives de n jusqu'à ce qu'il dépasse une limite.
def a(n, limit):
    # Cas d'arrêt : si n dépasse la limite, on arrête la récursion
    if n > limit:
        return
    # Affiche la valeur actuelle de n
    print("n: ", n)
    # Appelle récursivement la fonction avec n * n
    a(n*n, limit)

# Appel initial de la fonction récursive
a(2, 100000) # Affichera : 2, 4, 16, 256, 65536

print() # Saut de ligne pour rendre le terminal plus lisible

# --- Fonction récursive de validation de l'utilisateur ---

# Cette fonction demande à l'utilisateur de faire un choix entre une valeur minimale et maximale.
# Si l'entrée est invalide (texte, hors intervalle...), la fonction se rappelle elle-même.

def demander_choix_utilisateur(min, max):
    reponse_str = input(f"Quel est votre choix entre {str(min)} et {str(max)} : ")
    try:
        reponse_int = int(reponse_str) # Tente de convertir la réponse en entier
        if not min <= reponse_int <= max: # Vérifie si l'entier est dans l'intervalle autorisé
            print(f"ERREUR, rentre un entre nombre entre {min} et {max}")
            # Rappel récursif si erreur
            return demander_choix_utilisateur(min, max)
        return reponse_int # Si tout est bon, on retourne la valeur
    except:
        # Si la conversion en entier échoue, on relance la demande
        print("ERREUR : Vous devez rentrer un nombre ! ")
        return demander_choix_utilisateur(min, max)

# Appel de la fonction de choix
choix = demander_choix_utilisateur(1, 5)
print(f"Choix de l'utilisateur : {choix}") # Affiche le choix de l'utilisateur

##############################################
# Exercice : Crée un programme qui affiche la somme de tous les nombres pairs jusqu'à une limite.

# Écris une fonction récursive somme_pairs(n) qui :
# - Prend un nombre entier n en paramètre
# - Retourne la somme de tous les nombres pairs de 0 jusqu’à n inclus

# Ensuite, demande à l’utilisateur une limite avec validation
# Affiche la somme

##############################################
    