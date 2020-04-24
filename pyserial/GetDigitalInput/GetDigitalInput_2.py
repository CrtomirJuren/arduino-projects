# -*- coding: utf-8 -*-
"""
    Example for receiving ardino pushbutton value
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

print("Port COM3 is open")
print('0 = exit:\n')

def getValue():
    port.write(b'1')
    arduinoData = port.readline() #RESULT = 453
    #arduinoData = port.readline().decode('ascii') #RESULT = 453
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
    
