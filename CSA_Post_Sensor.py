import requests
import time

url = "http://10.97.15.141:8765/"

temperature = str(30)
humidity = str(40)
alarmStatus = str(True)

payload = "{\r\n \"node\": {\r\n \"id\": \"id1\",\r\n \"sensors\": {\r\n \"temperature\": " + temperature +  ",\r\n \"humidity\": " + humidity + "\r\n },\r\n \"actuators\": {\r\n  \"alarm\": " + alarmStatus + "\r\n  }\r\n }\r\n}\r\n"

print payload

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "87123044-5a61-a573-45f8-3d7652b0398b"
    }

try:
    response = requests.request("POST", url, data=payload, headers=headers)
    returnCode = str(response.status_code)
    if returnCode == '200':
        print ("CSA Post Return Code: ") + returnCode + " OK"

except:
    print ("CSA Post Return Code: ") + returnCode + " Not OK"
