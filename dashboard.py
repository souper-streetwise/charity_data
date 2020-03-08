import plotly.offline as pyo
import plotly.graph_objs as go
import sqlite3
import pandas as pd

# connect to the database and make a query to retrieve the number of rows for each charity
conn = sqlite3.connect('/Users/Charlotte/Documents/Code/Bristol_homeless_hackathon/web_app/charity_app/db.sqlite3')

query = '''SELECT Charity, COUNT(1) AS Interactions
    FROM record_record
    GROUP BY Charity
    '''

# submit query and read data into a dataframe. Make the index the charity and the column is the number of entries 
# for that charity
df = pd.read_sql_query(query, conn)
df.set_index('charity', inplace=True)

# set the data and layout variables then plot a bar plot of the number of interactions for each charity.

data = go.Bar(x=df.index, y=df['Interactions'])
layout = go.Layout(title = 'Charity Interactions', yaxis_title='Interactions', xaxis_title='Charity')
fig = go.Figure(data=data, layout=layout)

# save the html file for the figure
pyo.plot(fig, filename='charity_interactions_bar_chart.html')