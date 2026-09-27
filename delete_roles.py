import requests
from config import *
import json
from push import *
from delete import *

def delete_roles():
    query = {}
    delete(rolesCollection,query)



if __name__ == '__main__':
    delete_roles()

