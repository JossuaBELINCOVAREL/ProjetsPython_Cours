import time
import beepy

# Durées des cuissons en secondes
MODES_CUISSON = {
    1: ("Tagliatelles", 3 * 60),
    2: ("Fusili", 6 * 60),
    3: ("Tortelini", 9 * 60)
}

def afficher_menu():
    """
    Affiche les options de cuisson disponibles.
    """
    print("Bienvenue sur le programme de cuisson préféré des devs 🍝")
    print("Voici les modes de cuisson disponibles :")
    for key, (nom, duree) in MODES_CUISSON.items():
        print(f"{key} - {nom} : {duree // 60} minutes")

def demander_choix() -> int:
    """
    Demande à l'utilisateur de choisir un mode de cuisson.
    Retourne l'entier correspondant au choix.
    """
    while True:
        choix = input("Choisis le mode de cuisson souhaité (1, 2 ou 3) : ")
        try:
            choix_int = int(choix)
            if choix_int in MODES_CUISSON:
                return choix_int
            print("Erreur : Choix invalide, tape 1, 2 ou 3.")
        except ValueError:
            print("Erreur : tu dois entrer un chiffre !")

def demarrer_cuisson(duree: int):
    """
    Lance le compte à rebours de cuisson avec affichage dynamique.
    """
    temps_restant = duree
    while temps_restant > 0:
        minutes = temps_restant // 60
        secondes = temps_restant % 60
        print(f"Temps restant : {minutes:02d}:{secondes:02d}", end="", flush=True)

        for _ in range(10):
            if temps_restant <= 0:
                break
            time.sleep(1)
            print(".", end="", flush=True)
            temps_restant -= 1
        print()

def cuisson_terminee():
    """
    Affiche un message de fin et joue un son.
    """
    print("\nCuisson terminée ! Bon appétit 🍽️")
    beepy.beep(sound="ping")

def main():
    afficher_menu()
    choix = demander_choix()
    nom_pate, duree = MODES_CUISSON[choix]
    print(f"\nLancement de la cuisson des {nom_pate} pendant {duree // 60} minutes...\n")
    demarrer_cuisson(duree)
    cuisson_terminee()

main()
