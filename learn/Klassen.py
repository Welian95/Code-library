#Anwendungen von Klassen lernen 

## Zuweisungen von mehreren Variablen zu einer Klasse ähnlich wie bei Funktionen 

### Erste Klasse

class MyClass: #Dies ist ein Klasseobjekt mit dem Typ 'class' (eigener Variablentyp)
    zahl = 42 #Dies ist das erste Statement der Klasse MyClass 
    string = 'Zeichenkette' #String-Variable
    #Besonderheit die Liste wird im Gegensatz zu den anderen Variablen in allen Instanzen verändert! 
    #list = [] #Um das überschreiben zu vermeiden muss diese in die __init__-Funktion geschrieben werden (siehe unten) 

    #Besonderheit! Funktion definieren in der Klasse:

    def do_something(self, neuezahl): #Immer self als erste Variable
        
        self.zahl = neuezahl #Überschreiben der Variablen Zahl in der Klasse mit der neuen Zahl
        self.list.append(neuezahl)
        #Achtung! auf Klassenvariablen wird immer mit Self zugegriffen 



#Konstruktoren:

##Erster Konstruktor in der Klasse MyClass

    def __init__(self, buchstabeneu = 'a'): #defaultwert falls in Myclass nichts angegeben! 
        self.buchstabe = buchstabeneu #Wert-Zuweisung der Variable buchstabe durch eingabe eines Wertes in MyClass (siehe unten)
        self.list = [] #jetzt wird die Liste nur bei instanz überschrieben!



# Ausgabe 
if __name__ == '__main__':

    #Erstellen einer Instanz der Klasse:
    instanz = MyClass() #init bekommt default wert 

    instanz.do_something(10) #Ausführung der Funktion in der Klasse

    #Erstellen der 2. Instanz - Unterschiede zur ersten beachten! (die do_something funktion wurde hier nicht angewandt)
    instanz2 = MyClass('Ich bin instanz2') #init Variable wird überschrieben

    print (instanz.buchstabe, instanz.zahl, instanz.string, instanz.list) #Zugriff auf die Instanzvariablen wie Zugriffsoperator '.'

    print (instanz2.buchstabe, instanz2.zahl, instanz2.string, instanz2.list) #Zugriff auf den Konstruktor
