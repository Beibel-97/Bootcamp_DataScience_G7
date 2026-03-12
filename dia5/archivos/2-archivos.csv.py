"""
ARCHIVOS CSV
Un **archivo CSV (Comma Separated Values)** es un tipo de archivo de texto 
utilizado para **almacenar datos estructurados en forma de tabla**.  

En este formato, cada **línea del archivo representa una fila de datos**, 
y los **valores dentro de esa fila están separados por un delimitador**, 
generalmente una **coma (,)**

Los archivos CSV son muy utilizados para 
**intercambiar datos entre diferentes programas**, como:
- Excel
- Google Sheets
- Bases de datos
- Aplicaciones de análisis de datos
"""
import csv

with open('alumnos.csv','w',newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['dni','Nombre','Email'])
    escritor.writerow(['45454545','Jose Perez','jperez@gmail.com'])
    
# leer un archivo csv
with open('alumnos.csv','r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print('--------------')
        for campo in fila:
            print(campo)