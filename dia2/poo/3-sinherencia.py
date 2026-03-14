class Alumno:
    
    # constructor de clase
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        
class Profesor:
    
    def __init__(self,nombre,email,especialidad):
        self.nombre = nombre
        self.email = email
        self.especialidad = especialidad
        
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f'Especialidad : {self.especialidad}')
        
alumno = Alumno('Juan Perez','jperez@gmail.com')
alumno.mostrar()

profesor = Profesor('Ana Gomez','agomez@universidad.com','Data Analytics')
profesor.mostrar()