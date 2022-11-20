from decouple import config
from pymongo import MongoClient

MONGO_URI = config("MONGODB_URI")
# connect to database
connection = MongoClient(
    MONGO_URI
)