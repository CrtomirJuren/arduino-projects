/*
  example for sending potentimeter value to PC over serial
  and testing python code

  COLLECT MULTIPLE POINTS
*/

char received_data[]="";
  
void setup() {
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()>0){ //When Serial.available()<0, we didnt receive any bytes from python
    received_data = Serial.read();
   
      Serial.println(received_data);  //echo

  } //serial.available
} //void loop
