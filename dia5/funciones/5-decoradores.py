def saludar():
    print("Hola estudiante")

def ejecutar(funcion):
    funcion()

ejecutar(saludar)


import time

def medir_tiempo(funcion):

    def wrapper():

        inicio = time.time()

        funcion()

        fin = time.time()

        print("Tiempo:", fin - inicio)

    return wrapper

@medir_tiempo
def proceso_lento():
    print('inicio')
    for i in range(100000):
        pass
    print('termino')
    
@medir_tiempo
def saludar_2():
    print("Hola estudiante")
    
proceso_lento()
saludar_2()

def formato_asteriscos(funcion):

    def mifuncioninterna():
        print("*"*50)
        funcion()
        print("*"*50)

    return mifuncioninterna

@formato_asteriscos
def mostrar_mensaje():
    print("Titulo de mi programa")
    

mostrar_mensaje()
