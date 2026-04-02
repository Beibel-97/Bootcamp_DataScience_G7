import dash
from dash import dcc,html
import pandas as pandas
import plotly.express as px
import seaborn as sns

app = dash.Dash(__name__)

# paso 1 - creamos un dataframe con pandas
df = sns.load_dataset('penguins')

app.layout = html.Div([
    html.H1('Mi primer grafico con Ploty Dash'),
    dcc.Graph(
        figure=px.scatter(df,x='bill_length_mm',
                          y='bill_depth_mm',
                          color='species')
    )
])


if __name__ == '__main__':
    app.run(debug=True)