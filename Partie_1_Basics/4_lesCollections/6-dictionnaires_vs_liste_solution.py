# Avec une liste, plus long pour le CPU car souvent il faut boucler pleins de fois pour trouver les infos associés
# Avec un dictionnaire, on peut rechercher directement à la valeur souhaité les infos
# Ici on veut retrouver les infos de Eva

# Avec une liste

def obtenir_informations(nom, liste):
    for i in liste:
        if i[0] == nom:
            return i
    return None

personnes = [("Mélanie", 25, 1.6), ("Eva", 20, 1.67), ("Tom", 45, 1.54), ("Léo", 19, 1.7)]

infos = obtenir_informations("Eva", personnes)
print(infos)
print

# Avec un dictionnaire

personnes_dictionnaire = {"Mélanie" : (25, 1.6), "Eva" : (20, 1.67), "Tom" : (45, 1.54), "Léo" : (19, 1.7)}

infos_dictionnaire = personnes_dictionnaire.get("Eva")
if infos_dictionnaire == None:
    print("La clef n'existe pas")
else:
    print(infos_dictionnaire)