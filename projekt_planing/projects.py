import xlwings as xw
import glob
import pandas as pd
import os
import plotly.figure_factory as ff
import plotly.express as px
# Importieren Sie die Bibliothek "datetime"
from datetime import datetime, timedelta


#Funktionen um Wochenenden zu skippen
def date_by_adding_business_days(from_date, add_days):
    '''Adds business dates to from_date but doesen't count starting date as Day
    param from_date: starting time
    param add_days: business days to add'''
    business_days_to_add = add_days
    current_date = from_date
    while business_days_to_add > 0:
        current_date += timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5: # sunday = 6
            continue
        business_days_to_add -= 1
    return current_date

os.chdir(r'C:\Users\Jwesterhorstmann\Desktop\Coden\Projektsteuerung')
print (os.getcwd())

start_date = datetime.strptime("2022-12-12", "%Y-%m-%d")

# Excel-Datei einlesen
dataframe = pd.read_excel('beispiel-projekt.xlsx', header=0)

# Fügen Sie die Spalte "Startzeit" zum Dataframe hinzu und initialisieren Sie sie mit Nullen
start_date = datetime.strptime("2022-12-12", "%Y-%m-%d")
dataframe["Startzeit"] = start_date
dataframe["Endzeit"] = start_date

# Iterieren Sie über alle Zeilen im Dataframe
for index, row in dataframe.iterrows():
    # Überprüfen Sie, ob der Vorgang einen Vorgänger hat
    if row["Vorgänger"] == 0:
        # Wenn der Vorgang keinen Vorgänger hat, beginnt er bei Zeitpunkt 0
        start_time = start_date
    else:
        # Andernfalls suchen Sie nach dem Vorgang mit der angegebenen ID und verwenden Sie dessen Endzeit als Startzeit
        predecessor_df = dataframe[dataframe["Id"] == row["Vorgänger"]]

        # Überprüfen Sie, ob der Vorgang gefunden wurde
        if predecessor_df.empty:
            # Wenn der Vorgang nicht gefunden wurde, beginnt der aktuelle Vorgang bei Zeitpunkt Startzeit
            start_time = start_date
        else:
            # Andernfalls verwenden Sie die Endzeit des Vorgangs als Startzeit
            start_time = predecessor_df["Endzeit"].iloc[0]
    
    # Berechnen Sie die Endzeit des Vorgangs als Startzeit plus Dauer
    #end_time = start_time + timedelta(days=(row["Dauer"]))             #Ohne Berücksichtigung von Wochenenden
    end_time = date_by_adding_business_days(start_time, row["Dauer"]-1) #Mit Berücksichtigung von Wochenenden

    
    # Aktualisieren Sie die Start- und Endzeiten des Vorgangs im Dataframe
    dataframe.loc[index, "Startzeit"] = start_time
    dataframe.loc[index, "Endzeit"] = end_time


print (dataframe)

############################################# Umsetzung mit create_gantt() ############################

#dataframe_gant = dataframe.loc[:,["Vorgang", "Startzeit", "Endzeit"]]

# Spaltennamen ändern um die funktion create.gant anwenden zu können
#dataframe_gant = dataframe_gant.rename(columns={"Vorgang": 'Task', "Startzeit": 'Start', "Endzeit" : 'Finish'})

#print (dataframe_gant)

# Erstelle eine leere Liste, um die Dictionarys zu speichern
#dict_list = []

# Iteriere über die Zeilen des DataFrames
#for index, row in dataframe_gant.iterrows():
  # Erstelle ein Dictionary aus der aktuellen Zeile
  #dict_list.append(row.to_dict())

# Drucke die Liste der Dictionarys
#print(dict_list)

#fig = ff.create_gantt(dict_list)

#######################################################################################################


# Erstellen Sie eines Gantt-Diagramm

fig = px.timeline(
    dataframe, 
    x_start="Startzeit", 
    x_end="Endzeit", 
    y="Vorgang",
    color="Vorgang",
)
# Fügen Sie eine Referenzlinie für das aktuelle Datum hinzu
fig.add_vline(x=dataframe.loc[0,"Startzeit"], line_width=3, line_color="green")
fig.add_vline(x=dataframe["Endzeit"].iloc[-1], line_width=3, line_color="green")
fig.add_vline(x=datetime.today(), line_width=3, line_color="red")
fig.update_layout( xaxis_tickformat='%y-%m-%d')
fig.update_xaxes(showgrid=True, showline=True, linewidth=0.1, linecolor='black')
fig.update_yaxes(showticklabels=True, title=None,)
fig['layout']['xaxis'].update({'tickmode': 'linear', 'dtick': 86400000})
#fig.show()



fig.show()




#Umsetzung mit xlwings und berechnetes Start und Enddatum in exel schreiben

#Möglichkeit zur anpassung im Projekt hinzufügen

# mehrere Vorgänger einbauen 
# Mögliche Puffer einbauen

# Meilensteinplan (evtl. Integrieren?)

#Anpassung des Diagramms: Farbliche/übersichtliche Anpassungen, Beschriebung im Balken?!


# Projekt netz plan einbauen ?









# Pfeile um die verknüfungen zu sehen einbauen 

## draw an arrow from the end of the first job to the start of the second job

def draw_arrow_between_jobs(fig, first_job_dict, second_job_dict):
    ## retrieve tick text and tick vals
    job_yaxis_mapping = dict(zip(fig.layout.yaxis.ticktext,fig.layout.yaxis.tickvals))
    jobs_delta = second_job_dict['Start'] - first_job_dict['Finish']
    ## horizontal line segment
    fig.add_shape(
        x0=first_job_dict['Finish'], y0=job_yaxis_mapping[first_job_dict['Task']], 
        x1=first_job_dict['Finish'] + jobs_delta/2, y1=job_yaxis_mapping[first_job_dict['Task']],
        line=dict(color="blue", width=2)
    )
    ## vertical line segment
    fig.add_shape(
        x0=first_job_dict['Finish'] + jobs_delta/2, y0=job_yaxis_mapping[first_job_dict['Task']], 
        x1=first_job_dict['Finish'] + jobs_delta/2, y1=job_yaxis_mapping[second_job_dict['Task']],
        line=dict(color="blue", width=2)
    )
    ## horizontal line segment
    fig.add_shape(
        x0=first_job_dict['Finish'] + jobs_delta/2, y0=job_yaxis_mapping[second_job_dict['Task']], 
        x1=second_job_dict['Start'], y1=job_yaxis_mapping[second_job_dict['Task']],
        line=dict(color="blue", width=2)
    )
    ## draw an arrow
    fig.add_annotation(
        x=second_job_dict['Start'], y=job_yaxis_mapping[second_job_dict['Task']],
        xref="x",yref="y",
        showarrow=True,
        ax=-10,
        ay=0,
        arrowwidth=2,
        arrowcolor="blue",
        arrowhead=2,
    )
    return fig

###fig = draw_arrow_between_jobs(fig, jobB_dict, jobC_dict)