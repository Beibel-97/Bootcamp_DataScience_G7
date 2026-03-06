# BUCLE WHILE A DIFERECIA DE FOR EJECUTA UNA ACCIÓN MIENTRAS SE CUMPLA UNA CONDICIÓN
contador = 1
while (contador <= 10):
    print(contador)
    contador += 1
numero_adivinar = 5
print ("ADIVINA EL NÚMERO QUE ESTOY PENSANDO")
while (contador != numero_adivinar):
    contador = int(input())
    if contador == numero_adivinar:
        print ("GANASTE")
    else:
        print ("INTENTA DE NUEVO : ")
    