from pymongo import MongoClient

connection_string = 'mongodb+srv://lkk19:IONc14XUBjIgI9Oi@cluster0.6oclfrh.mongodb.net/Testing'

def insert_data(collection_name, query, data):
    client = MongoClient(connection_string)
    db = client['Testing']
    collection = db[collection_name]
    result = collection.update_one(query, {'$set': data}, upsert=True)
    client.close()
    return result

