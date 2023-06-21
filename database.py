from pymongo import MongoClient

# Establish a connection to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

def insert_data(data):
    # Logic to insert data into MongoDB
    collection = db['mycollection']
    collection.insert_one(data)

def get_data():
    # Logic to query data from MongoDB
    collection = db['mycollection']
    data = collection.find()
    return list(data)