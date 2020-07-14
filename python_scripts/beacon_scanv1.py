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

if __name__ == "__main__":
    prevRSSI=""
    dataLogger = open("/home/pi/logs/beacon_rssi.log","w",buffering=0) 
    scanner = Scanner().withDelegate(ScanDelegate())
    while 1:
        try:
            devices = scanner.scan(0.5)
    #        print("Amount of Devices = "+str(len(devices)))
            for ii in devices:
                #print("\t\t\tTesting "+ ii.addr)
                if ii.addr.encode('ascii','ignore') == '18:04:ed:ab:5b:04':
                    curRSSI = convertRSSIStrToInt(ii.rssi)
                    if curRSSI != prevRSSI and abs((abs(curRSSI) - abs(prevRSSI))) > 2 :
                        times=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        logStr="{0}:RSSI={1} dB".format(times,ii.rssi)
                        print(logStr)
                        dataLogger.write(logStr)
                        dataLogger.flush()
                    prevRSSI=curRSSI
        except :
            continue
        finally:
            dataLogger.close()


