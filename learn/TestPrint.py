#Ein paar Dinge die in der Main Funktion ausgeführt werden sollen 

def pt ():
    print('Hello World')

def funk (n=0):
    x = n + 42

    return x

print ('Ich stehe vor der main-funktion')

if __name__ == '__main__' :  #Alles hierunter wird nur ausgeführt wenn diese Datei ausgeführt wird - beim Import nicht 
    print('Ich stehe nach der main-funktion')
