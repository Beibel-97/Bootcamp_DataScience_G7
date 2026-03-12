import math
# CALCULADORA
salir = "no"
while(salir == "no"):
    # ENTRADA
    print("================ CALCULADORA CON PYTHON ============")

    print("========= OPCIONES ========")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. tabla de multiplicar")
    print("6. raiz cuadrada")
    opcion = int(input("Ingrese la opcion que desea: "))
    
    #PROCESO
    if(opcion >= 1 and opcion <=4):
        numero1 = int(input("Número 1 : "))
        numero2 = int(input("Número 2 : "))
        if opcion == 1:
            operacion = "suma"
            resultado = numero1 + numero2
        elif opcion == 2:
            operacion = "resta"
            resultado = numero1 - numero2
        elif opcion == 3:
            operacion = "multiplicación"
            resultado = numero1 * numero2
        elif opcion == 4:
            operacion = "división"
            resultado = numero1 / numero2

        print(f"La {operacion} de {numero1} y {numero2} es {resultado}")
    
    elif opcion == 5:
        tabla = int(input("Ingrese la tabla de multiplicar que desea ver : "))
        for contador in range(1,13,1):
            resultado = tabla * contador
            print(f'{tabla} x {contador} = {resultado}')
            
    elif opcion == 6:
        numero = int(input("ingrese el número para calcular su raiz cuadra : "))
        raiz = math.sqrt(numero)
        print(f'la raiz cuadra de {numero} es {raiz}')
        
    else:
        print("opción no valida...")
    
    
    
    salir = input("Desea salir del programa ?(si,no) : ")
    if salir == "si":
        break