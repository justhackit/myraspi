from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
        def __init__(self):
                DefaultDelegate.__init__(self) 
        def handleDiscovery(self,dev,isNewDev,isNewData):
                if isNewDev:
                        print("Discovered Device" + dev.addr)
                elif isNewData:
                        print ("Recieved New Data from" + dev.addr)

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)

for dev in devices:
        print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        for (adtype, desc, value) in dev.getScanData():
            print("{0}={1}".format(desc,value))