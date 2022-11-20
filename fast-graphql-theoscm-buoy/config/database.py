from gridfs import Database
from pymongo import MongoClient
from decouple import config

# connect to database
DATABASE = config("MONGOURL")
connection = MongoClient(
    DATABASE
    )
