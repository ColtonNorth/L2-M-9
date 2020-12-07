import json
import threading
import requests
from End_to_EndDemotest1 import write_temp

write_temp()

KEY2 = "Q8WQRS84BFT21SCG"
def test_case():
      URL='https://api.thingspeak.com/channels/1226418/feeds.json?api_key='
      HEADER='&results=1'
      NEW_URL=URL+KEY2+HEADER
      get_data=requests.get(NEW_URL).json()
     #print(get_data)
      channel_id=get_data['channel']['id']

      field_1=get_data['feeds']
      field_2=get_data['feeds']
      field_3=get_data['feeds']
 
      t=[]
      h=[]
      p=[]
      for x in field_1:
         #print(x['field1'])
         t.append(x['field1'])
         print(t)         #Prints value in the field. Tests whether values are being uploaded to the ThinkSpeak channel.
         y = float(t[0])
         if(y==1.0):
            print("Server successfully recieving value. Feedback loop")

      for n in field_2:
          h.append(n['field2'])
          print(h)         #Prints value in the field. Tests whether values are being uploaded to the ThinkSpeak channel.
      for m in field_3:
          p.append(m['field3'])
          print(p)         #Prints value in the field. Tests whether values are being uploaded to the ThinkSpeak channel.
     
if __name__ == '__main__':
     #thingspeak_post()
     test_case()
 
