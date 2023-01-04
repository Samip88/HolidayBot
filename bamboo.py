import pandas as pd
import requests
import time
KEY = "377499767a589821743c5a706d03149f4e360306"
subdomain = "webo.bamboohr.com"
uri = f"https://{KEY}:x@api.bamboohr.com/api/gateway.php/{subdomain}/v1/time_off/whos_out/"
headers = {"accept": "application/json"}
response = requests.get(uri, headers=headers)
employee_list = []

def get_employee_info(empl_id):
    print(empl_id)
    empl_uri = f"https://{KEY}:x@api.bamboohr.com/api/gateway.php/{subdomain}/v1/employees/{empl_id}/?fields=firstName%2ClastName%2CworkEmail&onlyCurrent=true"
    res = requests.get(empl_uri,headers=headers)
    if res.status_code == 200:
        print(res.json())
        return res.json()
    else:
        print(res.status_code)
if response.status_code == 200:
    data = response.json()
    for i in data:
        emp_id = i['employeeId']
        # print(i)
        # print(emp_id)
        empl_data = get_employee_info(emp_id)
        employee_list.append({
            "id":i["id"],
            "name":i["name"],
            "email":empl_data["workEmail"],
            "start" : i["start"],
            "end": i["end"]
        })
        # print(empl_data)

print(employee_list)

