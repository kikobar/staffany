import requests
from config import *

def list_sections():
    url = baseUrl+"/workspace/v2/sections"

    payload = {}
    headers = {
        "Authorization": "Bearer "+accessKey}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)



if __name__ == '__main__':
    list_sections()

