import requests
from config import *

def list_teams():
    url = baseUrl+"/workspace/v2/teams"

    payload = {}
    headers = {
        "Authorization": "Bearer "+accessKey}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)



if __name__ == '__main__':
    list_teams()

