import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

table_header = [
    html.Thead(
        html.Tr([html.Th(""), html.Th("Pf[W]"), html.Th('Qf[VAr]'), html.Th("Sf[VA]"), html.Th("Vl [V]"), html.Th("il[A]"), html.Th("iF[V]")]))
]

row1 = html.Tr([html.Td("bc ="), html.Td(id='p_bc'), html.Td(id='q_bc'), html.Td(id="s_bc"), html.Td(id="vlbc"), html.Td(id="ilbc"), html.Td(id="ifbc")])
row2 = html.Tr([html.Td("ca ="), html.Td(id="p_ca"), html.Td(id="q_ca"), html.Td(id="s_ca"), html.Td(id="vlca"), html.Td(id="ilca"), html.Td(id="ifca")])
row3 = html.Tr([html.Td("ab ="), html.Td(id='p_ab'), html.Td(id="q_ab"), html.Td(id="s_ab"), html.Td(id="vlab"), html.Td(id="ilab"), html.Td(id="ifab")]) 
row4 = html.Tr([html.Td("total ="), html.Td(id='p_total'), html.Td(id="q_total"), html.Td(id="s_total")]) 
table_body = [html.Tbody([row1, row2, row3, row4])]

# external_stylesheets = [dbc.themes.BOOTSTRAP]
layout = html.Div([
    # html.H3("Preencha os inputs!"),
    html.H4('Calculadora de Potencias'),
    dcc.Input(id='input_resistencia', type='text', placeholder='Resistência [Ω]'),
    dcc.Input(id='input_resistencia_indutor', type='text', placeholder='Resistência Indutor [Ω]'),
    dcc.Input(id='input_impedancia', type='text', placeholder='Impedância [mH]'),
    dcc.Input(id='input_tensaoFonte', type='text', placeholder='Tensão da fonte [V]'),
    html.Button(id='submit-button-state', n_clicks=0, children='Calcular'),

    html.H5("Resultado dos cálculos: "),
    dbc.Table(table_header + table_body),
    #Resultados totais
    dcc.Markdown('__Fator de Potencia:__ '),
    html.Table([
        html.Tr([html.Td(id="fp_resultado")])
    ]),
])