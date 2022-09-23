import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class FLayout(App):             #This name has to be the name of .kv file
    def build (self):
        return FloatLayout()    #return statement has to be Float layout 


if __name__ == '__main__':
    FLayout().run()