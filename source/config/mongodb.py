from pymongo import MongoClient
from source.config.env import user, password,host

uri = f'mongodb://{user}:{password}@{host}'

conn = MongoClient(uri, port=27017, UuidRepresentation='pythonLegacy')
