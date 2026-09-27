import requests
from config import *
import json
from push import *
from delete import *

def delete_timesheet_attendance_data():
    query = {}
    delete(shiftRecordsCollection,query)
    delete(clockAttemptsCollection,query)
    delete(workHoursCollection,query)



if __name__ == '__main__':
    delete_timesheet_attendance_data()

