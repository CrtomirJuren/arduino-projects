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
import time

#variables
numPoints = 10
dataList = [0]*numPoints
#create a log file .ods is open office document
dataFile = open('arduino_data_file.xlsx','w')

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

print("Example for transfering multiple data points")
print('0 = exit, 1=get arduino multiple data:\n')

#------------------------------------------------
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
    print("data list = ")
    print(dataList)

    print("data avg = ")
    dataAvg = sum(dataList)/numPoints
    print(dataAvg)

    dataFile.write(str(dataAvg)+'\n')

    #dataFile.write("\t")

    #check received data type of first element
    #print('dataList[0]:')
    #print(type(dataList[0]))

    return
'''
def closePort():
    port.flush()
    port.flushInput()
    port.flushOutput()
    port.close()
    print("Port COM3 is closed")
'''
while True:
    #userInput = input()
    userInput = input()

    if userInput == '1':
        #if user pressed 1 than go into for loop and collect data
        for i in range(0,numPoints):
            #get string data from arduino
            data = getValues()
            #convert string to numeric
            data = int(data)
            #store numeric data into list
            dataList[i] = data

        #print(dataList)
        printValues()

    if userInput == '0':
        print("Exiting the Program")
        dataFile.close()
        #closePort()
        break



