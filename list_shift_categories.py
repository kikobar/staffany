import requests
from config import *

def list_shift_categories():
    url = baseUrl+"/workspace/v2/shift-categories"

    payload = {}
    headers = {
        "Authorization": "Bearer "+accessKey}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)



if __name__ == '__main__':
    list_shift_categories()

