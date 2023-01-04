import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import time
import datetime
import bamboo

env_path = ".env"
load_dotenv(env_path)

slack_token = os.environ["SLACK_USER_TOKEN"]


client = WebClient(token=slack_token)


emplst = bamboo.employee_list

count = len(emplst)
print(count)


for item in emplst:
    mail = item['email']
    date = item['end']
    print(mail)
    print(date)

    date_format = '%Y-%m-%d'  
    date = datetime.datetime.strptime(date, date_format)
    date_tuple = date.timetuple()

    unix_time = time.mktime(date_tuple)
    print(unix_time)

    try:
     response = client.users_lookupByEmail(email = mail)
     mem_id = response['user']['id']
     print(mem_id)
    except SlackApiError as e:
     print("Error searching for user: {}".format(e))


    try:   
     client.users_profile_set(
        user=mem_id,
        profile={
            "status_text": "Leave of Absence",
            "status_emoji": ":mountain_railway:",
            "status_expiration": unix_time
        }
    )
    except SlackApiError as e:    
     print("Error updating status: {}".format(e))




   

   


