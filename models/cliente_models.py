from pydantic import BaseModel

class ClientesIn(BaseModel):
    cc: int
   # nombre: str
   # telefono: int
   # email: str
   # direccion : str
   # ciudad : str

class ClientesOut(BaseModel):
    nombre: str
    cc: int
    telefono: int
    email: str
    direccion : str
    ciudad : str