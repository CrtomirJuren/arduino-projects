/*
 * using uint8_t instead of bool. because it is used in different languages. bool variable isnt.
 */

// Pins
const uint8_t btn_pin = 6;
const uint8_t led_pin = 2;

// Globals
uint8_t led_state = LOW;
uint8_t btn_prev = HIGH;

void setup(){
  pinMode(btn_pin, INPUT);    //define pin as input-button
  pinMode(led_pin, OUTPUT);    //define pin as input-button
  Serial.begin(9600);    // opens serial port, sets data rate to 9600 bps
}

void loop(){
  uint8_t btn_state = digitalRead(btn_pin);
  //check if button was pressed. 
  //Check if RISING EDGE. Transition from 0V -> 5V on input pin
  if ((btn_state == HIGH)&&(btn_prev == LOW)){
    led_state = !led_state;
    digitalWrite(led_pin, led_state);  
  }
  btn_prev = btn_state; //save new button state

  // Pretend we are doing other stuff
  delay(500);
}

/*
void loop(){
  // send data only when you receive data:
  if (Serial.available() > 0){
  
    // read the incoming byte:
    serialData = Serial.read();
    if 
    //Serial.print("data_received");
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
 */
