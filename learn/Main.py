# Importieren eines anderen Pythonskripts 

import TestPrint #Anderes Pythonskript

import Klassen

import Vererbung

#Achtung! beim Import von Skripten ohne 'if name = main'-funktion werden diese automatisch ausgeführt!

#Anwendung der Main Funktion

if __name__ == '__main__': #Alles hierunter wird nur ausgeführt wenn diese Datei ausgeführt wird - beim Import nicht 

    print (TestPrint.funk()) #Ausführen einer Funktion aus enem anderen Skript 

    instanz= Klassen.MyClass() #Zugriff auf eine Klasse aus einer anderen Datei

    print( instanz.buchstabe) #Aufrufen einer Variable der Klasse 
