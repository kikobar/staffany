import requests
from config import *
import json
from datetime import datetime, timezone, UTC, date, timedelta
from zoneinfo import ZoneInfo
from push import *

def list_shift_slots():
    from_date = str(input('From date [YYYY-MM-DD]: '))
    from_date = str(datetime.strptime(from_date+" 00:01", "%Y-%m-%d %H:%M").replace(tzinfo=ZoneInfo(IANATimeZone)))
    from_date = datetime.fromisoformat(from_date).timestamp()
    from_date = datetime.fromtimestamp(from_date,tz=timezone.utc).isoformat().replace("+00:00","Z")
    to_date = str(input('To date [YYYY-MM-DD]: '))
    to_date = str(datetime.strptime(to_date+" 23:59", "%Y-%m-%d %H:%M").replace(tzinfo=ZoneInfo(IANATimeZone)))
    to_date = datetime.fromisoformat(to_date).timestamp()
    to_date = datetime.fromtimestamp(to_date,tz=timezone.utc).isoformat().replace("+00:00","Z")

    url = baseUrl+"/workspace/v2/shift-slots?start="+from_date+"&end="+to_date

    payload = {}
    headers = {
        "Authorization": "Bearer "+accessKey}

    response = requests.request("GET", url, headers=headers, data=payload)
    slots = json.loads(response.text)['data']['items']
    for key in slots:
        print(key)
        push(key,slotsCollection)



if __name__ == '__main__':
    list_shift_slots()

