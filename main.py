from db.clientes_db import ClientesInDB
from db.clientes_db import update_cliente, get_cliente, save_cliente
from db.compras_db import ComprasInDB
from db.compras_db import save_compra, get_Compra_Cliente
from models.cliente_models import ClientesIn, ClientesOut
from models.compras_models import ComprasIn, ComprasOut
import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8000",
    "https://minisap01.herokuapp.com" #Nombre de la app en Heroku - MiniSAP 
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@api.post("/clientes/registro_cliente/{cc}")
async def Reg_cliente(cliente_in: ClientesIn):
    cliente_in_db = get_cliente(cliente_in.cc)
    if cliente_in_db == None:
        save_cliente(cliente_in)
        Estado = {"Creado": True}
    else:
        Estado = {"Creado": False}
        #raise HTTPException(status_code=404, detail="El cliente ya existe") 
    return  Estado

@api.get("/clientes/consultar/{cc}")
async def Obtener_cliente(cc: int):
    clientes_in_db = get_cliente(cc)
    if clientes_in_db != None:
        clientes_out = ClientesOut(**clientes_in_db.dict())
        return clientes_out  
    else:
        raise HTTPException(status_code=404, detail="El cliente no existe")

@api.get("/clientes/compras/{cc}")
async def Obtener_compras(cc: int):
    compras_in_db = get_Compra_Cliente(cc)
    compras_out = []
    if compras_in_db != None:
        for i in compras_in_db:            
            compra_out = ComprasOut(**i.dict())
            compras_out.append(compra_out)
        return compras_out 
    else:
        raise HTTPException(status_code=404, detail="El cliente no registra compras")

@api.put("/clientes/actualizar/")
async def Actualizar_cliente(clientes_in: ClientesIn):
    clientes_in_db = get_cliente(clientes_in.cc)
    if clientes_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    else:  
        update_cliente(clientes_in_db)
        raise HTTPException(status_code=200, detail="El cliente has sido actualizado")
