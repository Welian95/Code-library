# On Microsoft
import ctypes  # An included library with Python install.   

###ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

##  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | Cancel 
##  6 : Cancel | Try Again | Continue




# On MacOS
import easygui #pip install easygui

easygui.msgbox('This is the message!', title='simple gui')
