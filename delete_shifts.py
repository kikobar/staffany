import requests
from config import *
import json
from push import *
from delete import *

def delete_shifts():
    query = {}
    delete(shiftsCollection,query)



if __name__ == '__main__':
    delete_shifts()

