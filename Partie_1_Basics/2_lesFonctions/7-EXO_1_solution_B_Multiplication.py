# Correction interactive de l'exercice : Table de multiplication personnalisée

# Fonction qui affiche une table de multiplication entre deux bornes
def afficher_table_multiplication(n, min, max):
    if min > max:
        print("ERREUR : Le minimum est plus grand que le maximum.")
        return
    for i in range(min, max + 1):  # On inclut le max
        print(f"{i} x {n} = {i * n}")

# Programme principal
print("Bienvenue dans le générateur de table de multiplication !")
print("")

# Demande à l'utilisateur la table souhaitée
while True:
    try:
        nombre = int(input("Quelle table veux-tu afficher ? (ex : 5 pour la table de 5) : "))
        break
    except ValueError:
        print("Erreur : tu dois entrer un nombre entier.")

# Demande à l'utilisateur les bornes min et max
while True:
    try:
        min_val = int(input("Quel est le multiplicateur minimum ? : "))
        max_val = int(input("Quel est le multiplicateur maximum ? : "))
        break
    except ValueError:
        print("Erreur : entre des nombres entiers.")

# Appel de la fonction avec les valeurs saisies
print("")
afficher_table_multiplication(nombre, min_val, max_val)
