from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)
pilot_hw = client.c4e
post = pilot_hw["post"]
new_post = {
    "title":"C4E",
    "author":"Huế xinh đẹp :3",
    "content":"anh Quân và anh Đạt rất nhiệt tình :3"
}
post.insert_one(new_post)
# print ("saving document {0}....".format(i+1))
