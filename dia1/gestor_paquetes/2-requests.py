import requests

url = "http://books.toscrape.com"

respuesta = requests.get(url)

print(respuesta.text)