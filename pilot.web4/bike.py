from pymongo import MongoClient


# 1, connect mobgo
mongo_uri = "mongodb+srv://admin:admin@pilot-app-wgovx.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)

# 2. get/create database
bike_db = client.bikes

# 3. get/create database
bike_collection = bike_db["my_collection"]