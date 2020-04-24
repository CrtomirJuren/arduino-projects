# -*- coding: utf-8 -*-
"""
  example for sending potentimeter value to PC over serial
  and testing python code
  
  USING PYTHON LIST
  WE COLLECT MULTIPLE POINTS
"""
#imports
import serial
import time

#variables
numPoints = 5
dataList = [0]*numPoints

#port initialization
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

print("Example for transfering multiple data points")
print("Port COM3 is open")
print('0 = exit, 1=get arduino multiple data:\n')


def getValue():
    port.write(b'1')
    #arduinoData = port.readline()                #RESULT = 453
    arduinoData = port.readline().decode('ascii') #RESULT = 453
    return arduinoData

def getValues():
    port.write(b'1')
    arduinoData = port.readline().decode().split('\r\n') #when it gets information from the bus. puts data into list
    #check arduino data
    return arduinoData[0]

def printValues():
    print("data = 1")
    print(dataList)
    
    #check received data type of first element
    print('dataList[0]:')
    print(type(dataList[0]))
    
    return

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
        #if user pressed 1 than go into for loop and collect data
        for i in range(0,numPoints):
            data = getValues()
            dataList[i] = data
        
        #print(dataList)
        printValues()
        
    if userInput == '0':
        print("Exiting the Program")
        closePort()
        break

