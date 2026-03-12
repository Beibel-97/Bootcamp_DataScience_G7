# FUNCIONES EN PYTHON
# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Se define utilizando la palabra clave 'def', seguida del nombre de la función y paréntesis.
def saludar(nombre):
    #return f"Hola {nombre}"
    print(f"Hola {nombre}")


nombre_usuario = input("Hola ¿Cómo te llamas? ")
#print(saludar(nombre_usuario))
saludar(nombre_usuario)

def sumar(a,b):
    return a + b

resultado = sumar(5,3)
print(f'la suma es {resultado}')