from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# ------------------------------------
# Conexión mysql
# ------------------------------------
#sqlite "sqlite:///personas.db"
DATABASE_URL = (
    "mysql+mysqldb://root:root2025@localhost/db_housing_api"
)
engine = create_engine(
    DATABASE_URL,
    echo=True
)

# ------------------------------------
# Clase base para modelos
# ------------------------------------

Base = declarative_base()

# ------------------------------------
# Modelo = tabla
# ------------------------------------
class Persona(Base):
    __tablename__ = "personas"
    
    id = Column(Integer,primary_key=True)
    nombre = Column(String(100))
    edad = Column(Integer)
    
    def __repr__(self):
        return f"Persona(id={self.id}, nombre='{self.nombre}', edad={self.edad})"
    
# ------------------------------------
# Crear tablas
# ------------------------------------

Base.metadata.create_all(engine)

# ----------------------------------
# Crear sesión
# ----------------------------------
Session = sessionmaker(bind=engine)

session = Session()

# ----------------------------------
# INSERT
# ----------------------------------
persona = Persona(
    nombre="Juan",
    edad=25
)
session.add(persona)

session.commit()
print("Persona insertada")

# ----------------------------------
# SELECT
# ----------------------------------

print("\nListado:")

personas = session.query(Persona).all()

for persona in personas:
    print(persona)
    
# ----------------------------------
# SELECT POR ID
# ----------------------------------

persona = session.query(Persona).filter(
    Persona.id == 1
).first()

print("\nPersona encontrada")
print(persona)

# ----------------------------------
# UPDATE
# ----------------------------------

persona.edad = 40

session.commit()

print("\nPersona actualizada")

# ----------------------------------
# DELETE
# ----------------------------------

session.delete(persona)
session.commit()

# ----------------------------------
# Cerrar sesión
# ----------------------------------
session.close()