import requests
from config import *

def list_roles():
    url = baseUrl+"/workspace/v2/roles"

    payload = {}
    headers = {
        "Authorization": "Bearer "+accessKey}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)



if __name__ == '__main__':
    list_roles()

