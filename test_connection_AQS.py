import json
import threading
import requests
from airqualityvals1 import write_airsensor

write_airsensor()

#Read API Key
KEY2 = "1CJF3RL8KTRYLFL9"

def test_connection():
    #URL to read from thingspeak channel
    URL= 'https://api.thingspeak.com/channels/1226517/feeds.json?api_key='

    #Header for new read URL
    HEADER = '&results=2'

    #New URL which will be read from
    NEW_URL=URL+KEY2+HEADER

    get_data=requests.get(NEW_URL).json()
    channel_id = get_data['channel']['id']

    #Fields to read data from
    #field1 represents carbon level values
    field_1 = get_data['feeds']

    #field2 represents nitrogen level values
    field_2 = get_data['feeds']

    #field3 represents voc level values
    field_3 = get_data['feeds']


    carbonLevelValue= []
    nitrogenLevelValue= []
    vocLevelValue= []

    #for each carbon value in the first feed of channel, print them and compare to thingspeak 
    for carbonValue in field_1:
        carbonLevelValue.append(carbonValue['field1'])
        print(carbonLevelValue)

    #for each nitrogen value in the second feed of channel, print them and compare to thingspeak 
    for nitrogenValue in field_2:
        nitrogenLevelValue.append(nitrogenValue['field2'])
        print(nitrogenLevelValue)
    
    #for each VOC value in the third feed of channel, print them and compare to thingspeak 
    for vocValue in field_3:
        vocLevelValue.append(vocValue['field3'])
        print(vocLevelValue)

if __name__ == '__main__':
    test_connection()