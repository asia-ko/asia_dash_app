import pandas as pd 
import dash
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
import plotly.express as px
from dash import dash_table


diabetes_train = pd.read_csv('./data/diabetes_train.csv')

fig = px.scatter_3d(diabetes_train, x='HbA1c_level', y='diabetes', z='blood_glucose_level',
              color='HbA1c_level',
                   size_max=40,
                   opacity=0.7)

fig.update_layout(margin=dict(l=1, r=1, b=1, t=1))

fig.write_html('diabetes.html')

graph = dcc.Graph(figure=fig)

app =dash.Dash()

server = app.server

app.layout = html.Div(html.H1(children = 'Logistic regression model'), graph)


if __name__ == '__main__':
    app.run_server()
