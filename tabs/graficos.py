import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import math
from numpy import *
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

fig = go.Figure()

layout = html.Div([
    dcc.Graph(
        id="graph",
        figure=fig
    ),
    html.Button(id='submit-graphButton', n_clicks=0, children='Atualizar o Grafico'),
])
