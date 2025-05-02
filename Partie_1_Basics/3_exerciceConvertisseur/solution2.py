# Constantes de conversion
POUCE_EN_CM = 2.54
CM_EN_POUCE = 0.394

def demander_mode_conversion() -> str:
    """
    Demande à l'utilisateur le sens de la conversion souhaitée.
    Retourne une chaîne : 'pouce_vers_cm' ou 'cm_vers_pouce'
    """
    while True:
        print("Quel type de conversion veux-tu faire ?")
        print("1 - Pouces vers centimètres")
        print("2 - Centimètres vers pouces")
        choix = input("Tape 1 ou 2 : ")

        if choix == "1":
            return "pouce_vers_cm"
        elif choix == "2":
            return "cm_vers_pouce"
        else:
            print("Erreur : tu dois entrer 1 ou 2.")

def demander_valeur() -> float:
    """
    Demande à l'utilisateur de rentrer une valeur numérique (float).
    """
    while True:
        valeur = input("Entre la valeur à convertir : ")
        try:
            return float(valeur)
        except ValueError:
            print("Erreur : tu dois entrer un nombre valide (utilise un point pour les décimales).")

def convertir(valeur: float, mode: str) -> float:
    """
    Effectue la conversion selon le mode donné.
    """
    if mode == "pouce_vers_cm":
        return valeur * POUCE_EN_CM
    elif mode == "cm_vers_pouce":
        return valeur * CM_EN_POUCE

def afficher_resultat(valeur: float, resultat: float, mode: str) -> None:
    """
    Affiche le résultat de la conversion.
    """
    if mode == "pouce_vers_cm":
        print(f"{valeur} pouces = {resultat} cm")
    else:
        print(f"{valeur} cm = {resultat} pouces")

# Programme principal
def main():
    mode = demander_mode_conversion()
    
    while True:
        valeur = demander_valeur()
        resultat = convertir(valeur, mode)
        afficher_resultat(valeur, resultat, mode)

        continuer = input("Souhaites-tu convertir une autre valeur ? (o/n) : ").lower()
        if continuer != "o":
            print("Merci d'avoir utilisé le convertisseur !")
            break

main()
