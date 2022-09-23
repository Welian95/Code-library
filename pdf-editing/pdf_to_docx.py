from pdf2docx import Converter
import glob
from kivy.app import App #Importieren der Klasse App
from kivy.uix.label import Label #Importieren der Überschrift für die App 
from kivy.uix.gridlayout import GridLayout #Import eines Layouts
from kivy.uix.textinput import TextInput #Import des Layouts für Usereingabeb 
from kivy.uix.button import Button #Importieren des Userlayoutrs für Schalter 
import pygame

class MyGrid(GridLayout): #Klasse welche alle Design-Element enthält, erbt ein Layout von kivy.uix.gridlayout
    def __init__ (self, **kwargs): #Konstruktor für das Layout, **kwargs steht für unendliche viele eingetragbare keywords
        super(MyGrid, self).__init__(**kwargs) #setup the konstruktor
        self.cols = 1 #Anzahl der Spalten im Main-Grid

        #Inside-Grid -- Erstellen eines Gitters in dem Gitter damit man unterschiedlich viele Spalten untereineander nutzen kann 
        self.inside = GridLayout()
        self.inside.cols = 2 # Anzahl der Spalten im Inside_Grid

        self.inside.add_widget(                #erstellen eines Widgets
            Label(color =(0.388, 0.655, 0.219, 1), text = 'Pfad zum Ordner: ',font_size=  40  ) )   #Erstellen eines Labels im Widget  
        self.pfad = TextInput(multiline = True) #multiline = mehrere Zeilen 
        self.inside.add_widget(self.pfad)      #Erstellen einer TextInput-Box

        self.add_widget (self.inside) #Einfügen des Inside-Grids als Widget in das Main-Grid

        pdf_folder =''

        #Main-Grid
        self.submit = Button (      #Erstellen eines neuen Buttons namens submit
            background_color =(0.388, 0.655, 0.219, 1),
            text ='PDF-files umwandeln',     #Beschriftung des Buttons
            font_size = 40 )        #Schriftgröße anpassen
        self.submit.bind(on_press=self.pressed)
        #self.submit.bind(on_press=self.pdf_converter(pdf_folder)) #Aktion welche eintrit wenn der Button geklickt wird - hier Ausführen der Funktion pressed
        self.add_widget(self.submit) #Erstellen des Widgets für den Button damit dieser angezeigt wird 

    def pressed(self, instance):
        '''This is a funktion to give the button an aktion '''
        pdf_folder = self.pfad.text        #speichern der Eingegebenen Variable self.name als name
        self.pfad.text = ''         #Feld leeren
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

class pdf2docxApp (App):  #Erstellen einer eigenen App-Klasse, welche von der Kivy.app erbt. Auch der Konstruktor wiurd vererbt deshalb ist das Auffrufen der __init__ nicht nötig
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    pdf2docxApp().run() #Starten der App mit der Methode 'run' welche MyApp von der Kivy.app geerbt hat 

    
#pdf_folder = r'C:\Users\Jwesterhorstmann\Desktop\VSC-Projekte\PDF-Bearbeitung\PDFtoDocx'