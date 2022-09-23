from kivy.app import App                        #Importieren der Klasse App
from kivy.uix.widget import Widget              #Wird genutzt um kv files zu verwenden 
from kivy.properties import ObjectProperty      #Wird genutzt um die Variblen aus der .kv Datei auslesen zu können 

#Lerning kv design language 


class MyGrid(Widget):                           #Klasse welche alle Design-Element enthält, erbt ein Layout von kivy.uix.widget #Das Layout wird in der .kv-Datei bestimmt
    name_var = ObjectProperty(None)             #Auslesen der Variable 'name_var' aus der .kv-Datei - der Wert ist None bis dieser ausgelesen wurde
    email_var = ObjectProperty(None)            #""                         


    def Button(self):                           #Funktion, welche beim Drücken des Buttons ausgelöst wird 
        print(f'name: {self.name_var.text}\
            \ne-mail: {self.email_var.text}')   #Ausgabe der Eingabe in der Konsole ! Achtung 'self.*_var.text' da es sich um Klassenvariablen handelt 
        self.name_var.text = ''                 #Eingabefeld leeren
        self.email_var.text = ''                #""


class MyApp(App):                               #Erstellen einer eigenen App-Klasse, welche von der Kivy.app erbt. Auch der Konstruktor wiurd vererbt deshalb ist das Auffrufen der __init__ nicht nötig
    def build(self):                            #Achtung! der Name der .kv-Datei muss gleich mit dem Namen dieser Klasse sein außgenommen der silbe 'app'!
        return MyGrid()                         #der Name der .kv Datei muss klein geschrieben sein!




if __name__ == '__main__':

    MyApp().run()                               #Starten der App 