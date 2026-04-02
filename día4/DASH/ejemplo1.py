import dash
from dash import dcc,html
from dash import Input,Output


app = dash.Dash(__name__)

@app.callback(
    Output('saludo-output','children'),
    Input('input-nombre','value')
)
def saludar(nombre):
    if nombre:
        return f"Hola {nombre}"
    
    return 'Por favor, escribe tu nombre'


app.layout = html.Div(
    [html.H1("HOLA MUNDO DESDE DASH"),
     dcc.Input(id='input-nombre',type='text',placeholder='Escribe tu nombre'),
     html.Div(id='saludo-output')]
)

if __name__ == '__main__':
    app.run(debug=True)