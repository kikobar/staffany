import requests
from config import *
import json
from push import *

def list_roles():
    url = baseUrl+"/workspace/v2/roles"

    payload = {}
    headers = {
        "Authorization": "Bearer "+accessKey}

    response = requests.request("GET", url, headers=headers, data=payload)
    roles = json.loads(response.text)['data']['items']
    for key in roles:
        print(key)
        push(key,rolesCollection)



if __name__ == '__main__':
    list_roles()

