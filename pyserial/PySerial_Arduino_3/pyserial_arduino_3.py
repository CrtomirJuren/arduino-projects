# -*- coding: utf-8 -*-
"""
  example for sending potentimeter value to PC over serial
  and testing python code
"""

import serial
import time

port = serial.Serial(
        "COM3",
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
#after serial.serial arduino resets. we see this on arduino blinking L led
#we need to wait until arduino is ready

time.sleep(3) 

print("Port COM3 is open")
print('0 = exit, 1=get arduino data:\n')

def getValue():
    port.write(b'1')
    arduinoData = port.readline().decode('ascii') #RESULT = 453
    return arduinoData

def closePort():
    port.flush()
    port.flushInput()
    port.flushOutput()
    port.close()
    print("Port COM3 is closed")

while True:
    #userInput = input()
    userInput = input()

    if userInput == '1':
        print(getValue())
        
    if userInput == '0':
        print("Exiting the Program")
        closePort()
        break
