#ENCAPSULAMIENTO EN POO CON PYTHON
class Usuario:
    __email = 'admin@gmail.com'
    __password = '123'
    
    def __init__(self):
        pass
    
    def login(self,email,password):
        if email == self.__email and password == self.__password:
            print('Login Exitoso')
        else:
            print('Login fallido')
    
    def set_email(self,email):
        self.__email = email
            
print("===== LOGIN DE USUARIOS ====")
email = input('Ingrese Email : ')
password = input('Ingrese Password : ')

usuario = Usuario()
#print(f"password : {usuario.__password}")
#usuario.__password = password
usuario.set_email('cesar@gmail.com')
usuario.login(email,password)