from pymongo import MongoClient
from config import *
import sys
import json

def delete(collec,query_filter):
	client = MongoClient(CONNECTION_STRING)
	database = client[DATABASE]
	collection = database[collec]
	result = collection.delete_many(query_filter)
	print(result.raw_result)
	
	
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Please pass exactly 2 parameters to this script: 1) collection name 2) query')
    else:
        delete(sys.argv[1],json.loads(sys.argv[2]))
    
