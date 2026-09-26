import requests
from config import *

def list_staff_members():
    url = baseUrl+"/workspace/v2/staff"

    payload = {}
    headers = {
        "Authorization": "Bearer "+accessKey}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)



if __name__ == '__main__':
    list_staff_members()

