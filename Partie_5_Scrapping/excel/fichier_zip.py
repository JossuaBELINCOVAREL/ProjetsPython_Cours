import zipfile

fichier_zip = zipfile.ZipFile("fichiers_excel.zip", 'w', zipfile.ZIP_DEFLATED)
fichier_zip.write("octobre.xlsx")
fichier_zip.write("novembre.xlsx")
fichier_zip.write("decembre.xlsx")
fichier_zip.close()