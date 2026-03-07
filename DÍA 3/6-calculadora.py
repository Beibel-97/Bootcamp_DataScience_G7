import math 
# CALCULADORA
salir = "NO"
while (salir == "NO"):
    salir = input ("¿Desea salir? (SI/NO): ")
    # ENTRADA
    print ("============================CALCULADORA CON PYTHON=================================")
    
    print ("===============OPCIONES===============")
    print ("1. Suma")
    print ("2. Resta")
    print ("3. Multiplicación")
    print ("4. División")
    print ("5. Tabla de Multiplicar")
    print ("6. raíz cuadrada")
    opcion = int(input ("Ingrese la opción que desea realizar: "))
    
    # PROCESO
    if (opcion >= 1 and opcion <= 4):
        numero1 = int(input ("Número 1 : "))
        numero2 = int(input ("Número 2 : "))
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

    elif (opcion == 5):    
        tabla = int(input ("Ingrese la tabla de multiplicar que desea ver: "))
        for contador in range (1,13,1):
            resultado = tabla * contador
            print (f"{tabla} x {contador} = {resultado}")
    
    elif (opcion == 6):
        numero = int(input ("Ingrese el número para calcular su raíz cuadrada: "))
        raiz = math.sqrt(numero)
        print (f"La raíz cuadrada de {numero} es {raiz}")
    
    else:  
        print ("Opción no válida")
    
    
    
    salir = input ("¿Desea salir? (SI/NO): ")
    if (salir == "SI"):
        break
    
    