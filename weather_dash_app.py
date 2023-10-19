# Importing the libraries

import pandas as pd 
import dash
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
import plotly.express as px
from dash import dash_table
import dash_bootstrap_components as dbc

# reading the data and preparing it for the tables and graphs
df_weather = pd.read_csv('./data/weather.csv')

#creating the bar graph
fig = px.bar(df_weather, 
             x='week-year', 
             y='weekly_avg',  
             color='city',
             barmode='group',
             height=500, width = 1000,
             title = 'Average temperature',)
fig.update_xaxes(tickangle=45)   

graph = dcc.Graph(figure=fig)


#creating the line graph
fig2 = px.line(df_weather, x='week-year', y='weekly_avg', color='city', title = 'Temperature over years',)
fig2.update_xaxes(tickangle=45)
fig2.write_html('weekly_temp.html')
graph2 = dcc.Graph(figure=fig2)


#creating the map
fig3 = px.choropleth(df_weather, locations='alpha-3',
                    projection='natural earth', 
                    width=1100, height=800,
                    animation_frame='week-year',
                    scope='world',
                    color='weekly_avg', locationmode='ISO-3',
                    title = 'Climat in Germany, Italy and USA')
fig3.write_html('map.html')
graph3 = dcc.Graph(figure=fig3)

# Add a dropdown component to the bar graph

dropdown = dcc.Dropdown(['Berlin', 'Rome', 'New York'], "Berlin", clearable=False)

app =dash.Dash()

server = app.server

app.layout = html.Div([html.H1(children = 'Climate in Berlin, Rome and New York', style = {'textAlign': 'center',
                                                                        'color': 'purple'}),
                       html.H2(children = 'Weekly temperature', style = {'paddingLeft':'30px'}),dropdown,graph, graph2, graph3
                      ])


@callback(
    Output(graph,'figure'), 
    Input(dropdown, 'value'))

def update_bar_chart(city): 
    mask = df_weather['city'] == city
    fig =px.bar(df_weather[mask], 
             x='week-year', 
             y='weekly_avg',  
             color='city',
             barmode='group',
             height=600, 
             width=1000,
             title = 'Average temperature')
    fig.update_xaxes(tickangle=45)
    return fig 

if __name__ == '__main__':
    app.run_server()
