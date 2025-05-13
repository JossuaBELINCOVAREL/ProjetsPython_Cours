# -------------------------
# Avec une LISTE
# -------------------------

contacts_liste = [
    ("Alice", "0611223344", "Paris"),
    ("Benoît", "0622334455", "Lyon"),
    ("Claire", "0633445566", "Marseille"),
]

# Fonction pour rechercher un contact par prénom
def chercher_contact_liste(prenom, liste):
    for contact in liste:
        if contact[0] == prenom:
            return contact
    return None

contact = chercher_contact_liste("Claire", contacts_liste)
print("Recherche via liste :")
print(contact)
print()

# -------------------------
# Avec un DICTIONNAIRE
# -------------------------

contacts_dict = {
    "Alice": ("0611223344", "Paris"),
    "Benoît": ("0622334455", "Lyon"),
    "Claire": ("0633445566", "Marseille"),
}

contact = contacts_dict.get("Claire")
print("Recherche via dictionnaire :")
if contact is None:
    print("Contact introuvable.")
else:
    print(contact)
