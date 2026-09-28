import requests
from config import *
import json
from datetime import datetime, timezone, UTC, date, timedelta
from zoneinfo import ZoneInfo
from push import *
import sys

def retrieve_timesheet_attendance_data(from_date=None,to_date=None):
    if not (from_date and to_date):
        from_date = str(input('From date [YYYY-MM-DD]: '))
        to_date = str(input('To date [YYYY-MM-DD]: '))

    url = baseUrl+"/workspace/v1/timesheets"

    payload = json.dumps({
        "range": {
            "from": from_date,
            "to": to_date
            }
        })
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "+accessKey
        }

    response = requests.request("POST", url, headers=headers, data=payload)
    shiftRecords = json.loads(response.text)['data']['shiftRecords']
    for key in shiftRecords:
        print(key)
        push(key,shiftRecordsCollection)
    clockAttempts = json.loads(response.text)['data']['clockAttempts']
    for key in clockAttempts:
        print(key)
        push(key,clockAttemptsCollection)
    workHours = json.loads(response.text)['data']['workHours']
    for key in workHours:
        print(key)
        push(key,workHoursCollection)



if __name__ == '__main__':
    if len(sys.argv) != 3:
        retrieve_timesheet_attendance_data()
    else:
        retrieve_timesheet_attendance_data(sys.argv[1],sys.argv[2])

