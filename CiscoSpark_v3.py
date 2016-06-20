#!/usr/bin/env python
import subprocess
import argparse
#import requests
from subprocess import call
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


parser = argparse.ArgumentParser()
parser.add_argument("t")
parser.add_argument("h")
args = parser.parse_args()

# => This is where the file with the sensor location is
file = open('/root/SensorLocation.txt', 'r+')
SensorLocation = file.read()
file.close()
# =<

str1 = """{\r\n  \"roomId\": \"Y2lzY29zcGFyazovL3VzL1JPT00vZDhiNjk3MDAtZjM3Yi0xMWU1LWJiMDctYjFhZjQ4ZGRhMzYy\","""
filename = """\"file\": \"http://www.ti.com/lsds/sites/ti/analog/sensors/images/icon-temperature.png","""
str2 = """\"text\": \"EnvMon Alert ("""""
str2a = """) Fora do Padrao => """
str3 = "Temp: " + args.t + "c" + " Humi: " + args.h + "%"
str4 = """\"\r\n}"""
#
url = "https://api.ciscospark.com/v1/messages"

stringa = str1 + filename + str2 + SensorLocation + str2a  + str3 + str4

payload = stringa
# print payload

headers = {
   'authorization': "Bearer ZjdmZjYzMDgtMjMxNC00NTYwLTlmNWEtZDE3MTE3ZWI0OWU1YTVjNmY1NmYtMmJl",
   'content-type': "application/json",
   'cache-control': "no-cache",
   'postman-token': "3cd027f8-9c39-13c1-dc6a-4c8f251e9735"
          }
response = requests.request("POST", url, data=payload, headers=headers)
subprocess.call(" python CiscoTropoSendSMS.py", shell=True)
# call(["./python", "CiscoTropoSendSMS.py"])
