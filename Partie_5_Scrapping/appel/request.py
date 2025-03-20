# FAIRE DES APPELS RÉSEAU AVEC REQUESTS
# possible avec:  .txt // .html // .json

import requests

reponse = requests.get("https://index.html")
if reponse.status_code == 200:
    reponse.encoding = "utf-8"
    print(reponse.text)
else:
    print("ERREUR code : " + str(reponse.status_code))