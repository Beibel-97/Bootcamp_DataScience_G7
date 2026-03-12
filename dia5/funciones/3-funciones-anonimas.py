#FUNCIONES ANONIMAS
#Son funciones que no tienen un nombre asociado
#Se definen con la palabra reservada lambda

def sumar(a, b):
    return a + b

sumar2 = lambda a,b: a + b
print(sumar(2,3))
print(sumar2(2,3))

multiplicar = lambda a, b: a * b
print(multiplicar(2, 3))


division = lambda a,b: a / b if b!= 0 else "No se puede dividir por cero"
print(division(6,2))
print(division(6,0))