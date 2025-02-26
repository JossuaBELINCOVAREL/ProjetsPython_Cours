# POO EXERCICE DE MISE EN SITUATION 2

class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        print(f"Bonjour, je m'appelle {self.nom}, j'ai {self.age} ans")

        if self.EstMajeur():
            print("Je suis majeur")
        else:
            print("Je suis mineur")
        print()

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25)
personne1.SePresenter()
personne2 = Personne("Emilie", 17)
personne2.SePresenter()