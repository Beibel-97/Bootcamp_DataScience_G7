from tkinter import *
from tkinter.ttk import Treeview

# Crear ventana principal
ventana = Tk()
ventana.title("Ejemplo Treeview")
ventana.geometry("500x300")


# ==========================
# CREAR TREEVIEW (TABLA)
# ==========================

# Treeview es un widget que permite mostrar datos en forma de tabla
tabla = Treeview(ventana)

# Definir las columnas de la tabla
# "columns" recibe una tupla con los nombres internos de las columnas
tabla["columns"] = ("DNI", "NOMBRE", "EMAIL")


# ==========================
# CONFIGURAR COLUMNAS
# ==========================

# "#0" es la columna especial que usa Treeview por defecto
# si no queremos usarla la ocultamos
tabla.column("#0", width=0, stretch=NO)

# column("nombre_columna", ...)
# anchor = alineación del contenido (W=izquierda, CENTER, E=derecha)
# width = ancho de la columna en pixeles
tabla.column("DNI", anchor=W, width=120)
tabla.column("NOMBRE", anchor=W, width=180)
tabla.column("EMAIL", anchor=W, width=200)


# ==========================
# ENCABEZADOS
# ==========================

# heading() define el título que aparecerá en la tabla

tabla.heading("#0", text="")  # columna oculta
tabla.heading("DNI", text="DNI")
tabla.heading("NOMBRE", text="NOMBRE")
tabla.heading("EMAIL", text="EMAIL")


# ==========================
# INSERTAR DATOS
# ==========================

# insert(parent, index, values)

# parent = nodo padre ('' significa raíz)
# index = posición donde insertar (END = al final)
# values = tupla con los datos de cada columna

tabla.insert('', END, values=("12345678", "Juan Perez", "juan@gmail.com"))
tabla.insert('', END, values=("87654321", "Ana Lopez", "ana@gmail.com"))
tabla.insert('', END, values=("44556677", "Carlos Ruiz", "carlos@gmail.com"))


# ==========================
# MOSTRAR TABLA EN LA VENTANA
# ==========================

# grid() posiciona el widget en la ventana
# row = fila
# column = columna
# padx / pady = espacios exteriores

tabla.grid(row=0, column=0, padx=20, pady=20)


ventana.mainloop()