# LISTAS
# Una lista es una colección ordenada y mutable de elementos.
# Se definen utilizando corchetes [] y los elementos están separados por comas.
dias = ["lunes","martes","miércoles","jueves","viernes"]

#imprimir uno o mas datos
print(dias)
print(dias[0])
print(dias[1:4])
print(dias[-1])
print(dias[:])

#agregar valores a la lista
dias.append("Sábado")
dias.append("Domingo")
print(dias)

#eliminar valores de la lista
dias.pop() # elimina el último elemento de la lista
dias.pop(3)
print(dias)

#modificar un elemento de la lista
dias[3] = "jueves"
dias[4] = "viernes"
print(dias)

#recorrer una lista con bucle for
print(f"total de la lista dias : {len(dias)}")
for contador in range(len(dias)):
    print(f'Hoy es {dias[contador]}')
    
#forma mejorada
for dia in dias:
    print(f'Hoy es {dia}')