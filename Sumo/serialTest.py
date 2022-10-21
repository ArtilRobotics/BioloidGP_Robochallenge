import time, sys, serial

#GBController = serial.Serial('/dev/tty.usbserial-A5052PWK',57600, serial.EIGHTBITS, serial.PARITY_NONE ,serial.STOPBITS_ONE)
GBController = serial.Serial('/dev/ttyUSB0',57600, serial.EIGHTBITS, serial.PARITY_NONE ,serial.STOPBITS_ONE)

def sendPacket(dato):
    a = dato
    b = 255-dato
    intlist = [255, 85, a, b, 0, 255]
    bytelist = bytes(intlist)   
    print(bytelist)
    GBController.write(bytelist)
    time.sleep(0.030303030303030303) 


sendPacket(2) # 2 ENCENDER LED
time.sleep(2)
sendPacket(1) # 1 APAGAR LED

GBController.close()