# shallow copy / deep copy

import copy

class Personne:
    def __init__(self, nom, age, amis):
        self.nom = nom 
        self.age = age
        self.amis = amis

    def AfficherInfo(self):
        print(f"Je m'apelle {self.nom}, j'ai {self.age} ans")
        print(f"J'ai en amis : {self.amis}")

    def __eq__(self, other):
        return self.nom == other.nom and self.age == other.age

personne1 = Personne("Eva", 35, ["Abduel", "Fred", "Marie"])
personne1.AfficherInfo()

# personne2 = copy.copy(personne1) # shallow copy
personne2 = copy.deepcopy(personne1) # deep copy
# personne1.nom = "Bob"
personne1.amis[0] = "Chantal"
personne2.AfficherInfo()

# personne2 = personne1 -> Ne fait pas une copie d'objet !!


print(personne1 == personne2)
print(personne1 is personne2)
print()


# Si impossible d'avoir accès à la class : 
print(personne1.__dict__ == personne2.__dict__)