# 

class EtreVivant:
    ESPECE = "(non identifié)"

    def AfficherEspece(self):
        print(f"Info être vivants : {self.ESPECE}")

class Chat(EtreVivant): # Ma classe chat hérite de la class EtreVivant
    ESPECE = "Félin"

class Personne(EtreVivant):
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

class Etudiant(Personne):
    def __init__(self, nom: str = "", age: int = 0, etudes: str = ""):
        # self.nom = nom 
        # self.age = age
        super().__init__(nom, age)
        self.etudes = etudes

    def SePresenter(self): # Surchargé la méthode SePresenter()
            super().SePresenter() # Ici on appelle avec super() la méthode SePresenter parente
            print(f"Je suis étudiant en {self.etudes}")


liste_personne = [Personne("Eva", 30), Personne("Paul", 15), Personne("Maurie", 28)]

for p in liste_personne:
    p.SePresenter()
    p.AfficherEspece()
    print()

chat = Chat()
chat.AfficherEspece()

etudiant = Etudiant("Marc", 22, "Ingénieur")
etudiant.SePresenter()
etudiant.AfficherEspece()

# Personne
#       -> Personne.espece_etre_vivant
#    personne1
#       -> self.espece_etre_vivant (copie de la variable de classe pour en faire une variable d'instance)
#    personne2
#       -> self.espece_etre_vivant
#    personne3
#       -> self.espece_etre_vivant