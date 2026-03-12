import csv
import os

ARCHIVO_CSV = 'alumnos.csv'

def cargar_alumnos():
    alumnos = {}

    if os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, mode="r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                dni = fila["dni"]
                alumnos[dni] = {
                    "nombre": fila["nombre"],
                    "email": fila["email"]
                }

    return alumnos

def guardar_alumnos(alumnos):
    with open(ARCHIVO_CSV, mode="w", encoding="utf-8", newline="") as archivo:
        campos = ["dni", "nombre", "email"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        for dni, info in alumnos.items():
            escritor.writerow({
                "dni": dni,
                "nombre": info["nombre"],
                "email": info["email"]
            })

alumnos = cargar_alumnos()