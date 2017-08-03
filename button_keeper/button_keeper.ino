/*
  DigitalReadSerial
 Reads a digital input on pin 2, prints the result to the serial monitor 
 
 This example code is in the public domain.
 */

// digital pin 2 has a pushbutton attached to it. Give it a name:
int pushButton = 2;
int led = 13;
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // make the pushbutton's pin an input:
  pinMode(pushButton, INPUT);
  pinMode(led, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input pin:
  int buttonState = digitalRead(pushButton);
  // print out the state of the button:
  
  
  for (int x = 0; x < 1000; x++) 
  {
      Serial.println("on");
      delay(1);        // delay in between reads for stability  
      digitalWrite(led, HIGH);
  }  
  
  for (int x = 0; x < 5000; x++) 
  {
      Serial.println("off");
      delay(1);        // delay in between reads for stability  
      digitalWrite(led, LOW);
  }
}



