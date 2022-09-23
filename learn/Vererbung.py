#Verervbung

class Lebewesen:
    augen = 3
    def __init__ (self): #Konstruktor von Lebewesen
        self.art = 'säuger'

    def lebe (self):
        self.augen = 2

#Die Klasse Hund wird zur Unterklasse der Klasse Lebewesen (dadurch erbt Klasse Hund die Atribute(Variablen) der Klasse Lebewesen)
#Konstruktoren werden nicht vererbt und müssen zusätzlich zugewiesen werden!!
class Hund(Lebewesen):
    beine = 4
    name = ''

    def __init__ (self): #Konstruktor von Hund
        Lebewesen.__init__(self)
    

    def do_something(self, augenzahl):
        self.augen = augenzahl

    #Ändern eines geerbten Attributes -> Ersetzt die lebe Methode aus Lebewesen
    def lebe (self): #gleich Syntax wie bei der übergeordneten Klasse verwenden!
        Lebewesen.lebe(self) #Erben von Lebewesen! muss gemacht werden sonst wird nicht geerbt
        self.beine= 43 #hinzufügen eines weitern Befehls 

fiffi = Hund()
fiffi.do_something(42)
fiffi.lebe()
print(f'Art:{fiffi.art} ,Augen:{ fiffi.augen},Beine:{fiffi.beine}')

#Merke durch das Wiederholte aufrufen von Methoden/Attributen (Variablen) in der Unterklasse, Werden die Atrribute der Oberenklasse (welche vererbt hat) verschattet (überschrieben) 
