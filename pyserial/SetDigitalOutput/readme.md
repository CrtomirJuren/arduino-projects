# SetDigitalOutput

## Python operation
- waits on user input in cmd
- has three user inputs in cmd
("Enter: '0' = LED OFF & '1' = LED ON & '2' = Exit")
- messages for arduino '0' = LED OFF & '1' = LED ON & '2'

## Arduino operation
- receives and sets digital output to TRUE, FALSE

## ARDUINO CODE
```c
int serialData;    // for incoming serial data
int pin = 2;

void setup() {
  pinMode(pin, OUTPUT);
  Serial.begin(9600);    // opens serial port, sets data rate to 9600 bps
}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
  
    // read the incoming byte:
    serialData = Serial.read();
    Serial.print("received");
    Serial.println(serialData); 
    //returns ASCII CODE. value 48 = ASCII FOR zero 
    //value 49 = ASCII FOR 1-one
    if(serialData == '1'){
      digitalWrite(pin, HIGH);
    }
    else if(serialData == '0'){
      digitalWrite(pin, LOW);
    }
  }  
}
```

## PYTHON CODE

```python
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

```