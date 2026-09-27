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
    delete(sys.argv[1],sys.argv[2])
    
