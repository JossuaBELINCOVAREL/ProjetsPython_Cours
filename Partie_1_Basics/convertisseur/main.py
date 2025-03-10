# 1 pouce = 2.54 cm
# 1 cm = 0.394 pouces

def demande_unite():
    while True:
        choix_conversion = input("Tu souhaites convertir de pouces vers cm (Tape 1) ou de cm vers pouces (Tape 2) ? ")

        try:
            choix_conversion = int(choix_conversion)
            if choix_conversion == 1:
                return "centimètres (cm)"
            elif choix_conversion == 2:
                return "pouces (inch)"
            else:
                print("Rentre un nombre valide, entre 1 et 2 !")
        except ValueError:
            print("Rentrez un nombre valide")

def calcul(valeur, choix_conversion):
    valeur_pc = 2.54
    valeur_cp = 0.394

    if choix_conversion == "centimètres (cm)":
        return float(valeur) * valeur_pc
    else:
        return float(valeur) * valeur_cp

# 1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"

choix_conversion = demande_unite()

# 2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)

while True:
    valeur = input(f"Rentre la valeur que tu souhaites convertir vers le {choix_conversion} : ")

    try:
        valeur = float(valeur)
        break
    except:
        print("Rentrez un nombre valide")

# 3 - Afficher la valeur convertie (et l'unité : cm ou pouces)

resultat = calcul(valeur, choix_conversion)

if choix_conversion == "centimètres (cm)":
    unite_depart = "pouces"
else:
    unite_depart = "cm"

print(f"{valeur} {unite_depart} est égal à {resultat} {choix_conversion}")


