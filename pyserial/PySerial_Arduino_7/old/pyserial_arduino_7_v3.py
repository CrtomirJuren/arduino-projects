# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:35:21 2020

@author: crtjur
"""

#imports
import serial
import serial.tools.list_ports
import time

#-----------variables-------------------------------
numPoints = 20
dataList = [0]*numPoints
dataFile = open('dataFile.txt','w')
numRowsCollect = 10
#--------------------------------------------------
def get_ports():
    #get a list of all active ports on PC
    ports = serial.tools.list_ports.comports()    
    
    #print(portData)
    print("total COM ports = " + str(len(ports))) #number of COM ports on computer

    #get name of single port print(portData[0]), print(portData[1])
    return ports
#--------------------------------------------------
def findArduino(portsFound):
    #initialize variables
    commPort='none'
    numConnections = len(portsFound)
    
    for i in range(0,numConnections):
        port = portsFound[i]
        strPort = str(port)
    
    if numConnections == 0:
        strPort = ""
    
    #search string in port names and split it
    """
    DEFAULT STRING NAME OF ARDUINO PORT
    COM3 - Arduino Uno
    we split by spaces
    list[]=[COM3,-,Arduino,Uno]
    list[0] = COM3
    """
    
    if 'Arduino' in strPort:
        splitPort = strPort.split(' ')
        commPort = (splitPort[0])
        print("Arduino found on " + str(splitPort[0]))
    else:
        print("Arduino not found")
    return commPort
#--------------------------------------------------

foundPorts = get_ports()
connectPort = findArduino(foundPorts)

try:
    port = serial.Serial(
        connectPort,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    port.isOpen() # try to open port, if possible print message and proceed with 'while True:'
    print ("port is opened!")

except IOError: # if port is already opened, close it and open it again and print message
  port.close()
  port.open()
  print ("port was already open, was closed and opened again!")
  
  
#--------------------------------------------------
def getValues():
    port.write(b'1')
    arduinoData = port.readline()#.decode.split('\r\n')
    
    return arduinoData[0]

def printToFile(data,index):
    dataFile.write(data)
    if index != (numPoints - 1): #last data point needs to end with new line
        dataFile.write(',') #comma separeted value list
    else:
        dataFile.write('\n') #last data point of list,doesnt need comma, it needs new line

def getAvarage(dataSet,row):
    dataAvg = sum(dataSet) / len(dataSet)
    print('Avarage for' + str(row) + 'is:' + str(dataAvg))


while True:
    
    userInput = input('Get data points?')
    
    if userInput == '1':
        for row in range(0,numRowsCollect):
            for i in range(0,numPoints):
                data = getValues()
                printToFile(data,i) #Pass function data point and current position
                dataInt = int(data)
                dataList[i] = dataInt
            
            #after one row of information is collected call avarage function
            getAvarage(dataList,row) #take avarage and print it to shell
            
        dataFile.close()
    
    break

