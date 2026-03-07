"""
Ejercicio: Lista de números

Escribe un programa en Python que realice las siguientes tareas:

1. Solicite al usuario ingresar 5 números enteros.
2. Guarde cada número en una lista.
3. Una vez ingresados todos los números, el programa debe:

   - Mostrar la lista de números ingresados.
   - Mostrar cuál es el número mayor.
   - Mostrar cuál es el número menor.
   - Mostrar la lista ordenada de mayor a menor.
"""
numeros = []
for i in range(5):
    num = int(input(f"Ingrese nro {i + 1} : "))
    numeros.append(num)
    
#Mostrar la lista de números ingresados.
print(f"Lista ingresada : {numeros}")

#Mostrar cuál es el número mayor.
# [5,3,4,7,2]
mayor = max(numeros)
        
print(f'el mayor es {mayor}')
menor = min(numeros)
#Mostrar cuál es el número menor.        
print(f'el menor es {menor}')

#Mostrar la lista ordenada de mayor a menor.
numeros = sorted(numeros,reverse=True)
print("Lista ordenada:", numeros)