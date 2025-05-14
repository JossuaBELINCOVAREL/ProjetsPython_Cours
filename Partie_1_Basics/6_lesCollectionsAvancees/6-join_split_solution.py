# On demande une entrée utilisateur sous forme d'une seule chaîne
entree = input("Entrez des prénoms séparés par des virgules : ")

# On transforme cette chaîne en liste avec .split()
liste_prenoms = entree.split(",")
print("Liste obtenue :", liste_prenoms)

# On recolle la liste avec " / "
chaine_reformatee = " / ".join(liste_prenoms)
print("Liste formatée avec slash :", chaine_reformatee)
