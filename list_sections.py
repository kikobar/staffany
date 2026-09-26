import requests
from config import *
import json
from push import *

def list_sections():
    url = baseUrl+"/workspace/v2/sections"

    payload = {}
    headers = {
        "Authorization": "Bearer "+accessKey}

    response = requests.request("GET", url, headers=headers, data=payload)
    sections = json.loads(response.text)['data']['items']
    for key in sections:
        print(key)
        push(key,sectionsCollection)



if __name__ == '__main__':
    list_sections()

