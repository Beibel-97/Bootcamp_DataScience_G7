# funciones para maximos minimos y ordenamiento en listas
numeros = [5,3,4,7,2]

print(f"Lista de Números : {numeros}")
#obtener el mayor
mayor = max(numeros)
print(f'El mayor es : {mayor}')

#obtener el menor
menor = min(numeros)
print(f'El menor es : {menor}')

#lista ordenada
lista_ordenada = sorted(numeros)
print(f"lista ordenada : {lista_ordenada}")

#lista ordenada descendente
lista_ordenada_desc = sorted(numeros,reverse=True)
print(f"lista ordenada : {lista_ordenada_desc}")