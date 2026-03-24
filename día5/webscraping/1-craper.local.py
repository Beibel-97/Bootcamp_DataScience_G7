from bs4 import BeautifulSoup
from tabulate import tabulate

with open('ejemplo_pagina.html','r',encoding='utf-8') as f:
    html = f.read()
    
#print(html)
soup = BeautifulSoup(html,"html.parser")
titulo = soup.find("h1").text
print(f"titulo : {titulo}")

productos = soup.find_all("div",class_="producto")
lista_productos = []
for producto in productos:
    nombre = producto.find("h2",class_="nombre").text
    precio = producto.find("p",class_="precio").text
    stock = producto.find("p",class_="stock").text
    lista_productos.append([nombre,precio,stock])
    
headers = ['Nombre', 'Precio', 'Stock']
print(tabulate(lista_productos, headers=headers, tablefmt='grid'))