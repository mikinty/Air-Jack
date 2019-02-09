const int NUM_POSITIONS = 5;
int stringPins[3] = {A0, A1, A2};
int cutoffs[3][8] = {{55, 109, 148, 178, 233, 335, 545, 1023},
                    {61, 90, 110, 147, 206, 336, 607, 1023},
                    {118, 137, 157, 186, 238, 344, 609, 1023}}; // got by trial-error

int trigPin = 11;
int echoPin = 12;
long duration, cm;
int buttonPin = D4;
int tempoPin = A4;


void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buttonPin, INPUT);
  pinMode(tempoPin, INPUT);
} 

void loop() {
  //https://randomnerdtutorials.com/complete-guide-for-ultrasonic-sensor-hc-sr04/
  if(digitalRead(buttonPin) == LOW) {
    Serial.write('a');
    int voltage = analogRead(tempoPin);
    if(voltage>500)
      voltage = 500;
    int v = map(voltage, 0, 500, 8, 16);
    Serial.write(v + 48);
    Serial.write('b');
    Serial.println();
    delay(100);
  }
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
  cm = (duration/2) / 29.1;
  if(cm > 10) {
    //far enough away that we don't count as a strum
    return;
  }
  int stringValues[3];
  for(int i=0;i<3;i++) {
    int voltage = analogRead(stringPins[i]);
    if(voltage==0) {
      stringValues[i] = 0;
      continue;
    }
    for(int j=0;j<8;j++) {
      if(voltage<cutoffs[i][j]) {
        stringValues[i] = j+1; 
        break;
      }
    }
    
  }
  Serial.write('s');
  for(int i=0;i<3;i++) {
    Serial.write(stringValues[i]+48);
  }
  Serial.write('e');
  delay(200);
}
