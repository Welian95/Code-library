import glob
import sys, os
from datetime import date

# get todays date

today = date.today().strftime("%d.%m.%Y") #todays date with given format


# load all files in the running folder

file_list = glob.glob("*")

# load files by ending - here Excel-file

xlsx_list = glob.glob("*.xlsm")

#gets the first excel in folder

Excel_name = xlsx_list[0] 

# get the directory were this .py is working
print (os.getcwd() )
print ( os.path.realpath("") )

print ( os.path.abspath("s")) 