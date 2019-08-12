"""
Find the BLE address for a mambo.  To run this,

sudo python findMambo.py

Note that the sudo is necessary for BLE permissions on linux.  It is only needed on
this program and nothing else.

Author: Amy McGovern
"""
#This causes an error so just going into the code works, bypassing the exception handler
#try:
#    from bluepy.btle import Scanner, DefaultDelegate
#    BLEAvailable = True
#except:
#    BLEAvailable = False
from bluepy.btle import Scanner, DefaultDelegate
BLEAvailable = True

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)

def main():
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(10.0)

    for dev in devices:
        #print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
        for (adtype, desc, value) in dev.getScanData():
            #print "  %s = %s" % (desc, value)
            if (desc == "Complete Local Name"):
                if ("Mambo" in value):
                    print("FOUND A MAMBO!")
                    print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
                    print("  %s = %s" % (desc, value))

                elif ("Swing" in value):
                    print("FOUND A SWING!")
                    print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
                    print("  %s = %s" % (desc, value))


if __name__ == "__main__":
    main()
