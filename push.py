from pymongo import MongoClient
from config import *
import sys
import json

def push(document,collection):
	client = MongoClient(CONNECTION_STRING)
	database = client[DATABASE]
	collection = database[collection]
	collection.insert_one(document)
	
	
if __name__ == '__main__':
    push(sys.argv[1],sys.argv[2])
    
