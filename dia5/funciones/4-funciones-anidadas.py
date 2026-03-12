# FUNCIONES ANIDADAS
# Las funciones anidadas son funciones definidas dentro de otras funciones.

def operaciones(a,b):
    def suma(a,b):
        return a + b
    def resta(a,b):
        return a - b
    def multiplicacion(a,b):
        return a * b
    def division(a,b):
        return a / b
    
    print(f"suma : {suma(a,b)}")
    print(f"resta : {resta(a,b)}")
    print(f"multiplicación : {multiplicacion(a,b)}")
    print(f"división : {division(a,b)}")
    
operaciones(10,5)

# FUNCIONES RECURSIVAS
# Una función recursiva es una función que se llama a sí misma para resolver un problema.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(f"Factorial de 5 : {factorial(5)}")

# FUNCIONES COMO PARAMETRO DE OTRA FUNCIÓN
def aplicar_funcion(func, valor):
    return func(valor)

doblar = lambda x: x * 2
resultado = aplicar_funcion(doblar,5)
print(f'resultado de aplicar funcion {resultado}')