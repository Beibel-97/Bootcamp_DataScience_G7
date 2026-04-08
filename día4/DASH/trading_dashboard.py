import dash
from dash import Input, Output, State, dcc, html
import pandas as pd
import plotly.express as px
import yfinance as yf


app = dash.Dash(__name__)
server = app.server


def obtener_datos_accion(simbolo: str) -> pd.DataFrame:
    historial = yf.download(
        simbolo,
        period="1mo",
        interval="1d",
        auto_adjust=False,
        progress=False,
    )

    if historial.empty:
        return pd.DataFrame(columns=["Date", "Close"])

    datos_close = historial[["Close"]].reset_index()
    datos_close["Date"] = pd.to_datetime(datos_close["Date"]).dt.date
    return datos_close


app.layout = html.Div(
    [
        html.H1("Dashboard de Precio de Acciones"),
        html.P("Ingresa el simbolo bursatil para consultar el precio de cierre del ultimo mes."),
        html.Div(
            [
                dcc.Input(
                    id="input-simbolo",
                    type="text",
                    value="AAPL",
                    placeholder="Ejemplo: AAPL",
                    debounce=True,
                    style={"width": "220px", "marginRight": "10px", "padding": "8px"},
                ),
                html.Button("Consultar", id="boton-consultar", n_clicks=0),
            ],
            style={"marginBottom": "20px"},
        ),
        html.Div(id="mensaje-estado", style={"marginBottom": "15px", "fontWeight": "bold"}),
        dcc.Graph(id="grafico-accion"),
    ],
    style={"maxWidth": "900px", "margin": "0 auto", "padding": "30px"},
)


@app.callback(
    Output("grafico-accion", "figure"),
    Output("mensaje-estado", "children"),
    Input("boton-consultar", "n_clicks"),
    State("input-simbolo", "value"),
)
def actualizar_grafico(n_clicks, simbolo):
    simbolo = (simbolo or "").strip().upper()

    if not simbolo:
        fig_vacio = px.line(title="Ingresa un simbolo para visualizar la grafica")
        fig_vacio.update_layout(template="plotly_white")
        return fig_vacio, "Escribe un simbolo valido, por ejemplo: MSFT o TSLA."

    try:
        df = obtener_datos_accion(simbolo)
    except Exception as error:
        fig_error = px.line(title="No se pudieron obtener los datos")
        fig_error.update_layout(template="plotly_white")
        return fig_error, f"Error al descargar informacion para {simbolo}: {error}"

    if df.empty:
        fig_sin_datos = px.line(title=f"No hay datos disponibles para {simbolo}")
        fig_sin_datos.update_layout(template="plotly_white")
        return fig_sin_datos, f"No se encontraron precios de cierre para {simbolo} en el ultimo mes."

    fig = px.line(
        df,
        x="Date",
        y="Close",
        markers=True,
        title=f"Precio de cierre de {simbolo} en el ultimo mes",
        labels={"Date": "Fecha", "Close": "Precio de cierre"},
    )
    fig.update_layout(template="plotly_white")

    return fig, f"Mostrando precios de cierre de {simbolo} descargados con yfinance."


if __name__ == "__main__":
    app.run(debug=True)
