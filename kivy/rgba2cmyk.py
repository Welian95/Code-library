print ('Konvertieren von RGB in CMYK(Wert zwischen 0-1)\n')

exit = 'no'

while exit == 'no':
    r = int(input('Rot-Anteil: '))
    g = int(input ('Grün-Anteil: '))
    b = int(input ('Blau-Anteil: '))

    print (f'Convertiert in CMYK: \n \n \
        Rot: {r/255}\n \
        Grün: {g/255}\n \
        Blau: {b/255}\n')

    exit = input ('Programm beenden? (yes/no) ')