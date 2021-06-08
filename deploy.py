import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import math
from numpy import *
from tabs import calculos, apresentacao, introducao_teorica, graficos
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os
from updateGraph import grafico_calculos
from dash.exceptions import PreventUpdate

def fasor(numero, angulo):
    fasor = numero*exp(1j*deg2rad(angulo))
    return fasor

def calcular_xl(l):
    xl = (l * 2 * math.pi * 60)
    return xl

def calcularReal(n):
    real = round(n.real, 3)
    imag = round(n.imag, 3)
    resultado = math.sqrt((real**2)+(imag**2))
    return resultado

# Define variable
myheading = 'Fase I - Trabalho Experimental de Circuitos 2 UFU'
apptitle = "Circuitos Trifasicos Equilibrados"
moodle_address = 'http://www.ufu.br/tags/moodle'

# Initiate app
# port = int(os.environ.get('PORT', 5000))
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)
app.title=apptitle
server = app.server

tabs_styles = {
    'height': '50px',  
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'textAlign': 'center',
    'alignItems': 'center',
    'justifyContent': 'center',
    'display':'flex'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px',
    'textAlign': 'center',
    'alignItems': 'center',
    'justifyContent': 'center',
    'display':'flex'
}



# Setando os elementos da pag principal
app.layout = html.Div( 
children=[
    html.H1(
        myheading, 
        style={
            'textAlign': 'center',
            'color': 'black',
            'fontFamily': 'bold'
    }),
    dcc.Tabs(id="tabs-styled-with-inline", className='custom-tabs-container', children=[
            dcc.Tab(label="Apresentação", value="tab-apresentacao", style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label="Introdução Teórica", value="tab-introducao_teorica", style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Cálculos', value='tab-calculos', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Gráficos', value='tab-graficos',style=tab_style, selected_style=tab_selected_style),
        ], style=tabs_styles),
    html.Div(id='tabs-content-inline'),
    dcc.Store(id='intermediate-value', storage_type='session'),
])

#callback das abas
@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-styled-with-inline', 'value'))  

def render_content(tab):
    if tab == "tab-calculos":  return calculos.layout,
    elif tab == "tab-apresentacao": return apresentacao.layout,
    elif tab == 'tab-introducao_teorica': return introducao_teorica.layout
    elif tab == 'tab-graficos': return graficos.layout

#callback da calculadora
try:
    @app.callback(
              Output('p_bc', 'children'),
              Output('p_ca', 'children'),
              Output('p_ab', 'children'),
              Output('p_total', 'children'),
              Output('q_bc', 'children'),
              Output('q_ca', 'children'),
              Output('q_ab', 'children'),
              Output('q_total', 'children'),
              Output('s_bc', 'children'),
              Output('s_ca', 'children'),
              Output('s_ab', 'children'),
              Output('s_total', 'children'),
              Output('fp_resultado', 'children'),
              Output('vlbc', 'children'),
              Output('vlca', 'children'),
              Output('vlab', 'children'),
              Output('ilbc', 'children'),
              Output('ilca', 'children'),
              Output('ilab', 'children'),
              Output('ifbc', 'children'),
              Output('ifca', 'children'),
              Output('ifab', 'children'),
              Output('intermediate-value', 'data'),
              Input('submit-button-state', 'n_clicks'),
              State('input_resistencia', 'value'),
              State('input_resistencia_indutor', 'value'),
              State('input_impedancia', 'value'),
              State('input_tensaoFonte', 'value'))

    def update_output(n_clicks, input_resistencia, input_resistencia_indutor, input_impedancia, input_tensaoFonte):
        if input_resistencia is None:
            raise PreventUpdate
        try:
            inputsGrafico = [0, 0, 0]
            print('')
            print('\n ____Try block____')

            r = float(input_resistencia)
            rl = float(input_resistencia_indutor)
            l = float(input_impedancia)/1000
            v = float(input_tensaoFonte)

            print(f' r : {r}\n rl : {rl}\n l : {l}\n v : {v}')

            # Calculo das tres tensoes fonte
            vbc = v*exp(1j*deg2rad(120))
            vca = v*exp(1j*deg2rad(0))
            vab = v*exp(1j*deg2rad(-120))

            # Calculo do xl
            xl = calcular_xl(l)

            # Calculo do z retangular
            z = complex((r+rl), round(xl,3))

            # Calculo das correntes de linha forma retangular
            ilabRet = vab/z
            ilbcRet = vbc/z
            ilcaRet = vca/z

            # Calculo das correntes de linha forma real
            ilab = round(calcularReal(ilabRet),3)
            ilbc = round(calcularReal(ilbcRet), 3)
            ilca = round(calcularReal(ilcaRet), 3)

            # Calculo das correntes de fase usando o real de qualquer IL
            iFab = round((ilab/math.sqrt(3)),3)
            iFbc = round((ilbc/math.sqrt(3)),3)
            iFca = round((ilca/math.sqrt(3)),3)

            '''Calculo da tensao de linha
            Aqui usamos o valor retangular'''

            vlbc = round(calcularReal(z * ilbc), 2)
            vlca = round(calcularReal(z * ilca), 2)
            vlab = round(calcularReal(z * ilab), 2)
            
            #armazenando os inputs do grafico fora da funcao
            inputsGrafico[0] = (vlab)
            inputsGrafico[1] = (ilab)
            inputsGrafico[2] = (iFab)

            #Calculos do S
            s_bc = round(((math.sqrt(3))*float(vlbc)*ilbc), 3)
            s_ca = round(((math.sqrt(3))*float(vlca)*ilca), 3)
            s_ab = round(((math.sqrt(3))*float(vlab)*ilab), 3) 
            s_total = s_bc + s_ca + s_ab

           
            #Calculos do P
            p_bc = round(s_bc * math.cos(120), 3)
            p_ca = round(s_ca * math.cos(0), 3)
            p_ab = round(s_ab * math.cos(-120), 3)
            p_total = round((p_bc + p_ca + p_ab), 3)


            #Calculos do Q
            q_bc = round(s_bc * math.sin(120), 3)
            q_ca = round(s_ca * math.sin(0), 3)
            q_ab = round(s_ab * math.sin(-120), 3)
            q_total = round((q_bc + q_ca + q_ab), 3)

            #Calculo do FP
            fp = p_total/s_total
            print(
                f'<<<<<<RESULTADOS>>>>>\nvbc = {vbc}\nvca = {vca}\nvab = {vab}\n\nxl = {xl}\nz = {z}\n\nilab = {ilab}\nilbc = {ilbc}\nilca = {ilca} \nIFab = {iFab}\nIFbc = {iFbc}\niFca = {iFca}')
            print(f'\nTensoes de linha!\nvlbc = {vlbc}\nvlca = {vlca}\nvlab = {vlab}')
            print(
                f'\n<<<<<POTENCIAS>>>>>\nS bc= {s_bc} \nS ca={s_ca} \nS ab={s_ab}\nS total = {s_total}')
            print("-*" * 10)
            print(f'P bc = {p_bc}\nP ca = {p_ca}\nP ab = {p_ab}\nP total = {p_total}')
            print("*-" * 10)
            print(f'Q bc = {q_bc}\nQ ca = {q_ca}\nQ ab = {q_ab}\nQ total = {q_total}')
            
            print(f'\n INPUTS DO GRAFICO>>>> {inputsGrafico}')
            return p_bc, p_ca, p_ab, p_total, q_bc, q_ca, q_ab, q_total, s_bc, s_ca, s_ab, s_total, fp, vlbc, vlca, vlab, ilbc, ilca, ilab, iFbc, iFca, iFab, inputsGrafico

        except TypeError:
            print(
                f"calcular com {type(input_resistencia)} e {type(input_resistencia_indutor)} e {type(input_impedancia)} e {type(input_tensaoFonte)} eh foda")
            return 0
except:
    print('estamos numa aba sem calculadora')

# callback do grafico
@app.callback(Output('graph', 'figure'),
            Input('intermediate-value', 'data'))

def update_graph(inputsGrafico):

    print(f'\n INPUTS DO GRAFICO NO GRAFICO = {inputsGrafico}\n')

    #descompactando
    v1, v2, v3, t = grafico_calculos(inputsGrafico[0], inputsGrafico[1], inputsGrafico[2])

    fig = go.Figure(go.Scatter())

    fig.add_trace(go.Scatter(x=t, y=v1, mode='lines', name='v1'))
    fig.add_trace(go.Scatter(x=t, y=v2, mode='lines', name='v2'))
    fig.add_trace(go.Scatter(x=t, y=v3, mode='lines', name='v3'))

    fig.update_layout(
        xaxis_title='Tempo [segundos]',
        yaxis_title="Tensão [Volts]"
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)