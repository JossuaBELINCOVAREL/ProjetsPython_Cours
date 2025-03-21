"""
Le scrapping consiste en la collecte/extraire des données sur un site web.
Tout ce qu'on voit sur un site internet peut-être récupérer.

Possible d'utiliser des bibliothèques/framework comme requests, BeautifulSoup, Scrapy, etc.

Certains sites se protège (possible de contourner avec le Headless browsing)

"""

from bs4 import BeautifulSoup

# Lecture des données du fichier html
f = open("recette.html", "r")
html_content = f.read()
f.close()
soup = BeautifulSoup(html_content, "html.parser")

titre_h1 = soup.find("h1") # <- Cherche le premier h1
description_div = soup.find("p", class_="description") # <- Cherche le premier p ayant la class description

div_info = soup.find("div", class_="info")
source_img = div_info.find("img")

print("Titre de la page :", titre_h1.text)
print("Paragraphe de description :", description_div.text)
print("La source de l'image est :", source_img["src"])



