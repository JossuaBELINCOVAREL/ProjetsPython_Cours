# JSON 
# Deserialiser le format TXT -> en DATA
    #-> Fonction loads()

import json

chemin_fichier = r"C:\Users\jossu\Documents\perso\Formations\Python\projets\projets_pour_repo\Partie_5_Scrapping\json\personne_json.txt"
    
with open (chemin_fichier, "r") as f:
    personne = json.loads(f.read())
print(personne)