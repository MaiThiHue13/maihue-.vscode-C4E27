# ex4
from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
pilot_hw = client.c4e
river = pilot_hw["river"]