# Utilisation de la bibliothèque PyPDF2
import PyPDF2

# Nous allons combiner les PDFs

from PyPDF2 import PdfFileWriter, PdfFileReader

# Création d'un objet PdfFileWriter

contenu_sortie = PdfFileWriter()

# Ouverture des PDFs

fichier_pdf1 = open("CV_BELIN_Jossua_CDP.pdf", "rb") # rb = read binary
fichier_pdf2 = open("CV_BELIN-COVAREL_Jossua.pdf", "rb")

reader_pdf1 = PdfFileReader(fichier_pdf1) # Création d'un objet PdfFileReader
reader_pdf2 = PdfFileReader(fichier_pdf2)

print("Nombre de pages dans le PDF 1 : ", reader_pdf1.getNumPages())

contenu_sortie.addPage(reader_pdf1.getPage(0))
contenu_sortie.addPage(reader_pdf2.getPage(0))

# Création du PDF de sortie

fichier_sortie = open("fichier_sortie.pdf", "wb") # wb = write binary
contenu_sortie.write(fichier_sortie)

fichier_sortie.close()
fichier_pdf1.close()
fichier_pdf2.close()
