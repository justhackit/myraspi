import os
import time
import requests
from datetime import datetime

def pushNotify(title,msg):
        r = requests.post("https://api.pushover.net/1/messages.json", data = {
        "token": "age....hmq",
        "user": "uxp...o9rb",
        "title":title,
        "message": msg
        })
        print(str(r.content) + " at " +str(datetime.now()))


def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

max_temp_sofar=40.0
while True:
        temp = float(measure_temp()[0:4])
        if temp > max_temp_sofar or temp > 65:
            pushNotify("ajsraspi","Max CPU temperature observed : {0} C".format(temp))
            max_temp_sofar=temp
        time.sleep(300)