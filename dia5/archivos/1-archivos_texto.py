# MANEJO DE ARCHIVOS DE TEXTO
# ESCRIBIR UN ARCHIVO TXT
# PERMISOS
# W - ESCRITURA
with open('notas.txt','w') as archivo:
    archivo.write("Hola mundo en mi archivo")
    archivo.write("\n")
    archivo.write("Esta es un clase de Python")
    
#LEER UN ARCHIVO
#PERMISO R - READ

with open('notas.txt','r') as archivo:
    contenido = archivo.read()
    print(contenido)
    
print("----- linea por linea -----")
# LEER CONTENIDO LINEA POR LINEA
with open('notas.txt','r') as archivo:
    for linea in archivo:
        print("linea : ",linea.strip())  # Usar strip() para eliminar saltos de línea adicionales
    
# AÑADIR CONTENIDO A UN ARCHIVO TXT
# PERMISO A . APPEND
with open('notas.txt','a') as archivo:
    nueva_linea = input('Escribe una nueva linea : ')
    archivo.write("\n")
    archivo.write(nueva_linea)