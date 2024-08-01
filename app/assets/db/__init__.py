from pymongo import MongoClient
from hashlib import md5
from uuid import uuid4
from os import getenv

try:
    Client = MongoClient(getenv("DB_URL"))
    database = Client.get_database('automate')
except:
    print('Erro ao conectar ao banco de dados')