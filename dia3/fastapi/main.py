from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message":"Mi primera API con FastAPI"}

#Path Parameters y Query Parameters
@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    return {
        "id":usuario_id,
        "nombre":"César"
    }
    
@app.get("/productos")
def listar_productos(categoria: str="todos",precio_min: float=0):
    return {
        "categoria":categoria,
        "precio_minimo":precio_min,
        "productos": [
            {"id": 1, "nombre": "Laptop", "precio": 3500},
            {"id": 2, "nombre": "Mouse", "precio": 80}
        ]
    }
    
# Validación con Pydantic
#sin validación
@app.post("/productos")
def crear_producto(data: dict):
    nombre = data.get("nombre")
    precio = data.get("precio")
    
    return {
        "nombre":nombre,
        "precio":precio
    }
#con validación usando pydantic
from pydantic import BaseModel, Field

class Producto(BaseModel):
    nombre: str = Field(
        min_length=3,
        max_length=50
    )

    precio: float = Field(
        gt=0
    )
    
@app.post("/productosval")
def crear_producto_validado(producto: Producto):

    return {
        "nombre": producto.nombre,
        "precio": producto.precio
    }