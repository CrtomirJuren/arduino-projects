/*
  example for sending potentimeter value to PC over serial
  and testing python code
*/

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
