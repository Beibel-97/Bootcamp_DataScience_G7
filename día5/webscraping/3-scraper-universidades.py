import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

URL = 'https://www.universidadperu.com/universidades-peru.php'

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL,headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    main = soup.find('main',id='main-content')
    enlaces = main.find_all('a')
    lista_universidades = []
    for enlace in enlaces:
        universidad_nombre = enlace.get_text()
        universidad_url = enlace.get("href")
        lista_universidades.append([universidad_nombre,universidad_url])
        
    print(tabulate(lista_universidades,headers=['Universidad','URL'],tablefmt='grid'))
else:
    print(f'status code  {response.status_code}')
