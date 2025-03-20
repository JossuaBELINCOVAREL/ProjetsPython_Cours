from PyPDF2 import PdfFileWriter, PdfFileReader

f = open("Lettre_de_motivation_Enedis_BELIN_Jossua.pdf", "rb") # rb = read binary

reader = PdfFileReader(f) # Création d'un objet PdfFileReader

page0 = reader.getPage(0)
texte = page0.extractText()

f.close()

print(texte)
