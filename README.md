### *Dash is an amazing framework for building ML and DataScience web apps*.

<p>This project was created by me to help some friends that needed to presentate their study in an interative way, with the possibility of someone try random inputs and see visually what that means after the formulas they explain on the site.
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
|![Multipages](https://user-images.githubusercontent.com/71408872/121244773-aa5ecb00-c875-11eb-9ec7-ecda4f080716.gif) | This is how the multipages work. You can switch between tabs and the site will render content depending on which tab you are.|
|![Calculator](https://user-images.githubusercontent.com/71408872/121244676-8ac7a280-c875-11eb-8926-1211d59610bb.gif) | This part is the "Calculator" tab, where with 4 inputs the site renders a table fullfilled with results kinda complicated to get by hand. God bless Numpy.|
|![Graphs](https://user-images.githubusercontent.com/71408872/121244828-b9de1400-c875-11eb-850e-21261154c4fc.gif) | Here you can see the Graph changing his output depending of the results of the table I said before. Because physics the trace V1 always shape in a similar way, but that is not on me. .|

# 💡 Tips
<p> This was my first try using Dash and even tho the documentation is pretty good, I found some troubles and I want to make sure that you (or me in the future) dont stumble there again
</p>

### Callbacks on Dash
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
There lots of ways to work with this, like multiple outputs with just one input, chained callbacks or even states (that i used on the table part) but that is very well explained here: <a href="https://dash.plotly.com/basic-callbacks">Basic Dash Callbacks</a>
</p>