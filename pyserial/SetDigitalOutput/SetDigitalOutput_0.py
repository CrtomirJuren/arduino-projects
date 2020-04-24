# -*- coding: utf-8 -*-
"""
 
"""
import serial #for Serial communication
import time   #for time.sleep(1) delay functions
 
port = serial.Serial('com3',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

print ("Example: Python is blinking LED on Arduino")
num_blinks = input("Set number of blinks:")

# Use this line if you wait some initialize hello from arduino
#print arduino.readline() #read the serial data and print it as line

while True:

    #send value '1' to serial
    print(f'Starting to send data to Arduino in:')
    for sec in reversed(range(3)):
        print(f'{sec}')
        time.sleep(0.5) 

    for blink_times in range(int(num_blinks)):
        port.write(b'1')
        time.sleep(0.5) 
        port.write(b'0')
        time.sleep(0.5) 

    break #stop while loop        

    
