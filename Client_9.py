#Este fichero será encargado de gestionar la conexión de nuestra base de datos con Mongo DB

from pymongo import MongoClient

#Instancia de tipo MongoClient (si no se le asignan argumentos se conecta al localhost por default)
db_client= MongoClient()