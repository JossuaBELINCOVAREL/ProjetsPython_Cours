# IsInstance -> Permet de vérifier les types

class Personne:
    def __init__(self, nom = str, age = int):
        self.nom = nom 
        self.age = age 

        if not isinstance(age, int):
            print("L'âge doit être de type int") # Permet de vérifier si age = int
            self.age = 0

    def AfficherInfo(self):
        print(f"Je m'apelle {self.nom}")
        if self.age > 0:
            print(f"L'an prochain, j'aurai {self.age + 1} ans.")

# personne = Personne("Jean", 20)
personne2 = Personne("Bob", "40")

# personne.AfficherInfo()
personne2.AfficherInfo()