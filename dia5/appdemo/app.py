from transformers import pipeline
import gradio as gr

pipe = pipeline("text-classification", model="cesarcodigo/modelo_sentimiento_peruano")

def analisis_sentimiento(texto):
  resultado = pipe(texto)[0]
  label = resultado['label']
  score = resultado['score']

  if label == 'positive':
    label = 'Positivo'
  else:
    label = 'Negativo'

  return f'Tú comentario  es {label} (score : {round(score, 4)})'

demo = gr.Interface(
    fn=analisis_sentimiento,
    inputs=gr.Textbox(label='coloca tu comentario'),
    outputs=gr.Textbox(label='Resultado')
)
demo.launch()