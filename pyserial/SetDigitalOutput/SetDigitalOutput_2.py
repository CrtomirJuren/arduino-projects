# -*- coding: utf-8 -*-
"""
  example for sending potentimeter value to PC over serial
  and testing python code
  
  USING PYTHON LIST
  1.WE COLLECT MULTIPLE POINTS
  2.CREATE AVARAGE OF DATA
"""
#imports
import serial
import serial.tools.list_ports
import time

#variables


#---------------------SERIAL PORT FUNCTIONS-------------------------------
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

#---------SERIAL PORTS CONNECTION-----------------
'''
#port initialization
port = serial.Serial(
        "COM3",
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
'''
#---------------------SERIAL PORT SEARCH-------------------
foundPorts = get_ports()
connectPort = findArduino(foundPorts)
#----------------SERIAL PORT INITIALIZATION--------------
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

#after serial.serial arduino resets. we see this on arduino blinking L led
#we need to wait until arduino is ready
time.sleep(3) 

print("Example SetDigitalOutput on Arduino")
print('0 = turn led off, 1 = turn led on, 2 = exit python app:\n')

#------------------------------------------------
def printToFile(data,index):
    dataFile.write(data)
    if index != (numPoints - 1): #last data point needs to end with new line
        dataFile.write(',') #comma separeted value list
    else:
        dataFile.write('\n') #last data point of list,doesnt need comma, it needs new line

def getAvarage(dataSet,row):
    dataAvg = sum(dataSet) / len(dataSet)
    print('Avarage for ' + str(row) + ' is: ' + str(dataAvg))


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

while True:
    #userInput = input()
    userInput = input()

    #valid arduino data to change led only "0" or "1"
    if userInput == '0':
        print(f'sending string value of 0 to Arduino...')
        port.write(b'0')

    if userInput == '1' or userInput == '1':
        print(f'sending string value of 1 to Arduino...')
        port.write(b'1')

    if userInput == '2':
        port.write(b'0') #turn led off when exiting    
        print(f'exiting application...')
        break #stop while loop        

    
