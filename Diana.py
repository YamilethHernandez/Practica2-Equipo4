from enum import Enum

from fastapi import FastAPI

app = FastAPI()

class ModelName(str, Enum):
    Nombre = "Nombre"
    Apellidos = "Apellidos"
    IRyC = "IRyC"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.Nombre:
        return {"model_name": model_name, "message": "Mi Nombre Diana Berenice"}
       

    if model_name.value == "IRyC":
        return {"model_name": model_name, "message": "Carrera: Ingeniería en Redes Inteligentes y Ciberseguridad"}

    return {"model_name": model_name, "message": "Mis apellidos son Aguilar"}