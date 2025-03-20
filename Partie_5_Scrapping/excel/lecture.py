# Lecture de données de plusieurs fichiers

import openpyxl

wb1 = openpyxl.load_workbook("octobre.xlsx", data_only=True) # Permet de récupérer seulement les valeurs et pas les formules
wb2 = openpyxl.load_workbook("novembre.xlsx", data_only=True)
wb3 = openpyxl.load_workbook("decembre.xlsx", data_only=True)

sheet1 = wb1["Feuil1"]
sheet2 = wb2["Feuil1"]
sheet3 = wb3["Feuil1"]

# Lecture de toutes les ventes pour chaque mois {"Pommes" : (760, 660, 900), "Poires" : (x, x, x)} etc.

def ajouter_data(sheet, d):
    for row in range(2, sheet.max_row):
        nom_article = sheet.cell(row, 1).value
        if not nom_article:
            break
        total_ventes = sheet.cell(row, 4).value
        if d.get(nom_article):
            d[nom_article].append(total_ventes)
        else:
            d[nom_article] = [total_ventes]


donnees = {}
ajouter_data(sheet1, donnees)
ajouter_data(sheet2, donnees)
ajouter_data(sheet3, donnees)


print(donnees)


