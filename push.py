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
    if len(sys.argv) != 3:
        print('Please pass exactly 2 parameters to this script: 1) json document 2) collection name')
    else:
        push(json.loads(sys.argv[1]),sys.argv[2])
    
