from pymongo import MongoClient
# from faker import Faker
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient (mongo_uri)
pilot_hw = client.c4e
customers = pilot_hw["customers"]

# events = []
event_counts = 0
# ads = []
ads_counts = 0
# wom = []
wom_counts = 0
all_customers = list(customers.find())
for i in all_customers:
    # print(all_customers)
    if i["ref"] == "events":
        # events.append(i)
        event_counts += 1

    elif i["ref"] == "ads":
        # ads.append(i)
        ads_counts += 1
    else:
        # wom.append(i)
        wom_counts += 1
print("events: ", event_counts)
print("ads: ", ads_counts)
print("wom: ", wom_counts)

# prepare data
refs_counts = [event_counts, ads_counts, wom_counts]

# prepare labels
refs_name = ["events", "advertisements", "word of mouth"]

# draw pie
pyplot.pie(refs_counts,labels=refs_name, autopct="%1.f%%",shadow=True, explode=[0,0,0.1])
pyplot.title("events, advertisements, word of mouth ")

# show
pyplot.show()
