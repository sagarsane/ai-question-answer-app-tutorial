from pymongo import MongoClient
import key_param

# create mongo client
client = MongoClient(key_param.MONGO_URI)
# create database
db = "langchain_demo"
# create collection
collectionName = "collection_of_text_blobs"
collection = client[db][collectionName]