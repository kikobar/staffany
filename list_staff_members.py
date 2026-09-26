import requests
from config import *
import json
from push import *

def list_staff_members():
    url = baseUrl+"/workspace/v2/staff"

    payload = {}
    headers = {
        "Authorization": "Bearer "+accessKey}

    response = requests.request("GET", url, headers=headers, data=payload)
    staff = json.loads(response.text)['data']['items']
    for key in staff:
        print(key)
        push(key,staffCollection)



if __name__ == '__main__':
    list_staff_members()

