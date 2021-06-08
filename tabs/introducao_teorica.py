from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Caption import Caption
from dash_html_components.Div import Div
from dash_html_components.Figcaption import Figcaption
from dash_html_components.Figure import Figure

layout = html.Div([
    dcc.Markdown('''
    Ao estudar a energia elétrica em corrente alternada nos dias atuais deve-se saber que desde o momento em que ela é gerada, até a sua distribuição, o sistema trifásico é o sistema padrão. Além de seus geradores oferecerem um maior aproveitamento de espaço, os motores trifásicos possuem maior rendimento, melhor fator de potência e capacidade de sobrecarga quando comparados aos motores monofásicos.
    
   Quando as tensões senoidais de um circuito têm a mesma magnitude, a mesma frequência e são defasadas em 120°, pode-se dizer que o circuito trifásico encontra-se em equilíbrio. Além disso, as correntes também devem estar em equilíbrio. As cargas trifásicas em equilíbrio podem estar configuradas tanto no modo estrela (Y), quanto no modo triângulo (▲).
   
    A ligação trifásica em estrela ocorre quando conecta-se um dos terminais das cargas a um ponto neutro e o outro terminal é conectado a uma das fases do sistema. Utiliza-se o ponto comum para realizar a medição das tensões de fase. Na figura abaixo encontra-se um esquema que representa o modo em estrela: 
    '''),
    html.Figure([
        html.Img(src='assets/LigacaoEstrela.png'),
        html.Figcaption("Figura 1: Representação esquemática da ligação estrela"),
    ]),
    dcc.Markdown('''
    O esquema representado na Figura 1 permite que sejam obtidas as relações entre as tensões de fase e linha:
        '''),
    html.Img(src='assets/Formula1.png'),
    dcc.Markdown('''
    Onde:

    VL: tensão de fase;

    VF: tensão de linha.
    '''),
    dcc.Markdown('''
    Sabendo que a figura 1 corresponde a um esquema em série, é possível afirmar  que as correntes de linha (IL) e de fase (IF) são iguais. Sendo assim, as potências obedecem as seguintes relações:
    '''),
    html.Img(src='assets/Formula2.png'),
    dcc.Markdown('''Quando deseja-se relacionar as tensões de fase, encontramos as seguintes relações de potência:
    '''),
    html.Img(src='assets/Formula3.png'),
    dcc.Markdown(''' 
    O segundo tipo de ligação trifásica equilibrada ocorre quando a carga elétrica forma um triângulo que possui, em cada um dos seus vértices, ligações com os condutores de fase do sistema. A ligação trifásica em triângulo pode ser representada pela figura a seguir:
    '''),
    html.Figure([
        html.Img(src='assets/LigacaoTriangulo.png'),
        html.Figcaption("Figura 2: Representação esquemática da ligação triângulo"),
    ]),
    dcc.Markdown(''' 
    Neste tipo de configuração, as correntes de linha e fase estão relacionadas de acordo com a fórmula a seguir:
    '''),
    html.Img(src='assets/Formula4.png'),
    dcc.Markdown(''' As relações de potência ativa, reativa e aparente apresentadas para o esquema do tipo estrela continuam válidas neste caso.''')

])