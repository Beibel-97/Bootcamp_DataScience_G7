# DICCIONARIOS
# Son colecciones desordenadas de elementos que se almacenan en pares clave-valor. 
# Cada clave es única y se utiliza para acceder a su valor correspondiente.
# Se definen utilizando llaves {} y los pares clave-valor se separan por comas.

capitales = {
    "Perú":"Lima",
    "Ecuador":"Quito",
    "Colombia":"Bogotá",
    "Argentina":"Buenos Aires"
}

print(capitales["Ecuador"])


# Agregar o modificar un nuevo par clave-valor
capitales["Bolivia"] = "La Paz"
nueva_capital = {
    "Chile":"Santiago"
}
capitales.update(nueva_capital)
print(capitales)

# eliminar un par clave-valor
del capitales['Argentina']
capitales.pop('Mexico','no existe')
print(capitales)

#buscar un valor
if 'Bolivia' in capitales:
    capitales.pop('Bolivia')
else:
    print('no existe Mexico en capitales')

print(capitales)

# como recorrer un diccionario
print("Recorriendo por claves")
for clave in capitales.keys():
    print(clave)
    
print("Recorriendo por valores")
for valor in capitales.values():
    print(valor)
    
print("recorrer por clave,valor")
for clave,valor in capitales.items():
    print(f"la capital de {clave} es {valor}")