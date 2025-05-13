# Rendre possible le in

def element_dans_liste(nom, liste):
    ''' for element in liste:
        if nom.lower() == element.lower():
            return True
        return False '''
    liste_lower = [element.lower() for element in liste]
    return nom.lower() in liste_lower

noms = ["Jean", "Eva", "Sophie", "Martin", "Bill", "Abdel", "Christophe"]

if element_dans_liste("JEAn", noms):
    print("Il est là")
else:
    print("Il n'est pas là")