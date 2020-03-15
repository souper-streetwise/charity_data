import plotly.graph_objs as go
import sqlite3
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go


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
all_charities = df.index

# create a dictionary for the dropdown containing all the charity names
charity_options = []
for i in all_charities:
    charity_options.append({'label':i,'value':i})

# Launch the application:
app = dash.Dash()


# Create a Dash layout that contains a dropdown with multiple items and a Graph component:
app.layout = html.Div([
    html.H1('Charity Data Dashboard', style = {'text-align': 'center', 'font-size':'50px', 'font-weight': 'lighter'}),
    html.Div('Select charities:', style = {'font-size':'20px'}),    
    dcc.Dropdown(id='charity-input',options=charity_options,value=all_charities, multi = True),
    dcc.Graph(id='graph')
], style = {'font-family': 'Gill Sans'})


# Call back to take in the values from the dropdown and use to update the graph
@app.callback(Output('graph', 'figure'),
              [Input('charity-input', 'value')])
def update_figure(selected_charities):
    # x data is the charities selected in the dropdown, y data is the corresponding number of interactions 
    # for these charities
    x_data = selected_charities
    y_data = df.loc[selected_charities]['Interactions']
    # make the data list for a bar plot using the x and y data and set the layout parameters.
    # These are returned to update the bar plot
    return {
        'data': [go.Bar(x=x_data, y=y_data)],
        'layout': go.Layout(
            xaxis={'title': 'Charity'},
            yaxis={'title': 'Number of Interactions'},
            hovermode='closest'
        )
    }


# Add the server clause:

if __name__ == '__main__':
    app.run_server()
