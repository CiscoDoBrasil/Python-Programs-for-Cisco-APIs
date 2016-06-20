#!/usr/bin/python
# -*- coding: cp1252 -*-
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import time
import csv
import os, sys
#
def sendme( customerNames, numberToDials ):
    url = "https://api.tropo.com/1.0/sessions"

    querystring = {"action":"create","token":"644f66556f70456f61584a6c786d4e75524b626c52617771774e75746f4b516645436b5567616952466a4b6f"}

    payload = "{\n  \"token\": \"644f66556f70456f61584a6c786d4e75524b626c52617771774e75746f4b516645436b5567616952466a4b6f\",\n  \"numberToDial\" : 5521993329936,\n  \"customerName\" : \" SE1540\",\n  \"msg\" :  \" Please enter the Substation Spark room for more details...\"\n}"
    headers = {
        'content-type': "application/json",
        'accept': "application/json",
        'accept-language': "application/json",
        'cache-control': "no-cache",
        'postman-token': "e7ad2f37-1394-a2f8-2b88-91b9f3c0a8c2"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)
#    print str
    return
#
with open('C:\Python27\smsusers.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    customerNames = []
    numberToDials = []
    count = 0
    for row in readCSV:
        count = count + 1
        customerName = row[0]
        print customerName
        numberToDial = row[1]
        print numberToDial
        customerNames.append(customerName)
        numberToDials.append(numberToDial)
    print count    
    csvfile.close()    
    numRows = 1
    
    while numRows < count:  
        # Aqui entra o código para mandar SMS
        sendme((customerNames[numRows]),(numberToDials[numRows]))
        numRows = numRows + 1
    

