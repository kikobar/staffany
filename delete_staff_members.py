import requests
from config import *
import json
from push import *
from delete import *

def delete_staff_members():
    query = {}
    delete(staffCollection,query)



if __name__ == '__main__':
    delete_staff_members()

