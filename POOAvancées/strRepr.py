# __str__ permet de reprensentation sous chaine de caractère
# __repr__ permet de representation sous forme d'objet dans le debugger pour le developpeur


class Personne:
    def __init__(self, nom, age):
        self.nom = nom 
        self.age = age

    def AfficherInfo(self):
        print(f"Je m'apelle {self.nom}, j'ai {self.age} ans")

    # def __str__(self):
    #     return "STR"
    
    def __repr__(self):
        return __class__.__name__ + " " + str(self.__dict__)

personne1 = Personne("Eva", 35)
personne1.AfficherInfo()

print(personne1)