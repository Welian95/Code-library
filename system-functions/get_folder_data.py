import glob
from datetime import date

# get todays date

today = date.today().strftime("%d.%m.%Y") #todays date with given format


# load all files in the running folder

file_list = glob.glob("*")

# load files by ending - here Excel-file

xlsx_list = glob.glob("*.xlsm")

#gets the first excel in folder

Excel_name = xlsx_list[0] 


print (file_list)