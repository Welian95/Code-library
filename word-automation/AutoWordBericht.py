#!/usr/bin/env python
# coding: utf-8

# ### Ausfüllen des Handbuchs 

# In[1]:


from docxtpl import DocxTemplate, InlineImage
from datetime import date
from random import randint
import pandas as pd
import glob
import os
from PIL import Image

#Excel:
import xlwings as xw


# ### get todays date

# In[2]:


today = date.today().strftime("%d.%m.%Y") #todays date with given format


# ## Load Excel-file

# ### list of all files that end with .xlsx in Folder

# In[3]:


xlsx_list = glob.glob("*.xlsm")
xlsx_list


# In[4]:


Excel_name = xlsx_list[0] #gets the first excel in folder


# In[5]:


wk = xw.Book(Excel_name) # opens excel-file


# # Get every sheet that exists 

# In[6]:


###wk.sheets


# Sheet_Names = [ str(list(sheets.keys())[a]).split(']')[-1].split('>')[0] for a in range (len (wk.sheets)) ]
# 
# Sheet_Names

# Sheet_Names[1:]

# context_data ={}
# 
# for i in range (len (Sheet_Names[1:])):
#     

# ### Create a dict with all excel tabels (beside nr.1) and but every row do another dict 

# In[7]:


context_data ={}


# In[8]:


context_data ={}
for i in list(wk.sheets)[1:]: #begin with the second worksheet
    sheet = wk.sheets(i)
    context_data.update ( {str(i).split(']')[-1].split('>')[0] : sheet['A9'].expand().options(pd.DataFrame,numbers=int,empty='', dtype=str,chunksize=10_000).value.reset_index().to_dict('records')   }) #Name deklarieren und Einlesen des Inhalts-> Speichert alle Werte(.values) ab 'A9' als DataFrame, Chunksize = Matrixgröße ,numbers = int -> keine Dezimalstellen,empty=''->leere zellen sind nicht 'none',  )
    
#context_data


# ### Textvariablen-sheet 

# In[9]:


sheet = wk.sheets(1) #opens first map in excel


# In[10]:


df_data = sheet['A9'].expand().options(pd.DataFrame, chunksize=10_000).value #Einlesen des Inhalts-> Speichert alle Werte(.values) ab 'A2' als DataFrame, Chunksize = Matrixgröße

###df_data


# In[11]:


text_data = df_data.iloc[:,0].to_dict() #Dateframes first column to dict

text_data['today']=today #add todays date

###text_data


# In[12]:


objektname = text_data['Objektname'] #decline Name of objkt


# ## Load all Pictures 

# ### list of all files that are in folder 'pictures'

# ### Get all png files

# In[13]:


picture_list = glob.glob("pictures/*.png")

###picture_list


# In[14]:


picture_w_ending = [picture.split('\\')[-1] for picture in picture_list]

###picture_w_ending


# ### Get all picture names 

# In[15]:


picture_name = [picture.split('.')[0] for picture in picture_w_ending]

###picture_name


### ### Read a Table with fig sizes
##fig_sizes = wk.sheets[0]['F10'].expand().options(pd.DataFrame,chunksize=10_000).value.reset_index()
##
#####fig_sizesfig_sizes.iloc[0,0] #Breitefig_sizes.iloc[0,1] #Längeim_size_laenge = []
##im_size_breite = []
##
##for i in range(len(picture_list)):
##                image = Image.open(glob.glob("pictures/*.png")[i])
##                im_size_laenge.append(image.size[0])
##                im_size_breite.append(image.size[1])
##                
##pd.DataFrame(im_size_breite,im_size_laenge)
### ### Change every given PNG-file in folder to given size 
##for i in range(len(picture_list)):
##                image = Image.open(glob.glob("pictures/*.png")[i])
##                image = image.resize((int(fig_sizes.iloc[i,0]),int(fig_sizes.iloc[i,1])),Image.ANTIALIAS)
##                image.save(fp=f'pictures/{picture_w_ending[i]}')
### ## Load Word-file

# ### list of all files that end with .docx

# In[16]:


docx_name = glob.glob("*.docx")

###docx_name


# ### decline filename

# In[17]:


docx_name = docx_name[0] #gets first docx in folder

###docx_name


# ### Load docx-file to write in it 

# In[18]:


doc = DocxTemplate(docx_name) 

###doc


# ## Insert Pictures

# In[19]:


###InlineImage(doc,"pictures\\Auflistung_Transmission.png",width)


# ### write an insert code for each picture given 

# In[20]:


imagen = [f'(InlineImage(doc,"{i}"))' for i in glob.glob("pictures/*.png")]

###imagen


# ### write an dict to to dicline names to code 

# In[21]:


image_dict = {}
#doc = [] # must be dicline but gets overwritten later 

for (name, link)  in zip (picture_name, imagen):

    image_dict.update({name : eval(link)})
    
###image_dict


# ## Create Context to write in word 

# ### create one dict out off multile dicts 

# In[22]:


#dicts = [text_data,names_dict,Tabelle2_dict]
dicts = [text_data,image_dict] 

#context_data = {} #ersetzen

for dict in dicts:
    context_data.update(dict)
    
### context_data


# In[ ]:





# In[23]:


context = context_data


# ### write into word

# In[24]:


doc.render(context)     #render context into document

doc.save(f'§{today}_{objektname}_Sprinkenhof.docx') #save document with new ending count


# In[25]:


#context


# ### Bildvariablen in Excel schreiben 

# In[26]:


picture_name = ['{{' + i + '}}' for i in picture_name]

###picture_name


# In[27]:


pic_vars = pd.DataFrame(picture_name)

###pic_vars.set_index(0)


# In[28]:


sheet = wk.sheets(1) #Öffnen der Excel-Arbeitsmappe 
df = sheet.range('E10').value = pic_vars.set_index(0)

wk.close

