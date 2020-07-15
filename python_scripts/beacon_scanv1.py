#!/usr/bin/python3

from bluepy.btle import Scanner, DefaultDelegate
from datetime import datetime
import re

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def HandleDiscovery(self,dev,new_dev,new_dat):
        if new_dev:
            pass
        if new_dat:
            pass
        
def convertRSSIStrToInt(rssi):
    return int(re.sub("[^0-9-]", "", rssi))

def rssiChange(prev,curr):
    return abs((abs(curRSSI) - abs(prevRSSI))) 

if __name__ == "__main__":
    prevRSSI=0
    dataLogger = open("/home/pi/logs/beacon_rssi.log","w",buffering=0) 
    scanner = Scanner().withDelegate(ScanDelegate())
    while 1:
        try:
            devices = scanner.scan(1)
    #        print("Amount of Devices = "+str(len(devices)))
            device=None
            for ii in devices:
                if ii.addr.encode('ascii','ignore') == '18:04:ed:ab:5b:04':
                    device=ii
                    print("Device Found")
                    break

            if device != None:
                curRSSI = device.rssi
                if curRSSI != prevRSSI and rssiChange(prevRSSI,curRSSI) > 0 :
                    times=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    logStr="{0}|RSSI={1},Diff={2}".format(times,device.rssi,rssiChange(prevRSSI,curRSSI))
                    print("\t"+logStr)
                    dataLogger.write(logStr+"\n")
                prevRSSI=curRSSI
            else:
                print("device not found")
                dataLogger.write("device not found\n")
        except Exception as e:
            print(e)
            dataLogger.write(e)
    dataLogger.close()


