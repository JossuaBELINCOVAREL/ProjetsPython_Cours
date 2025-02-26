'''
Demander le nom
Tester la majorité
Si pas d'age, écrire juste le nom
'''

class Personne:
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

personne1 = Personne("Eva", 30) 
personne2 = Personne("Paul", 15)

personne3 = Personne()

personne4 = Personne(age = 87)

personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()
personne4.SePresenter()

