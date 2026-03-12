import os
from time import sleep

"""
CRUD
 - CREATE
 - READ
 - UPDATE
 - DELETE
"""
ANCHO = 50

dic_alumnos = {
    '12345678':{
        'nombre':'Juan Perez',
        'email':'juanperez@gmail.com'
    },
    '10010010':{
        'nombre':'Ana Lopez',
        'email':'analopez@gmail.com'
    }
}

while(True):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "GESTIÓN DE ALUMNOS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR ALUMNO
         [2] MOSTRAR ALUMNOS
         [3] ACTUALIZAR ALUMNO
         [4] ELIMINAR ALUMNO
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR ALUMNO")
        print("=" * ANCHO)
    if opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR ALUMNOS")
        print("=" * ANCHO)
    if opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR ALUMNO")
        print("=" * ANCHO)
    if opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR ALUMNO")
        print("=" * ANCHO)
    if opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL SISTEMA...")
        print("=" * ANCHO)
        sleep(2)
        break
    
    input("Presione ENTER para continuar...")