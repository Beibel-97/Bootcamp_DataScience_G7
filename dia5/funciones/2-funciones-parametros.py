# PARAMETROS EN FUNCIONES
# Una función puede recibir parámetros para trabajar con datos externos.
# Los parámetros se definen entre los paréntesis de la definición de la función.

def potencia(base,exponente=2):
    return base ** exponente

print(potencia(3)) # Llamada a la función con un parámetro (exponente por defecto)
print(potencia(3,4))  # Llamada a la función con ambos parámetros

def operaciones(a,b):
    suma = a + b
    resta = a - b
    return suma,resta

resultado_suma,resultado_resta = operaciones(5,3)
print(f'suma : {resultado_suma}')
print(f'resta : {resultado_resta}')

# PARAMETROS ARGS Y KWARGS

def sumar_todos(*args):
    print(args)
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

print(sumar_todos(1,2,3))
print(sumar_todos(10,20))

def calculadora(**kwargs):
    print(kwargs)
    if kwargs['operacion'] == 'suma':
        return kwargs['a'] + kwargs['b']
    elif kwargs['operacion'] == 'resta':
        return kwargs['a'] - kwargs['b']
    else:
        return 'operación incorrecta'
    
resultado1 = calculadora(operacion='suma',a=10,b=5)
print(f'resultado 1 : {resultado1}')
resultado2 = calculadora(operacion='resta',a=10,b=5)
print(f'resultado 2 : {resultado2}')