from pydantic import BaseModel
from datetime import datetime
from datetime import date

class ComprasIn(BaseModel):
    cc_cliente: int
   
class ComprasOut(BaseModel):
    id_compra: int
    #fecha: datetime
    cc_cliente:int
    nombre_producto: str
    cantidad: int
    precio_pub : float
    costo_total: float