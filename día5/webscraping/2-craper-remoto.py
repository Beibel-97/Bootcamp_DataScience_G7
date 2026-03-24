import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

URL = "https://books.toscrape.com/"

response = requests.get(URL)

if response.status_code == 200:
    data = response.content
    soup = BeautifulSoup(response.content,'html.parser')
    books = soup.find_all('article',class_='product_pod')
    print(books[0])
    print(f'total de libros : {len(books)}')
    lista_libros = []
    print(books[0])
    for book in books:
        title = book.find('h3').find('a')['title']
        price = book.find('p',class_='price_color').get_text()
        lista_libros.append([title,price])
        
    print(tabulate(lista_libros,headers=['Titulo','Precio'],tablefmt='grid'))
