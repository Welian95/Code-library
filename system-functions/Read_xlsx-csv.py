# function to read xlsx or csv data

import pandas as pd

filename = 'file_name.xlsx' #.csv/.xslm etc

df_excel = pd.read_excel (filename)

df_csv = pd.read_csv('data.csv', sep = ';' ) #csv/utf seperator


#Slicing methods

##Slicing a column by name
df_excel[:,('column_name')]
