import pymongo
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://root:9054899580@cluster0.imux3xq.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


d = {
    "name" : "Sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}

d = {
    "name" : "Sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
d = {
    "name" : "Sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
d = {
    "name" : "Sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
d = {
    "name" : "Sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)