import kivy
from kivy.app import App #Importieren der Klasse App
from kivy.uix.label import Label #Importieren der Überschrift für die App 
from kivy.uix.gridlayout import GridLayout #Import eines Layouts
from kivy.uix.textinput import TextInput #Import des Layouts für Usereingabeb 
from kivy.uix.button import Button #Importieren des Userlayoutrs für Schalter 

class MyGrid(GridLayout): #Klasse welche alle Design-Element enthält, erbt ein Layout von kivy.uix.gridlayout
    def __init__ (self, **kwargs): #Konstruktor für das Layout, **kwargs steht für unendliche viele eingetragbare keywords
        super(MyGrid, self).__init__(**kwargs) #setup the konstruktor
        self.cols = 1 #Anzahl der Spalten im Main-Grid

        #Inside-Grid -- Erstellen eines Gitters in dem Gitter damit man unterschiedlich viele Spalten untereineander nutzen kann 
        self.inside = GridLayout()
        self.inside.cols = 2 # Anzahl der Spalten im Inside_Grid


        self.inside.add_widget(                #erstellen eines Widgets
            Label(text = 'First Name: ') )     #Erstellen eines Labels im Widget  
        self.name = TextInput(multiline = False) #multiline = mehrere Zeilen 
        self.inside.add_widget(self.name)      #Erstellen einer TextInput-Box

        self.inside.add_widget(                #erstellen eines Widgets
            Label(text = 'Last Name: ') )     #Erstellen eines Labels im Widget  
        self.lastname = TextInput(multiline = False) #multiline = mehrere Zeilen 
        self.inside.add_widget(self.lastname)      #Erstellen einer TextInput-Box

        self.inside.add_widget(                #erstellen eines Widgets
            Label(text = 'E-Mail: ') )     #Erstellen eines Labels im Widget  
        self.email = TextInput(multiline = False) #multiline = mehrere Zeilen 
        self.inside.add_widget(self.email)     #Erstellen einer TextInput-Box

        self.add_widget (self.inside) #Einfügen des Inside-Grids als Widget in das Main-Grid

        #Main-Grid

        self.submit = Button (      #Erstellen eines neuen Buttons namens submit
            text ='drück mich',     #Beschriftung des Buttons
            font_size = 40 )        #Schriftgröße anpassen
        self.submit.bind(on_press=self.pressed) #Aktion welche eintrit wenn der Button geklickt wird - hier Ausführen der Funktion pressed
        self.add_widget(self.submit) #Erstellen des Widgets für den Button damit dieser angezeigt wird 

    def pressed(self, instance):
        '''This is a funktion to give the button an aktion '''
        name = self.name.text        #speichern der Eingegebenen Variable self.name als name
        last = self.lastname.text    #""
        email = self.email.text      #""
        print(f'name: {name}\n last name: {last}\n email: {email}') #Ausgabe der Usereingabe in der Konsole
        self.name.text = ''         #Feld leeren
        self.lastname.text = ''      #Feld leeren 
        self.email.text = ''         #Feld leeren

class MyApp (App):  #Erstellen einer eigenen App-Klasse, welche von der Kivy.app erbt. Auch der Konstruktor wiurd vererbt deshalb ist das Auffrufen der __init__ nicht nötig
    def build(self):
        return MyGrid()




if __name__ =='__main__':
    MyApp().run() #Starten der App mit der Methode 'run' welche MyApp von der Kivy.app geerbt hat 


