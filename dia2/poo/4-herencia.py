class Persona:
    # constructor de clase
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        
class Alumno(Persona):
    pass

class Profesor(Persona):
    
    def __init__(self,nombre,email,especialidad):
        super().__init__(nombre,email)
        self.especialidad = especialidad
        
    def mostrar_profesor(self):
        print(f'Nombre : {self.nombre}')
        print(f'Email : {self.email}')
        print(f'Especialidad : {self.especialidad}')
        

alumno = Alumno('Juan Perez','jperez@gmail.com')
alumno.mostrar()

profesor = Profesor('Ana Gomez','agomez@universidad.com','Data Analytics')
profesor.mostrar_profesor()