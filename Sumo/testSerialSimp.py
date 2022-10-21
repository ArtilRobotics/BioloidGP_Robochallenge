import time, sys, serial
               
 ser = serial.Serial('/dev/ttyAMA0',57600, serial.EIGHTBITS, serial.PARITY_NONE ,serial.STOPBITS_ONE)
         
     ser.write('Hello\n')
     time.sleep(1)