# function to read xlsx or csv data
## using pandas to import 
### file and .py has to be in the same folder

import pandas as pd

filename = 'file_name.csv' #.csv/.xslm/etc

df_excel = pd.read_excel (filename)

df_csv = pd.read_csv('data.csv', sep = ';' ) #csv/utf seperator

## using xlwings to import 

import xlwings as xw

filename = 'file_name.xlsx'
sheet_name = 'Tabelle1'                        #name of the excel Worksheet

wk = xw.Book(filename) 
sheet = wk.sheets(sheet_name)

df_excel = sheet.range('G4').value             #insert can also be more cells 'A1:C6'

wk.close



#Slicing methods

##Slicing a column by name
df_excel[:,('column_name')]
df_excel['column_name']


##Slice rows in a given range
df_excel[3:6]

##Slice every second row
df_excel[::2]

##Get every data of a row by data greater 10 in another row
df_excel['column_name'][df_excel['column2_name']>10]

##Set a column as index
df_excel = df_excel.set_index('column_name')

##iloc
### get data of 4 row and 1 column
df_excel.iloc[4,1]

##loc
### get data only by row
df_excel.loc['row_index']
### get data of row and column
df_excel.loc['row_index', 'column_name']
### change data of a row 
df_excel.loc['row_index'] = ['data1', 'data2', '...'] #sice of data must be same than row



#Math-functions

##get mean value (Mittelwert)
df_excel.mean()

##sum all values of a column 1
df_excel.sum(axis=1)

##use a function vor every value in dataframe
### build lambda-function f
f = lambda x: x-1 if not x%2 == 0 else x
df_excel.applymap(f)

#Interpolate NaN values 
df_excel.interpolate()


#Sort-methodes 

##sort data by index 
df_excel.sort_index( inplace=True) #

