class Persona:
    
    def __init__(self,nom,ema):
        self.nombre = nom
        self.email = ema
        
    def mostrar(self):
        print("NOMBRE : " + self.nombre)
        print("EMAIL : " + self.email)
        
class Alumno(Persona):
    
    def __init__(self,nom,ema,nota):
        super().__init__(nom,ema)
        self.nota = nota
        
    def mostrar(self):
        print("===== DATOS DEL ALUMNO =====")
        super().mostrar()
        print(f"NOTA : {self.nota}")
        
class Profesor(Persona):
    
    def __init__(self,nom,ema,esp):
        super().__init__(nom,ema)
        self.especialidad = esp
        
    def mostrar(self):
        print("============== DATOS DEL PROFESOR ==============")
        super().mostrar()
        print(f"ESPECIALIDAD : {self.especialidad}")

        
alumno1 = Alumno("Juan Perez", "jperez@gmail.com",20)
#alumno1.mostrar()
profesor1 = Profesor("Ana Gomez", "agomez@codigo.edu.pe","Desarrollo Web Full Stack")
#profesor1.mostrar()

# función que usa polimorfismo
def presentar_datos(persona):
    persona.mostrar()
    
presentar_datos(alumno1)
presentar_datos(profesor1)