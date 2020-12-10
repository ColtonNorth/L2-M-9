from random import randint
import http.client
import urllib.request
from time import sleep
key = "UQ8UQVWT64WAQ7VW"  # My API Key.
def write_airsensor():
    while True:
        sleep(15)
        #Carbon, nitrogen, and voc level values initiated with values above threshold 
        carbonLevels = 2001
        nitrogenLevels = 101
        vocLevels = 755

        #parameters for fields encoded, carbon level assigned with field 1, nitrogen level assigned with field 2, voc level assigned with field3
        params = urllib.parse.urlencode({'field1': carbonLevels, 'field2': nitrogenLevels, 'field3': vocLevels,'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            #print carbon, nitrogen and voc level values
            print (carbonLevels)
            print (nitrogenLevels)
            print (vocLevels)
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break
#main function to run execution
if __name__ == "__main__":
        while True:
                #run script 
                write_airsensor()