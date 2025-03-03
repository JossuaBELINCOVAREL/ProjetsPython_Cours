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

"""
Quand devez-vous utiliser la copie superficielle au lieu de la copie profonde, et vice versa ? :

Lorsque vous faites une copie superficielle, un nouvel objet est créé et il conserve les pointeurs de référence de l'objet original. 
Comme le processus de copie superficielle n'est pas récursif, les copies des objets enfants originaux ne sont pas créées. 
En gros, vous avez donc deux objets qui partagent le même ensemble d'éléments. 
Cela signifie que toute modification apportée à l'objet copié se reflète instantanément dans l'objet original.

Dans le cas d'une copie profonde, cependant, un processus de copie récursif est effectué, et des copies de tous les objets enfants sont créées.
Ainsi, si vous apportez une modification à l'objet copié, elle ne se reflétera pas dans l'objet original.

Le moment et la raison pour lesquels vous devriez choisir l'un ou l'autre dépendent du cas d'utilisation, 
mais il est primordial que vous compreniez le fonctionnement interne des deux processus.


"""