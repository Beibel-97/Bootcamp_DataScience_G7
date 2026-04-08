import dash
from dash import dcc,html
import pandas as pandas
import plotly.express as px
import seaborn as sns

from dash.dependencies import Input, Output

df = sns.load_dataset("penguins")

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1('DASHBOARD CON VARIOS GRAFICOS'),
    html.Div([
        html.P("Selecciona la especie de pingüino:"),
        dcc.Dropdown(
            id='dropdown-especie',
            options=[
                {'label': especie, 'value': especie} for especie in df['species'].unique()
            ],
            value=df['species'].unique().tolist(),
            clearable=False,
        )
        ],style={'width': '30%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(
                id='grafico-dispersion'
            ),
            dcc.Graph(
                id='grafico-boxplot'
            )
        ])
    ])

@app.callback(
    Output('grafico-dispersion', 'figure'),
    Output('grafico-boxplot', 'figure'),
    Input('dropdown-especie', 'value')
)
def actualizar_grafico(especies_seleccionadas):
    if not isinstance(especies_seleccionadas, list):
        especies_seleccionadas = [especies_seleccionadas]
        
    df_filtrado = df[df['species'].isin(especies_seleccionadas)]
    
    fig1 = px.scatter(
        df_filtrado,
        x='bill_length_mm',
        y='bill_depth_mm',
        color='species',
        title='Relación entre largo y profundidad del pico de los pingüinos'
    )
    
    fig2 = px.box(
        df_filtrado,
        x='sex',
        y='body_mass_g',
        title='Distribución del peso corporal por sexo'
    )
    
    return fig1,fig2
    
if __name__ == '__main__':
    app.run(debug=True)