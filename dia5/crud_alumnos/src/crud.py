from time import sleep
from src.datos import alumnos,guardar_alumnos
from src.utils import pausa,titulo,limpiar
from src.decoradores import pantalla

@pantalla("REGISTRAR ALUMNO")
def registrar_alumno():
    dni = input("INGRESE DNI : ")
    nombre = input("INGRESE NOMBRE : ")
    email = input("INGRESE EMAIL : ")
    
    alumnos[dni] = {
        "nombre":nombre,
        "email":email
    }
    titulo("ALUMNO REGISTRADO EXITOSAMENTE!!!")
    
@pantalla("MOSTRAR ALUMNOS")
def mostrar_alumnos():
    for dni,info in alumnos.items():
        print(f"DNI : {dni}")
        print(f"NOMBRE : {info['nombre']}")
        print(f"EMAIL : {info['email']}")
        print("*" * 50)
        
@pantalla("ACTUALIZAR ALUMNO")
def actualizar_alumno():
    dni = input("Ingrese DNI del alumno : ")

    if dni in alumnos:
        print(f"Alumno encontrado : {alumnos[dni]['nombre']}")
        print("Ingrese nuevos datos o presione ENTER para conservar los anteriores")

        nuevo_nombre = input(f"Nuevo nombre ({alumnos[dni]['nombre']}): ")
        nuevo_email = input(f"Nuevo email ({alumnos[dni]['email']}): ")

            
        alumnos[dni]["nombre"] = nuevo_nombre if nuevo_nombre else alumnos[dni]["nombre"]

        if nuevo_email != "":
            alumnos[dni]["email"] = nuevo_email

        print("Alumno actualizado...")
    else:
        print("Alumno no encontrado...")
        
@pantalla("ELIMINAR ALUMNO")
def eliminar_alumno():
    dni = input("Ingrese DNI del alumno : ")

    if dni in alumnos:
        del alumnos[dni]
        print("Alumno eliminado...")
    else:
        print("Alumno no encontrado...")
        
def menu_principal():
    while True:
        limpiar()
        titulo("CRUD DE ALUMNOS")
        print("""
            [1] REGISTRAR ALUMNO
            [2] MOSTRAR ALUMNOS
            [3] ACTUALIZAR ALUMNO
            [4] ELIMINAR ALUMNO
            [5] SALIR
        """)
        
        opcion = int(input("INGRESE OPCIÓN : "))
        
        if opcion == 1:
            registrar_alumno()
            pausa()
        elif opcion == 2:
            mostrar_alumnos()
            pausa()
        elif opcion == 3:
            actualizar_alumno()
            pausa()
        elif opcion == 4:
            eliminar_alumno()
            pausa()
        elif opcion == 5:
            guardar_alumnos(alumnos)
            limpiar()
            titulo("SALIENDO DEL SISTEMA...")
            print("Datos guardados en alumnos.csv")
            sleep(2)
            break
        else:
            print("Opción no válida.")