import requests
from config import *
import json
from push import *
from delete import *

def delete_shift_slots():
    query = {}
    delete(slotsCollection,query)



if __name__ == '__main__':
    delete_shift_slots()

