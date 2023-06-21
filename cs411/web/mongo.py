from pymongo import MongoClient

connection_string = 'mongodb+srv://lkk19:IONc14XUBjIgI9Oi@cluster0.6oclfrh.mongodb.net/Testing'

# Create a MongoClient to interact with MongoDB Atlas
client = MongoClient(connection_string)

# Select your database
db = client['Testing'] # Replace 'YourDatabaseName' with your database name

# Select the collection within the database
collection = db['test'] # Replace 'YourCollectionName' with your collection name

# Insert data into the collection
data = {'name': 'John Doe', 'email': 'john.doe@example.com'}
collection.insert_one(data)
