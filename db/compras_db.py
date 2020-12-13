from datetime import datetime
from typing import  Dict
from pydantic import BaseModel

class ComprasInDB(BaseModel):
    id_compra: int
    fecha: datetime
    cc_cliente:int
    nombre_producto: str
    cantidad: int
    precio_pub : float
    costo_total: float

database_compras = Dict[int, ComprasInDB]

database_compras = {
    1: ComprasInDB(**{"id_compra":1,
                        "fecha":"2020-12-01 22:16:29",
                        "cc_cliente":1057123440,
                        "nombre_producto":"Kit Herramientas",
                        "cantidad":2,
                        "precio_pub":12000,
                        "costo_total":24000,
                    }),
     
    2: ComprasInDB(**{"id_compra":2,
                        "fecha":"2020-12-03 18:16:29",
                        "cc_cliente":35098653,
                        "nombre_producto":"Taladro Black & Decker",
                        "cantidad":1,
                        "precio_pub":50000,
                        "costo_total":50000,
                    }),
                            
    3: ComprasInDB(**{"id_compra":3,
                        "fecha":"2020-12-05 11:00:09",
                        "cc_cliente":1069264262,
                        "nombre_producto":"Galon de Pintura Pintuco Terracota",
                        "cantidad":5,
                        "precio_pub":30000,
                        "costo_total":150000,
                    }),

    4: ComprasInDB(**{"id_compra":4,
                        "fecha":"2020-12-08 12:10:30",
                        "cc_cliente":91567991,
                        "nombre_producto":"Alambre de cobre x metro",
                        "cantidad":4,
                        "precio_pub":2000,
                        "costo_total":8000,
                    }),

    5: ComprasInDB(**{"id_compra":5,
                        "fecha":"2020-12-13 15:45:29",
                        "cc_cliente":35098653,
                        "nombre_producto":"Placas Metálicas Aluminio 2m x 1m Calibre 16",
                        "cantidad":3,
                        "precio_pub":35000,
                        "costo_total":105000,
                    }),
}

generator = {"id":5}

def get_Compra_Cliente(cedulas: int):
    cliente_in_idcompra = [x for x in database_compras if database_compras[x]["cc_cliente"] == cedulas]
    return cliente_in_idcompra

def save_compra(compra_in_db: ComprasInDB):
    generator["id"] = generator["id"] + 1
    compra_in_db.id_compra = generator["id"]
    database_compras[compra_in_db.id_compra] = compra_in_db.dict()
    return compra_in_db