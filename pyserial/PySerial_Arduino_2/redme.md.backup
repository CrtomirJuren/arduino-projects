# PYSERIAL 2

-	reject invalid user inputs
-	when arduino gets string value "1", send data to PC
-	arduino outputs data only when requested from PC
-	arduino is sending potentimoeter data every 200ms
-	python is reading data. no user inputs


## ARDUINO CODE
```
const int potentiometer_pin = A0;
int analog_data = 0;
char userInput;
  
void setup() {
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()>0){ //When Serial.available()<0, we didnt receive any bytes from python
    userInput = Serial.read();
    if(userInput == '1'){
      analog_data = analogRead(potentiometer_pin);
      //Serial.println("analog_data= ");
      Serial.println(analog_data);  // IMPORTANT delimiter, escape sequence for data is line feed = new line "\n"
    } //if user input "1"
  } //serial.available
} //void loop

```

## PYTHON CODE

```python
# -*- coding: utf-8 -*-
"""
  example for sending potentimeter value to PC over serial
  and testing python code
  
  CLOSE TO AUTOMATING ARDUINO SERIAL MONITOR
"""

import serial

port = serial.Serial(
        "COM3",
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

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


```