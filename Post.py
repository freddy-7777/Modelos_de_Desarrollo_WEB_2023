#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Levantamos el server Uvicorn
#-uvicorn Post:app --reload-
#{"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}
#Definimos nuestra entidad: User

class User(BaseModel):
    id:int
    Name: str
    LastName:str
    Age:int
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= [User(id=0,Name="Alfredo", LastName="Garcia", Age="30"),
             User(id=1,Name="Juan", LastName="Perez", Age="45"),
             User(id=2,Name="María", LastName="Lopez", Age="22")]


#***Get
@app.get("/usersclass/")
async def usersclass():
    return (users_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/


#***Post
@app.post("/usersclass/")
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/