import requests
from config import *
import json
from push import *
from delete import *

def delete_sections():
    query = {}
    delete(sectionsCollection,query)



if __name__ == '__main__':
    delete_sections()

