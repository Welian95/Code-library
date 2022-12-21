# Importieren der benötigten Bibliotheken
import os
from PyPDF2 import PdfFileMerger

#os.chdir(r'C:\Users\Jwesterhorstmann\Desktop\GIT\pdf-editing')

#os.chdir(os.getcwd())

# Definieren der Pfade zu den beiden PDFs
pdf1_path = r"C:\Users\Jwesterhorstmann\Desktop\Neuer Ordner (2)"
pdf2_path = r"C:\Users\Jwesterhorstmann\Desktop\Neuer Ordner (2)"

# Öffnen der beiden PDFs
pdf1 = open(pdf1_path, "rb")
pdf2 = open(pdf2_path, "rb")

# Initialisieren des PDF-Mergers
merger = PdfFileMerger()

# Hinzufügen der beiden PDFs zum Merger
merger.append(pdf1)
merger.append(pdf2)

# Definieren des Ausgabe-Pfades und des Dateinamens der neuen PDF
output_path = r"C:\Users\Jwesterhorstmann\Desktop\Neuer Ordner (2)"

# Schreiben der neuen PDF
with open(output_path, "wb") as output:
    merger.write(output)

# Schließen der PDFs
pdf1.close()
pdf2.close()
