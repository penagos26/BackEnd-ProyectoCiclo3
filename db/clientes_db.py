from typing import  Dict
from pydantic import BaseModel

class ClientesInDB(BaseModel):
    nombre: str
    cc: int
    telefono: int
    email: str
    direccion : str
    ciudad : str

database_clientes = Dict[int, ClientesInDB]

database_clientes = {
    1069264262: ClientesInDB(**{"nombre":"Diego Guizasola",
                            "cc":1069264262,
                            "telefono":3173330923,
                            "email":"diego.guizasola@gmail.com",
                            "direccion":"Calle 26 # 80-22",
                            "ciudad":"Bogotá",
                            }),
     
    35098653: ClientesInDB(**{"nombre":"Patricia Gonzales",
                            "cc":35098653,
                            "telefono":3112237709,
                            "email":"paticogonza12@hotmail.com",
                            "direccion":"Calle 5 # 4-70",
                            "ciudad":"Acacias",
                            }),
                            
    45672334: ClientesInDB(**{"nombre":"Gustavo Cordoba",
                            "cc":45672334,
                            "telefono":3214567890,
                            "email":"tavocordoba93@gmail.com",
                            "direccion":"Av Colombia # 12-33",
                            "ciudad":"Cali",
                            }),

    91567991: ClientesInDB(**{"nombre":"Marina Malagon",
                            "cc":91567991,
                            "telefono":3001328877,
                            "email":"marimala01@live.com",
                            "direccion":"Carrera 80 # 21-30",
                            "ciudad":"Medellin",
                            }),

    1057123440: ClientesInDB(**{"nombre":"Andrea Calderon",
                            "cc":1057123440,
                            "telefono":3156341209,
                            "email":"ancarocalosp01@yahoo.com",
                            "direccion":"Av San Martin # 17-35",
                            "ciudad":"Sogamoso",
                            }),
}

def get_cliente(cedulas: int):
    if cedulas in database_clientes.keys():
        return database_clientes[cedulas]
    else:
        return None

def save_cliente(cliente_in_db: ClientesInDB):
    database_clientes[cliente_in_db.cc] = cliente_in_db.dict()
    return cliente_in_db

def update_cliente(cliente_in_db: ClientesInDB):
    database_clientes[cliente_in_db.cc] = cliente_in_db.dict()
    return cliente_in_db