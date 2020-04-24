# -*- coding: utf-8 -*-
"""
 
"""
import serial #for Serial communication
import time   #for delay functions
 
port = serial.Serial('com3',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

# Use this line if you wait some initialize hello from arduino
#print arduino.readline() #read the serial data and print it as line

print ("Enter: '0' = LED OFF & '1' = LED ON & '2' = Exit")
 
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

    
