import kivy

from kivy.app import App #Importieren der Klasse App
from kivy.uix.label import Label #Importieren der Überschrift für die App 
from kivy.uix.gridlayout import GridLayout #Import eines Layouts
from kivy.uix.textinput import TextInput #Import des Layouts für Usereingabeb 
from kivy.uix.button import Button #Importieren des Userlayoutrs für Schalter 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window


class MyGrid(GridLayout): #Klasse welche alle Design-Element enthält, erbt ein Layout von kivy.uix.gridlayout
    #Aufbau der App (Grid etc.)
    def __init__ (self, **kwargs): #Konstruktor für das Layout, **kwargs steht für unendliche viele eingetragbare keywords
        super(MyGrid, self).__init__(**kwargs) #setup the konstruktor
        self.cols = 1 #Anzahl der Spalten im Main-Grid

        #Inside-Grid -- Erstellen eines Gitters in dem Gitter damit man unterschiedlich viele Spalten untereineander nutzen kann 
        self.inside = GridLayout()
        self.inside.cols = 2 # Anzahl der Spalten im Inside_Grid


        self.inside.add_widget(                #erstellen eines Widgets
            Label(text = 'Input the secret code: ', #Erstellen eines Labels im Widget
            font_size = 80  ) )         #Schriftgröße
        self.code = TextInput(font_size = 120 ,multiline = False, text =  "test") #multiline = mehrere Zeilen 
        self.inside.add_widget(self.code)      #Erstellen einer TextInput-Box

        self.add_widget (self.inside) #Einfügen des Inside-Grids als Widget in das Main-Grid

        #Main-Grid

        self.submit = Button (      #Erstellen eines neuen Buttons namens submit
            text ='Code verification',     #Beschriftung des Buttons
            font_size = 80 )        #Schriftgröße anpassen
        self.submit.bind(on_press=self.pressed) #Aktion welche eintrit wenn der Button geklickt wird - hier Ausführen der Funktion pressed
        self.add_widget(self.submit) #Erstellen des Widgets für den Button damit dieser angezeigt wird 


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
        code = self.code.text        #speichern der Eingegebenen Variable self.name als name
        
        if code == correct_code:
            self.textpopup(title='Your input is...', text='Correct !')

        else: 
            self.textpopup(title='Your input is...', text='Incorrect !')

        print (self.code.text)
        self.code.text = ''         #Feld leeren



class CodeCheck (App):  #Erstellen einer eigenen App-Klasse, welche von der Kivy.app erbt. Auch der Konstruktor wiurd vererbt deshalb ist das Auffrufen der __init__ nicht nötig
    def build(self):
        return MyGrid()




if __name__ =='__main__':
    correct_code = input('Input the secret code:')
    CodeCheck().run() #Starten der App mit der Methode 'run' welche MyApp von der Kivy.app geerbt hat