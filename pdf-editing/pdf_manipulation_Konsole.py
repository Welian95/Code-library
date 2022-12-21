from pdf2docx import Converter
from PyPDF2 import  PdfMerger
import glob, os, sys




def convert():
    '''funktion top convert all pdf.files in a given folder to a docx-files
    param pdf_folder: a system link to a folder'''
    pdf_fileS = glob.glob (f'{pdf_folder}\*pdf') #Liste mit allen pdf Daten im angegebenen Ordner 

    for i in range (len(pdf_fileS)):
        pdf_name = pdf_fileS[i].split('\\')[-1].split('.')[0]    #Name der PdfDatei 
        docx_name = pdf_name + '.docx'                          #Name der DocxDatei
        
        pdf_file = pdf_folder + f'\{pdf_name}.pdf'
        doxc_file = pdf_folder + f'\{docx_name}'

        cv = Converter(pdf_file)
        cv.convert(doxc_file)
        cv.close        

def merge():
    ''' a function to merge every pdf-file in working directory
    param: None'''
    pdf_list = glob.glob (f'{pdf_folder}\*pdf') #Liste mit allen pdf Daten im angegebenen Ordner 

    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)
    
    file_name = "Merged.pdf"

    # Prüfe, ob die Datei bereits im aktuellen Ordner vorhanden ist
    if os.path.exists(file_name):
    # Wenn die Datei bereits vorhanden ist, füge eine laufende Nummer hinzu,
    # um die Datei zu unterscheiden
        i = 1
        while os.path.exists(f"{file_name.split('.')[0]}_{i}.pdf"):
            i += 1
        file_name = f"{file_name.split('.')[0]}_{i}.pdf"

    # Erstelle die Datei im aktuellen Ordner
    merger.write(file_name)
    merger.close()

##pdf_folder = r"C:\Users\Jwesterhorstmann\Desktop\NeuerOrdner2"
#os.chdir(r"C:\Users\Jwesterhorstmann\Desktop\NeuerOrdner2") #Change Working directory
##convert()
#merge()

if __name__ == "__main__":

    Option = "run"

    while Option != "exit" or"J"or "j" "Ja" or "ja" or "Y" or "y" or"Yes" or "yes": #while schleife damit das programm weiter läuft


        print('Herzlich Wilkommen zum PDF-Manipulations-Programm der Firma Bode\n\
            _____________________________________________________________________\n\
                \n Die ist ein Programm, um den Umgang mit PDF-Dateien zu vereinfachen.\n\
                \n Als erstes müssen Sie einen Ordner-Pfad angeben in dem die zu bearbeitenden PDFs abgelegt sind.\n\
                \nDanach müssen Sie eine der folgenden Optionen wählen.\n\
                    \n1. Alle PDFs in Word Datein konvertieren\n\
                        \n2. Alle PDFs zu einer zusammenführen\n\
                        _____________________________________________________________________\n\
                            \nDas Programm kann jederzeit durch den Befhel (exit) geschlossen werden.')

        pdf_folder = input ("\nBitte geben Sie den Pfad zum Ordner an:\n")
        os.chdir(pdf_folder) #Change Working directory
        
        
        # Alle Dateien im Ordner aufgelistet
        files = os.listdir(pdf_folder)

        # Alle Dateien mit der Endung .txt auflisten
        pdf_files = [file for file in files if file.endswith(".pdf")]

        Option = input ("\nGeben Sie die Option an (1/2):\n")

        if Option == str(1):
            convert()
        elif Option == str(2):
            merge()
            print(f'\n---\npdfs merged\n---\n\
                \nFolgende Datein wurden zusammengeführt:\n{pdf_files}\n')
        else :
             Option = input ("\nProgramm schließen? (exit)\n")
