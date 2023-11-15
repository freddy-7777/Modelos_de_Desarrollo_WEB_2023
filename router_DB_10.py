#Acciones
#1 cambiamos path de "usersclass" a "userdb"
#Movemos basemodel
#vaciamos user list

#-uvicorn main:app --reload-

#Path:  http://127.0.0.1:8000/userdb

#POST-body-JSON
#{"username":"Alfredo", "email":"alfredo.garcia@buap.mx"}

#En vez de Importar el framework fastapi, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException
#Invocamos la entidad que hemos creado ****nEw
from db.models.user import User
#Importamos la instancia que devolvera al usuario en formato user ***new
from db.schemas.user import user_schema
#Importamos nuestro cliente para poder agregar usuarios a la db****nEw
from db.Client_9 import db_client



#Creamos un objeto a partir de la clase FastAPI
router= APIRouter()

#Levantamos el server Uvicorn
#-uvicorn 4_codigos_HTTP:app --reload-
#{"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}
#Definimos nuestra entidad: user


#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= []


#***Get
@router.get("/userdb/")
async def usersclass():
    return (users_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/


#***Get con Filtro Path
@router.get("/userdb/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/1


#***Get con Filtro Query
@router.get("/userdb/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1
 
 
#***Post
@router.post("/userdb/",response_model=User, status_code=201)
async def usersclass(user:User):
    
    #found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    #for index, saved_user in enumerate(users_list):
    #    if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
    #       raise HTTPException(status_code=204,detail="el usuario ya existe")
    #else:
    
    #2Transformo mi entidad user en un diccionario. Transformo User en diccionario
    user_dict= dict (user)
    #Elimino id del diccionario
    del user_dict["id"]
    #1 Creo un esquema que se llama usuarios dentro de Computacion
    #Computación= Base de datos
    #users= Colección o esquema
    id= db_client.Computacion.users.insert_one(user_dict).inserted_id
    
    #Consultamos el user insertado en la bd con todo y id asignado automaticamente
    #Me devuelve un JSON hay que convertirlo a un objeto tipo User (user.py en schemas)
    new_user=  user_schema(db_client.Computacion.users.find_one({"_id":id}))
    
    #La base de datos devuelve un JSON debemos transformarlo a un objeto tipo user:
    return User(**new_user)
    

    
    #http://127.0.0.1:8000/usersclass/
   
   
    #***Put
@router.put("/userdb/")
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           users_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/userdb/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del users_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}
    
    #http://127.0.0.1:8000/usersclass/1