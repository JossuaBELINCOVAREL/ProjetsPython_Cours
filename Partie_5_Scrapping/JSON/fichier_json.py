# JSON 
# Manipulation des données structurées
# cf JSON editor online pour tester si besoin


# Sérialiser la DATA -> en format TXT
    #-> Fonction dumps()
# Deserialiser le format TXT -> en DATA
    #-> Fonction loads()

import json
    
personne = {
    "nom": "Eva",
    "age": 30,
    "amis" : ["Alice", "Bob"]
}

personne_json = json.dumps(personne) # <- serialisation
print("JSON:" + personne_json)


# création du fichier fichier_json.txt json dans le même répertoire que ce fichier

chemin_fichier = r"C:\Users\jossu\Documents\perso\Formations\Python\projets\projets_pour_repo\Partie_5_Scrapping\json\personne_json.txt"

with open(chemin_fichier, "w") as f:
    f.write(personne_json)



# print(f"Fichier fichier_json.txt créé ici : {chemin_fichier}")

f.close()
