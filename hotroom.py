#!/usr/bin/env python3

import phant
import time
import serial

# set up serial interface
s = serial.Serial('/dev/ttyUSB1', timeout=1)

# Set up date feed
p = phant.Phant('LQVlgNnAYgcqrljogEzp', 'temp', 'localtime', private_key="I'm not that stupid.")

while True:

    # Get temp
    s.write(bytearray("x",'ascii')) #send a character to start sampling
    temp = str(s.readline(), 'ascii').strip()
    print ('Temp: ' + temp)

    # Get time
    ltime = time.strftime("%Y-%m-%d %H:%M:%S")

    p.log(temp, ltime)
    #print(p.remaining_bytes, p.cap)
    #data = p.get()
    #print('Submitted: ')
    #print(data)
    time.sleep(30)


