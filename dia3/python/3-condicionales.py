# CALCULADORA
# CREAR UN PROGRAMA QUE PERMITA SUMAR RESTAR MUTIPLICAR O DIVIDIR 2 NÚMEROS
# DEPENDIENDO DEL TIPO DE OPERACIÓN QUE SE INDIQUE
# ENTRADA
numero1 = int(input("Número 1 : "))
numero2 = int(input("Número 2 : "))
operacion = input("Ingrese operación(+ - x /): ")
# PROCESO
if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "x":
    resultado = numero1 * numero2
elif operacion == "/":
    resultado = numero1 / numero2
else:
    print("Operación no valida...")
    exit()
# SALIDA
print(f"{numero1} {operacion} {numero2} = {resultado}")