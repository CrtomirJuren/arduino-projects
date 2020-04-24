# PYSERIAL 1

-	pyserial python + arduino hello world 
-	OUTPUTS DATA ALL THE TIME, no logic involved
-	arduino is sending potentimoeter data every 200ms
-	python is reading data. no user inputs

## ARDUINO CODE
```

const int potentiometer_pin = A0;
int analog_data = 0;
  
void setup() {
  Serial.begin(9600);
}

void loop() {
  analog_data = analogRead(potentiometer_pin);
  Serial.println(analog_data);  // IMPORTANT delimiter, escape sequence for data is line feed = new line "\n"
  delay(200);
}
```

## PYTHON CODE

```python

import serial

device = serial.Serial("COM3", baudrate = 9600, timeout = 1)

while 1:
    #arduinoData = ser.readline() #RESULT = b'453\r\n'
    arduinoData = device.readline().decode('ascii') #RESULT = 453
    print(arduinoData)

device.close()
```