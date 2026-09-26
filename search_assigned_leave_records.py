import requests
from config import *
import json
from datetime import datetime, timezone, UTC, date, timedelta
from zoneinfo import ZoneInfo

def search_assigned_leave_records():
    from_date = str(input('From date [YYYY-MM-DD]: '))
    to_date = str(input('To date [YYYY-MM-DD]: '))

    url = baseUrl+"/workspace/v2/leaves/records/search"

    payload = json.dumps({
        "dateRange": {
            "from": from_date,
            "to": to_date
            }
        })
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "+accessKey
        }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)



if __name__ == '__main__':
    search_assigned_leave_records()

