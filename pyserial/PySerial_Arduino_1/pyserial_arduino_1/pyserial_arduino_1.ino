/*
  example for sending potentimeter value to PC over serial
  and testing python code
*/

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
