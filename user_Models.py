#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

class User(BaseModel):
    id:str | None
    username: str
    email:str
    