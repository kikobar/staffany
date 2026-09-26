import requests
from config import *
import sys

def retrieve_staff_member(staffId):
    url = baseUrl+"/workspace/v2/staff/"+staffId

    payload = {}
    headers = {
        "Authorization": "Bearer "+accessKey}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)



if __name__ == '__main__':
    retrieve_staff_member(sys.argv[1])

