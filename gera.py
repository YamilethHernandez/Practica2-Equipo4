from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

gapp = FastAPI()

class  Frutero(BaseModel): 
    name: str
    fruta: List[str] = []

@gapp.get("/")
def read_root():
    return {"Frutero": "Ricas frutas"}

@gapp.put("/fruta/")
def agregar_fruta(fruta: Frutero):
    return{"message": f"agregar_fruta: {fruta.name}"}