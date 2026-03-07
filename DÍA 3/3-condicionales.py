# CALCULADORA
# CREAR UN PROGRMA QUE PERMITA SUMAR, RESTAR, MULTIPLICAR O DIVIDIR DOS NÚMEROS
# DEPENDIENDO DEL TIPO DE OPERACIÓN QUE SE INIDIQUE
# ENTRADA
numero1 = int(input ("Número 1 : "))
numero2 = int(input ("Número 2 : "))
operacion = input ("Ingrese operación(+, -, *, /): ")
# PROCESO
if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    resultado = numero1 / numero2
else:
    print("Operación no válida")
    exit()
# SALIDA
print(f"{numero1} {operacion} {numero2} = {resultado}")