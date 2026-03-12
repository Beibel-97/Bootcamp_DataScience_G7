# TUPLAS
# Son inmutables, no se pueden modificar
# Se definen utilizando paréntesis () y los elementos están separados por comas.
dias = ("lunes", "martes", "miércoles", "jueves","viernes")
print(dias)
print(dias[0])
print(dias[1:4])
print(dias[-1])
print(dias[:])
print(type(dias))

#dias.append("sabado") # Esto generará un error porque las tuplas son inmutables

# cuando se deben usar tuplas en vez de listas?
#  - Cuando no se necesita modificar la colección de datos.
#  - Cuando se quiere asegurar que los datos permanezcan constantes.
#  - Cuando se busca optimizar el rendimiento, ya que las tuplas son más rápidas que las listas.

# AGREAR ELEMENTOS A UNA TUPLA
dias = list(dias) # Convertir la tupla a una lista
print(type(dias))
dias.append("sábado") # Agregar un elemento a la lista
dias.append("domingo") # Agregar otro elemento a la lista   
dias = tuple(dias) # Convertir la lista de nuevo a una tupla
print(type(dias))
print(dias)

# RECORRER UNA TUPLA
for dia in dias:
    print(f'Hoy es {dia}')