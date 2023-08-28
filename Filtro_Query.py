#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Levantamos el server Uvicorn
#-uvicorn Filtro_Query:app --reload-
#{"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}
#Definimos nuestra entidad: User

class User(BaseModel):
    id:int
    name: str
    lastName:str
    age:int
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= [User(id=0,name="Juan", lastName="Garcia", age="30"),
             User(id=1,name="Juan", lastName="Perez", age="30"),
             User(id=2,name="María", lastName="Lopez", age="22")]




#***Get con Filtro Query
@app.get("/usersclass/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1
 
 
 #***Get con Filtro Query
@app.get("/usersclass2/")
async def usersclass(age:int, name:str):
    users=filter (lambda user: user.age == age, users_list)#Función de orden superior
    users1=filter (lambda user: user.name == name, users)#Función de orden superior
    try:
        return list(users1)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass2/?age=30&name=Juan