/*
 * serial_echo.pde
 * ----------------- 
 * Echoes what is sent back through the serial port.
 *
 * http://spacetinkerer.blogspot.com
 */

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
    Serial.println(serialData); //returns ASCII CODE. value 48 = ASCII FOR 0-zero 
                                //value 49 = ASCII FOR 1-one   
    if(serialData == '1'){
      digitalWrite(pin, HIGH);
    }
    else if(serialData == '0'){
      digitalWrite(pin, LOW);
    }
  }  
}
