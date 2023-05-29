from pymongo import MongoClient
from bson.objectid import ObjectId

GAME_COLLECTION_NAME = "games"
USER_COLLECTION_NAME = "users"

def get_database():
    # Fornecer a URL do mongodb atlas para conectar python ao mongodb usando pymongo (add string de conexão com meu banco de dados)
    CONNECTION_STRING = "mongodb+srv://admin:fgRsevzWmrupxkD5@product-manager.lor6uci.mongodb.net/?retryWrites=true&w=majority"

    # Conexão usando MongoClient

    client = MongoClient(CONNECTION_STRING)

    # Criando o banco de dados 
    return client ['product-manager']

def list_games():
    dbGameVault = get_database()
    collection_name = dbGameVault[GAME_COLLECTION_NAME]
    
    item_details = collection_name.find()
    for item in item_details:
        print(item)

    return item_details

#usuário pode cadastrar seu game 
def save_game(game):
    dbGameVault = get_database()
    collection_name = dbGameVault[GAME_COLLECTION_NAME]
    
    collection_name.insert_one(game)

def delete_game(id):
    dbGameVault = get_database()
    collection_name = dbGameVault[GAME_COLLECTION_NAME]

    myquery = { "_id": ObjectId(id) }
    
    collection_name.delete_one(myquery)

# Criar cadastro de usuário

def get_user(email):
    dbGameVault = get_database()
    collection_name = dbGameVault[USER_COLLECTION_NAME]

    myquery = {"email": email }
    user = collection_name.find_one(myquery)
    return user

def save_user(user):
    dbGameVault = get_database()
    collection_name = dbGameVault[USER_COLLECTION_NAME]
    
    collection_name.insert_one(user)