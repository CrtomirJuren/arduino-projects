/*
  example for sending potentimeter value to PC over serial
  and testing python code
*/

// Pins
const uint8_t btn_pin = 6;
const uint8_t led_pin = 2;

// Globals
uint8_t led_state = LOW;
uint8_t btn_prev = HIGH;
uint8_t btn_state;

char userInput ;

void setup(){
  pinMode(btn_pin, INPUT);    //define pin as input-button
  pinMode(led_pin, OUTPUT);    //define pin as input-button

  Serial.begin(9600);    // opens serial port, sets data rate to 9600 bps
}

void loop(){
  
  //Check if RISING EDGE. Transition from 0V -> 5V on input pin
  btn_state = digitalRead(btn_pin); //check if button was pressed. 
  if ((btn_state == HIGH)&&(btn_prev == LOW)){
    led_state = !led_state;
    digitalWrite(led_pin, led_state);
    Serial.println(led_state);  // IMPORTANT delimiter, escape sequence for data is line feed = new line "\n"  
  }
  
  btn_prev = btn_state; //save new button state

  if(Serial.available()>0){ //When Serial.available()<0, we didnt receive any bytes from python
    userInput = Serial.read();
    if(userInput == '1'){

    } //if user input "1"
  } //serial.available
  //
  // Pretend we are doing other stuff
  delay(500);
}
