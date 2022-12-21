from docxtpl import DocxTemplate, InlineImage #pip install docxtpl
from datetime import date
from random import randint
import glob
import pandas as pd #pip install pandas
import os, sys
from PIL import Image #pip install pillow
from docx.shared import Cm, Inches , Mm , Emu
import shutil


import xlwings as xw #pip install xlwings

import kivy         #pip install kivy

from kivy.app import App #Importieren der Klasse App
from kivy.uix.label import Label #Importieren der Überschrift für die App 
from kivy.uix.gridlayout import GridLayout #Import eines Layouts
from kivy.uix.textinput import TextInput #Import des Layouts für Usereingabeb 
from kivy.uix.button import Button #Importieren des Userlayoutrs für Schalter 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy_deps import sdl2, glew

class MyGrid(GridLayout): 

    #Aufbau der App (Grid etc.)
    def __init__ (self, **kwargs): 
        super(MyGrid, self).__init__(**kwargs) 
        self.cols = 1                               #Anzahl der Spalten im Main-Grid

        #Inside-Grid -- Erstellen eines Gitters in dem Gitter damit man unterschiedlich viele Spalten untereineander nutzen kann 
        self.inside = GridLayout()
        self.inside.cols = 2                        #Anzahl der Spalten im Inside_Grid


        self.inside.add_widget(                     #erstellen eines Widgets
            Label(text = 'Pfad zum Vorlagen-Ordner: \n(Wordvorlage)',   #Erstellen eines Labels im Widget
            font_size = 20  ) )                     #Schriftgröße
        self.template = TextInput(font_size = 20 ,multiline = True, text = "" ) #multiline = mehrere Zeilen 
        self.inside.add_widget(self.template)           #Erstellen einer TextInput-Box

        self.inside.add_widget(                     #erstellen eines Widgets
            Label(text = 'Pfad zum Projekt-Ordner: \n(-Berichtsdaten.xlsm \n -"pictures"-Ordner\n-Ausgabe)',  #Erstellen eines Labels im Widget
            font_size = 20  ) )                     #Schriftgröße
        self.place = TextInput(font_size = 20 ,multiline = True, text = "" ) #multiline = mehrere Zeilen 
        self.inside.add_widget(self.place)           #Erstellen einer TextInput-Box
        
        self.inside.add_widget(                     #erstellen eines Widgets
            Label(text = 'Anzahl übersprungender Arbeitsmappen: \n(Achtung! nicht ändern wenn nicht notwendig!)',   #Erstellen eines Labels im Widget
            font_size = 12  ) )                     #Schriftgröße 
        self.no_iteres = TextInput(font_size = 12 ,multiline = True, text = "9")
        self.inside.add_widget(self.no_iteres)           #Erstellen einer TextInput-Box

        self.add_widget (self.inside)               #Einfügen des Inside-Grids als Widget in das Main-Grid
        
        #Main-Grid

        self.submit = Button (                      #Erstellen eines neuen Buttons namens submit
            text ='Bericht generieren',             #Beschriftung des Buttons
            font_size = 40 )                        #Schriftgröße anpassen
        self.submit.bind(on_press=self.pressed)     #Aktion welche eintrit wenn der Button geklickt wird - hier Ausführen der Funktion pressed
        self.add_widget(self.submit)                #Erstellen des Widgets für den Button damit dieser angezeigt wird 


    #Pop-up window 
    def textpopup(self, title='', text=''):
        """Open the pop-up with the name.

        :param title: title of the pop-up to open
        :type title: str
        :param text: main text of the pop-up to open
        :type text: str
        :rtype: None
        """
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=text,))
        popup = Popup(title=title, content=box ,size_hint=(None, None), size=(800, 200) )
        popup.open()

    def pressed(self, instance):
        '''This is a funktion to give the button an aktion '''
        #speichern der Eingegebenen Variable self.name als name
        run_path= str(rf'{self.place.text}')
        
        template_path = str(rf'{self.template.text}')
        
        run_path = run_path.replace('\\',"\\\\")
        

        
        template_path = template_path.replace('\\',"\\\\")

        print( run_path,template_path)
        #self.place.text = ''         #Feld leeren
        #self.template.text= '

        ###################################################Berichtsdaten##################################################################################
        
        #get todays date
        today = date.today().strftime("%d.%m.%Y") #todays date with given format
        
        #Input names:
        os.chdir(run_path)

        path_pictures = rf'{run_path}\pictures' #Pfad für Bilder
        path_picture_source = rf'{template_path}pictures'

        # ## Find Word-Template-file
        word_list =[ item for item in os.listdir(template_path) if item.endswith('.docx')] #list of all files that end with .xlsm in Folder
        docx_name = rf'{template_path}\{word_list[0]}' #gets the #Pfad der Vorlage

        # ## Find Excel-Template-file
        excel_list_source =[ item for item in os.listdir(template_path) if item.endswith('.xlsm')] #list of all files that end with .xlsm in Folder
        excel_source = rf'{template_path}\{excel_list_source[0]}' #gets the #Pfad der Vorlage


        #check Excel path and if path not exist create a new one
        if not glob.glob(run_path + '/' + '*.xlsm'): 
            shutil.copy(excel_source, run_path)

        # Check picture path and if path not exist create a new one
        if not os.path.exists(path_pictures): 
 
            shutil.copytree(path_picture_source, path_pictures)


        #List all picture files
        picture_list =[ item for item in os.listdir(path_pictures) if item.endswith('.png')] #List all picture files


        # ## Load Excel-file
        xlsx_list =[ item for item in os.listdir(run_path) if item.endswith('.xlsm')] #list of all files that end with .xlsm in Folder
        Excel_name = xlsx_list[0] #gets the first excel in folder
        wk = xw.Book(Excel_name) # opens excel-file
        no_itersheets = int(self.no_iteres.text)            #Anzahl der nicht zur Iteration genutzten Arbeitsblätter im Bericht, von Startseite bis X. Ab X dürfen nur noch iterierbare Tabellenblätter kommen. (Abbildungsblätter werden nicht gezählt)

        # ### create data out of excel sheets  --- Iterationsblätter

        context_data ={}
        for i in list(wk.sheets)[no_itersheets:]: #begin with the no_itersheets. worksheet !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            sheet = wk.sheets(i)
            context_data.update ( {str(i).split(']')[-1].split('>')[0] : sheet['A9'].expand().options(pd.DataFrame,numbers=int,empty='', dtype=str,chunksize=10_000).value.reset_index().to_dict('records')   }) #Name deklarieren und Einlesen des Inhalts-> Speichert alle Werte(.values) ab 'A9' als DataFrame, Chunksize = Matrixgröße ,numbers = int -> keine Dezimalstellen,empty=''->leere zellen sind nicht 'none',  )
            
            
        for i in list(context_data.keys()):        #for every key (with dict as value)
            for j in range(len(context_data[i])):  #go over every list, wich is in the top dict   
                context_data[i][j] = {k: v for k, v in context_data[i][j].items() if v != ''} #go over every dict in list and delete every key-value-pair if value is None ('')
        
        for i in list(context_data.keys()):
            context_data[i] = [item for item in context_data[i] if item] #delete every empty dict


        # ### Textvariablen-sheet (Startseite)

        sheet = wk.sheets(1) #opens first map in excel

        df_data = sheet['A9'].expand().options(pd.DataFrame, chunksize=10_000).value #Einlesen des Inhalts-> Speichert alle Werte(.values) ab 'A2' als DataFrame, Chunksize = Matrixgröße


        #Get data from excel to resize the pictures
        df_pic_size= sheet['F10'].expand().options(pd.DataFrame, chunksize=10_000).value.index.tolist()
        df_pic_size = [int (x) for x in df_pic_size]
        df_pic_size = [str (x) for x in df_pic_size]

        ###df_data
        text_data = df_data.iloc[:,0].to_dict() #Dateframes first column to dict
        text_data['today']=today #add todays date

        ###text_data

        objektname = text_data['Objektname'] #decline Name of objkt
        auftraggeber = text_data['Auftraggeber'] #decline Name of company


        # ## Load all Pictures 

        picture_w_ending = [picture.split('\\')[-1] for picture in picture_list]


        # ### Get all picture names 

        picture_name = [picture.split('.')[0] for picture in picture_w_ending]




        # ### Load docx-file to write in it 


        doc = DocxTemplate(docx_name) 

 

        g = [f'pictures\\{i}'for i in picture_list] #name of all pics


        d = df_pic_size #Size of all pics 

        imagen = []
        for (a,b) in zip (g,d):
            imagen.append ( f'(InlineImage(doc,"{a}", Cm({b})))')



        ###imagen


        # ### write an dict to to dicline names to code 


        image_dict = {}
        #doc = [] # must be dicline but gets overwritten later 

        for (name, link)  in zip (picture_name, imagen):

            image_dict.update({name : eval(link)})
            

        # ### create one dict out off multile dicts 

        dicts = [text_data,image_dict] 


        for dict in dicts:
            context_data.update(dict)
            

        # ## Create Context to write in word 
        context = context_data


        # ### write into word


        doc.render(context)     #render context into document


        doc.save(f'§{today}_{objektname}_{auftraggeber}.docx') #save document with new ending count


        # ### Bildvariablen in Excel schreiben 

        picture_name = ['{{' + i + '}}' for i in picture_name]

        ###picture_name



        pic_vars = pd.DataFrame(picture_name)

        sheet = wk.sheets(1) #Öffnen der Excel-Arbeitsmappe 
        df = sheet.range('E10').value = pic_vars.set_index(0)

        wk.close

        # popup if done

        self.textpopup(title='AutoWordBericht.exe', text='Ihr Bericht wurde erfolgreich generiert!')



#Ausführen der App

class MyApp (App):  #Erstellen einer eigenen App-Klasse, welche von der Kivy.app erbt. Auch der Konstruktor wiurd vererbt deshalb ist das Auffrufen der __init__ nicht nötig
    def build(self):
        return MyGrid()

if __name__ =='__main__':
    MyApp().run() #Starten der App mit der Methode 'run' welche MyApp von der Kivy.app geerbt hat