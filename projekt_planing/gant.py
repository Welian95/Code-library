import pandas as pd
import plotly.figure_factory as ff

jobA_dict = dict(Task="Job A", Start=pd.to_datetime('2009-01-01'), Finish=pd.to_datetime('2009-02-28'))
jobB_dict = dict(Task="Job B", Start=pd.to_datetime('2009-03-05'), Finish=pd.to_datetime('2009-04-15'))
jobC_dict = dict(Task="Job C", Start=pd.to_datetime('2009-05-01'), Finish=pd.to_datetime('2009-06-30'))

df = [jobA_dict, jobB_dict, jobC_dict]

print (df)

fig = ff.create_gantt(df)

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

#fig.show()