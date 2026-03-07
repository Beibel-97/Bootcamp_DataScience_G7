# BUCLE FOR: PERMITE REPETIR SENTENCIAS DE CODIGO UNA DETERMINDA CANTIDAD DE VECES
for contador in range(1,11,1):
    print (contador)

# TABLA DE MULTIPLICAR
# ENTRADA
numero = int(input ("Ingrese la tabla de multiplicar que desea ver : "))

# PROCESO
for contador in range (1,13,1):
    resultado = numero * contador
    print (f"{numero} x {contador} = {resultado}")
    