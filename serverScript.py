import http.client
import urllib
from urllib import request
from urllib.request import urlopen
import requests
import json
import time
from time import sleep
import sqlite3
import smtplib

def read_data_thingspeak_temperature():
    URL = 'https://api.thingspeak.com/channels/1226418/fields/1.json?api_key=Q8WQRS84BFT21SCG&results1'
    KEY = 'Q8WQRS84BFT21SCG'
    HEADER = '&results=1'
    NEW_URL = URL+KEY+HEADER
    #print(NEW_URL)

    get_data = requests.get(NEW_URL).json()
    #print(get_data)

    temp = []
    for x in get_data['feeds']:
        print(x['field1'])
        temp.append(x['field1'])
    return float(temp[0])

def read_data_thingspeak_pressure():
    URL = 'https://api.thingspeak.com/channels/1226418/fields/3.json?api_key=Q8WQRS84BFT21SCG&results1'
    KEY = 'Q8WQRS84BFT21SCG'
    HEADER = '&results=1'
    NEW_URL = URL+KEY+HEADER
    #print(NEW_URL)

    get_data = requests.get(NEW_URL).json()
    #print(get_data)

    temp = []
    for x in get_data['feeds']:
        print(x['field3'])
        temp.append(x['field3'])
    return float(temp[0])

def read_data_thingspeak_humidity():
    URL = 'https://api.thingspeak.com/channels/1226418/fields/2.json?api_key=Q8WQRS84BFT21SCG&results1'
    KEY = 'Q8WQRS84BFT21SCG'
    HEADER = '&results=1'
    NEW_URL = URL+KEY+HEADER
    #print(NEW_URL)

    get_data = requests.get(NEW_URL).json()
    #print(get_data)

    temp = []
    for x in get_data['feeds']:
        print(x['field2'])
        temp.append(x['field2'])
    return float(temp[0])

def read_data_thingspeak_carbonDioxide():
    URL = 'https://api.thingspeak.com/channels/1226517/fields/1.json?api_key=1CJF3RL8KTRYLFL9&results1'
    KEY = '1CJF3RL8KTRYLFL9'
    HEADER = '&results=1'
    NEW_URL = URL+KEY+HEADER
    #print(NEW_URL)

    get_data = requests.get(NEW_URL).json()
    #print(get_data)

    temp = []
    for x in get_data['feeds']:
        print(x['field1'])
        temp.append(x['field1'])
    return float(temp[0])

def read_data_thingspeak_nitrogenDixoxide():
    URL = 'https://api.thingspeak.com/channels/1226517/fields/2.json?api_key=1CJF3RL8KTRYLFL9&results1'
    KEY = '1CJF3RL8KTRYLFL9'
    HEADER = '&results=1'
    NEW_URL = URL+KEY+HEADER
    #print(NEW_URL)

    get_data = requests.get(NEW_URL).json()
    #print(get_data)

    temp = []
    for x in get_data['feeds']:
        print(x['field2'])
        temp.append(x['field2'])
    return float(temp[0])

def read_data_thingspeak_VOC():
    URL = 'https://api.thingspeak.com/channels/1226517/fields/3.json?api_key=1CJF3RL8KTRYLFL9&results1'
    KEY = '1CJF3RL8KTRYLFL9'
    HEADER = '&results=1'
    NEW_URL = URL+KEY+HEADER
    #print(NEW_URL)

    get_data = requests.get(NEW_URL).json()
    #print(get_data)

    temp = []
    for x in get_data['feeds']:
        print(x['field3'])
        temp.append(x['field3'])
    return float(temp[0])

def get_new_email():
    URL = 'https://api.thingspeak.com/channels/1250054/fields/1.json?api_key=9LUVISPMRDQXBZAQ&results1'
    KEY = '9LUVISPMRDQXBZAQ'
    HEADER = '&results=1'
    NEW_URL = URL+KEY+HEADER
    #print(NEW_URL)

    get_data = requests.get(NEW_URL).json()

    temp = []
    for x in get_data['feeds']:
        print(x['field1'])
        temp.append(x['field1'])
    return temp[0]

if __name__ == '__main__':
    #Create mail server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("QualityFlowProject@gmail.com", "L2_M_9**")

    #connect to database file
    dbconnect = sqlite3.connect("database.db");

    #If we want to access columns by name we need to set
    dbconnect.row_factory = sqlite3.Row;
    #now we create a cursor to work with db
    cursor = dbconnect.cursor();


    while True:
        #See if there are any new emails and add to database
        mostRecentEmail = get_new_email()
        cursor.execute('''SELECT email FROM emails WHERE email=?''',(mostRecentEmail,))
        result = cursor.fetchone()
        if result:
            print('Email already exists in database')
        else:
            print('New email added')
            cursor.execute('''Insert INTO emails VALUES (?)''',(mostRecentEmail,))
            dbconnect.commit()

        #Gathering data from thingspeak
        print('Current Temperature: ')
        read_data_thingspeak_temperature()
        print('Current Humidity: ')
        read_data_thingspeak_humidity()
        print('Current Pressure')
        read_data_thingspeak_pressure()
        print('Current Carbon Dioxide level: ')
        read_data_thingspeak_carbonDioxide()
        print('Current Nitrogen Dioxide level: ')
        read_data_thingspeak_nitrogenDixoxide()
        print('Current VOC level: ')
        read_data_thingspeak_VOC()

        print('\n\n\nSetting values for comparison...')
        carbonDioxideLevel = read_data_thingspeak_carbonDioxide()
        nitrogenDioxideLevel = read_data_thingspeak_nitrogenDixoxide()
        VOCLevel = read_data_thingspeak_VOC()
        temperature = read_data_thingspeak_temperature()
        humidity = read_data_thingspeak_humidity()
        pressure = read_data_thingspeak_pressure()

        #Send 1 back to all data collectors since data has been read.
        print('Data collected from collectors, returning 1 to collectors')
        sendBack = 1
        key = "TO2CUQWI0J9YV7V2"
        params = urllib.parse.urlencode({'field1': sendBack,'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(alertBuzzer)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection closed")
        key = "UQ8UQVWT64WAQ7VW"
        params = urllib.parse.urlencode({'field1': sendBack,'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(alertBuzzer)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection closed")

        #Inserting values into database
        cursor.execute('''INSERT INTO vals VALUES(?, ?, ?, ?, ?, ?);''', (temperature, humidity, pressure, carbonDioxideLevel, nitrogenDioxideLevel, VOCLevel))
        dbconnect.commit();

        #If the carbonDioxide, nitrogenDioxide, or VOC functions return a value above the specified thresholds, notify the controller to activate buzzer (1 turns on, 0 turns off).
        if(carbonDioxideLevel > 2000 or nitrogenDioxideLevel > 100 or VOCLevel > 750):
            print('Air quality poor, alerting buzzer.')
            alertBuzzer = 1
            key = "P2ALDMI1Y8H2Y4JP"
            params = urllib.parse.urlencode({'field1': alertBuzzer,'key':key })
            headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
            conn = http.client.HTTPConnection("api.thingspeak.com:80")
            try:
                conn.request("POST", "/update", params, headers)
                response = conn.getresponse()
                print(alertBuzzer)
                print(response.status, response.reason)
                data = response.read()
                conn.close()
            except:
                print("connection closed")
            #Send emails to all emails in database
            cursor.execute('SELECT * FROM emails');
            print('Sending Emails to customers...')
            for row in cursor:
                #print(row['email']);
                server.sendmail("QualityFlowProject@gmail.com", row['email'],"The Quality Flow has detected poor air quality, please be cautious.")
            print('Emails sent')

        print('Sleeping 25 seconds...')
        sleep(25)
