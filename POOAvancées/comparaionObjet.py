# Comparer --> is / ==
# Ne compare pas les données mais les Objets

class Personne:
    def __init__(self, nom = str, age = int):
        self.nom = nom 
        self.age = age 

    def AfficherInfo(self):
        print(f"Je m'apelle {self.nom}, j'ai {self.age} ans")

    def __eq__(self, other):
        return self.nom == other.nom and self.age == other.age

personne1 = Personne("Eva", 35)
personne1.AfficherInfo()

personne2 = Personne("Jean", 24)
personne2.AfficherInfo()

personne3 = Personne("Eva", 35)

# Compare les objets sans def __eq__ (ça compare les données donc l'égalité)

print(personne1 == personne2)
print(personne1 is personne2)
print()

# Avec __eq__ ça retourne TRue sur la premièere, le is compare toujours les objets
print(personne1 == personne3)
print(personne1 is personne3)

