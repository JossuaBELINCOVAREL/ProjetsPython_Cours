# Variable de classe se rapporte directement à toute la classe et non à chaque objet (chaque self, même si au final elle le possède quand même)
# Ci-dessous, toutes les Personne sont des Humains, peu importe leur age/noms etc.

class Personne:
    ESPECE = "Humain" # Variable de classe, 1 variable pour toutes les Personne

    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom 
        self.age = age
        if self.nom == "":
            self.DemandeNom()
        print(f"Constructeur personne : {self.nom}")
        print()

    def SePresenter(self):       
        if self.age == 0:
            print(f"Bonjours je m'apelle {self.nom}")
            return
        
        print(f"Bonjours je m'apelle {self.nom}, j'ai {self.age} ans")
        if self.EstMajeur():
            print("Je suis Majeur")
        else:
            print("Je suis Mineur")

    def EstMajeur(self):
        if self.age >= 18:
            return True
        return False
    
    def DemandeNom(self):
        self.nom = input("Quel est ton nom ? ")

    def AfficherEspece():
        print(f"Info être vivants : {Personne.ESPECE}")

liste_personne = [Personne("Eva", 30), Personne("Paul", 15), Personne("Maurie", 28)]

for p in liste_personne:
    p.SePresenter()
    Personne.AfficherEspece()
    print()


# Personne
#       -> Personne.espece_etre_vivant
#    personne1
#       -> self.espece_etre_vivant (copie de la variable de classe pour en faire une variable d'instance)
#    personne2
#       -> self.espece_etre_vivant
#    personne3
#       -> self.espece_etre_vivant