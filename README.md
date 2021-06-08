### *Dash is an amazing framework for building ML and DataScience web apps*.

![Screenshot_1](https://user-images.githubusercontent.com/71408872/121252074-f6ae0900-c87d-11eb-8725-a32fc5c10f3f.png)


<p>This project was created by me to help some friends that needed to present their study in an interactive way, with the possibility of someone try random inputs and see visually what that means after the formulas they explain on the site.
</p>

# 📚 Contents

- [App Samples](#app-samples)
- [Tips](#tips)
    - [Callbacks on Dash](#callbacks-on-dash)
    - [Ploting graphs with Plotly Express](#ploting-graphs-with-plotly-express)
    - [Deploying dash apps on heroku](#deploying-dash-apps-on-heroku)
- [Getting started](#getting-started)

## App samples
| App | Description |
| --- | :---: |
|![Multipages](https://user-images.githubusercontent.com/71408872/121244773-aa5ecb00-c875-11eb-9ec7-ecda4f080716.gif) | This is how the multipages work. You can switch between tabs and the site will render content depending on which tab you are in.|
|![Calculator](https://user-images.githubusercontent.com/71408872/121244676-8ac7a280-c875-11eb-8926-1211d59610bb.gif) | This part is the "Calculator" tab, where with 4 inputs the site renders a table filled with results somewhat complicated to get by hand. God bless Numpy.|
|![Graphs](https://user-images.githubusercontent.com/71408872/121244828-b9de1400-c875-11eb-850e-21261154c4fc.gif) | Here you can see the Graph changing it's output depending of the results of the table I said before. Because of some physical aspects the trace V1 is always shaped in a similar way, but that is not on me. .|

# 💡 Tips
<p> This was my first try using Dash and even though the documentation is pretty good, I had some troubles and I want to make sure that you (or me in the future) don't stumble there again
</p>

## Callbacks on Dash
<p>The callbacks will always have this structure:</p>

```py
@app.callback(
              Output('id_of_the_output_Element', 'property_that_will_change'),
              Input('id_of_the_input_Element', 'property_that_wil_be_stored')

def function_Dat_Update_Output(input_value): #args can have name but always represent the property_that_wil_be_stored 
		if "blabla" == "blabla":
				return input_value + 3 #now the property_that_will_change have this value
```
There is no flexibility to this, you need to get the Output first, Input second and the function that update stuff immediately after. Remember you `don't` call the function, you just define them.<p>
<p>
There lots of ways to work with this, like multiple outputs with just one input, chained callbacks or even states (that I used on the table part), but that is very well explained here: <a href="https://dash.plotly.com/basic-callbacks">Basic Dash Callbacks</a>
</p>

<p>For pratical purposes here is a sample of the code from the tabs, where I used callbacks: <p>

```py

app.layout = html.Div(
children=[
		dcc.Tabs(id="tabs-styled-with-inline", className='custom-tabs-container', children=[
        dcc.Tab(label="Apresentação", value="tab-apresentacao", style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Introdução Teórica", value="tab-introducao_teorica", style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Cálculos', value='tab-calculos', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Gráficos', value='tab-graficos',style=tab_style, selected_style=tab_selected_style),
        ], style=tabs_styles),
    html.Div(id='tabs-content-inline'),
    dcc.Store(id='intermediate-value', storage_type='session'),
])

@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-styled-with-inline', 'value'))  

def render_content(tab):
    if tab == "tab-calculos":  return calculos.layout, #Depending of the tab Im in return different things, NOICE
    elif tab == "tab-apresentacao": return apresentacao.layout,
    elif tab == 'tab-introducao_teorica': return introducao_teorica.layout
    elif tab == 'tab-graficos': return graficos.layouts
```

## Plotting graphs with Plotly express
<p>Because the Function that produce the graph data was so large, I have to put it inside a separeted page. And with that Dash is amazingly pratical. You just have to make sure that the .py file containing your fuction and the deploy.py are both in the same directory.
</p>
<p> ![Untitled](https://user-images.githubusercontent.com/71408872/121246379-7b495900-c877-11eb-95a1-4460adc0b10d.jpg)</p>

With everybody on the same place we just need to import

```py
from updateGraph import grafico_calculos #the name of the function inside updateGraph
```

<p>Now to make the graph visually apear you need to create a dcc.graph somewhere and change the "figure" property with the use of callbacks. The syntax part to plot graphs is much better explained on <a href="https://plotly.com/python/plotly-express/">Plotly Express</a>. 
But for pratical purposes I will show how to make a simple line going up

```py
@app.callback(Output('graph', 'figure'),
            Input('inputsGraph', 'data'))

def update_graph(inputsGraph):

	  x_content = [1, 2, 3, 4]
		y_content = [1, 2, 3, 4] #If x go higher y go higher, BOOM there is a line going up
		
    fig = go.Figure(go.Scatter()) 
		# Fig is the thing we gonna return to fullfill the figure property of ours dcc.graph Element

    fig.add_trace(go.Scatter(x=x, y=v, mode='lines', name='Line going Up baby'))
   
    fig.update_layout(
        xaxis_title="This is the X Axis",
        yaxis_title="This is the Y Axis"
    )

    return fig 
```

## Deploying dash apps with heroku
<p>This is part is very straight forward because there is not much different ways to do (I think), but you need to get every step right or the deploy display much more errors that you can handle.
</p>
So the step by step guide is:

* Intiate a git repo: git init
* Write a .gitignore file on your current directory with  

```py
venv
*.pyc
.env
.DS_Store
```
Maybe you need to ignore more things but that worked fine for me. And remember the .gitignore files `DOES NOT` have a file extension, I messed up with this some times.

* Create the Procfile. archive with the content below, and notice it doesn't have an extension too

```py
web: gunicorn deploy:server
```
Deploy is the name of the file your program is inside. You can change this name but not the typing structure.One space more or less and the heroku will not understand. At leas for me was like that.

* Write on the terminal
```py
pip freeze > requirements.txt 
# this create a requirements.txt file with all the
# librarys heroku server will need to install
```
* Now you just have to setup your git to connect with heroku. Follow the lines below

```bash 
> heroku login #press any key except q and do the login
> git add .
> git commit -m "Commited yay"
> heroku create -n mywebapp
> heroku git:remote -a mywebapp
> git push heroku master #This part can take several minutes
> heroku ps:scale web=1 #your app is already deployd but this make sure will be only one runnig around
> heroku open # :D
```

# Getting Started

```bash
# CLone repository
git clone https://github.com/Mesheo/Circuitos-Trifasicos.git && cd Circuitos-Trifasicos

#Install Dependencies
pip install {whatever that is underscore on the imports}

#Run Aplication
python deploy.py
```
Go to http://127.0.0.1:8050/ to see the application running