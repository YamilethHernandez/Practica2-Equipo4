import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    a: int = None
    b: int = None


app = FastAPI()


@app.get("/")
async def get_info():
    '''
    Esta es una simple solicitud de obtención
         : return: devuelve datos directamente
    '''
    data = {
        "username": "test",
        "password": "admin123"
    }
    return data

@app.get("/post_info2")
async def post_info2(a: int,b:int):
    '''
         Una solicitud de obtención con parámetros
    :param a: 
    :param b: 
    :return: a + b
    '''
    c = a + b
    result = {'a': a, 'b': b, 'a+b': c}
    return result

@app.post("/post_info1")
async def post_info1(request_data: Item):
    '''
         Debe pasar la interfaz de publicación json
         : param request_data: campo json (clase de artículo)
         : return: devuelve la suma de a + b
    '''
    a = request_data.a
    b = request_data.b
    c = a + b
    result = {'a': a, 'b': b, 'a+b': c}
    return result

if __name__ == '__main__':
    uvicorn.run(app=app, host='192.168.10.102', port=8000)