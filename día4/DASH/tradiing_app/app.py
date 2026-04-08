import dash
from dash import Input, Output, State, dcc, html
import pandas as pd
import plotly.express as px
import yfinance as yf

import os
os.environ['TZ'] = 'America/New_York'

# Use pytz to provide the timezone

def obtener_precios_cierre(simbolo: str) -> pd.DataFrame:
    simbolo = simbolo.strip().upper()
    datos = yf.download(simbolo, period="1mo", progress=False, auto_adjust=False)

    if datos.empty:
        return pd.DataFrame()

    if isinstance(datos.columns, pd.MultiIndex):
        datos.columns = datos.columns.get_level_values(0)

    precios = datos[["Close"]].dropna().reset_index()
    precios["Variacion"] = precios["Close"] - precios["Close"].iloc[0]

    return precios


def figura_vacia(mensaje: str):
    fig = px.line(title=mensaje)
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    fig.update_layout(
        template="plotly_white",
        annotations=[
            {
                "text": mensaje,
                "xref": "paper",
                "yref": "paper",
                "x": 0.5,
                "y": 0.5,
                "showarrow": False,
                "font": {"size": 18},
            }
        ],
    )
    return fig


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Dashboard de Precio de Acciones"),
        html.P("Ingresa el símbolo bursátil para consultar el precio de cierre del último mes."),
        html.Div(
            [
                dcc.Input(
                    id="input-simbolo",
                    type="text",
                    value="AAPL",
                    placeholder="Ejemplo: AAPL, MSFT, TSLA",
                    debounce=True,
                    style={"width": "240px", "marginRight": "12px"},
                ),
                html.Button("Buscar", id="boton-buscar", n_clicks=0),
            ],
            style={"marginBottom": "20px"},
        ),
        html.Div(id="mensaje-estado", style={"marginBottom": "12px", "fontWeight": "bold"}),
        dcc.Graph(id="grafico-accion", figure=figura_vacia("Ingresa un símbolo para consultar datos")),
    ],
    style={"maxWidth": "1000px", "margin": "0 auto", "padding": "24px"},
)


@app.callback(
    Output("grafico-accion", "figure"),
    Output("mensaje-estado", "children"),
    Input("boton-buscar", "n_clicks"),
    State("input-simbolo", "value"),
)
def actualizar_grafico(_, simbolo):
    if not simbolo or not simbolo.strip():
        return figura_vacia("Ingresa un símbolo válido"), "Debes ingresar un símbolo bursátil."

    simbolo = simbolo.strip().upper()
    precios = obtener_precios_cierre(simbolo)

    if precios.empty:
        return (
            figura_vacia(f"No se encontraron datos para {simbolo}"),
            f"No se encontraron precios de cierre para {simbolo} en el último mes.",
        )

    variacion_total = precios["Close"].iloc[-1] - precios["Close"].iloc[0]
    variacion_pct = (variacion_total / precios["Close"].iloc[0]) * 100

    fig = px.line(
        precios,
        x="Date",
        y="Close",
        markers=True,
        title=f"Precio de cierre de {simbolo} en el último mes",
        labels={"Date": "Fecha", "Close": "Precio de cierre"},
    )
    fig.update_layout(template="plotly_white")

    mensaje = (
        f"Último cierre: {precios['Close'].iloc[-1]:.2f} USD | "
        f"Variación del mes: {variacion_total:+.2f} USD ({variacion_pct:+.2f}%)"
    )

    return fig, mensaje


if __name__ == "__main__":
    app.run(debug=True)