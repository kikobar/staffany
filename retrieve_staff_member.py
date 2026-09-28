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
    if len(sys.argv) != 2:
        print('Please pass exactly 1 parameter, the staffId of the staff member')
    else:
        retrieve_staff_member(sys.argv[1])

