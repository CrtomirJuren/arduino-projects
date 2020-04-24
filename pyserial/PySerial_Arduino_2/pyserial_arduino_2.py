# -*- coding: utf-8 -*-
"""
  example for sending potentimeter value to PC over serial
  and testing python code
  
  CLOSE TO AUTOMATING ARDUINO SERIAL MONITOR
"""

import serial

#device = serial.Serial("COM3", baudrate = 9600, timeout = 1)

port = serial.Serial(
        "COM3",
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
#port.open()
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
"""
while 1:
    
    userInput = input('Get data points?')
    
    if userInput == '1':
        print(arduinoData)
"""
while True:
    #userInput = input()
    userInput = input()

    if userInput == '1':
        print(getValue())
        
    if userInput == '0':
        print("Exiting the Program")
        closePort()
        break
    
#port.flush()
#port.flushInput()
#port.flushOutput()
#port.close()