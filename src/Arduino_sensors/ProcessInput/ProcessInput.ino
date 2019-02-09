const int NUM_POSITIONS = 5;
int stringPins[3] = {A0, A1, A2};
int cutoffs[7] = {42, 86, 123, 165, 229, 375, 1023}; // got by trial-error

int trigPin = 11;
int echoPin = 12;
long duration, cm;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
} 

void loop() {
  //https://randomnerdtutorials.com/complete-guide-for-ultrasonic-sensor-hc-sr04/
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
    for(int j=0;j<3;j++) {
      if(voltage<cutoffs[j]) {
        stringValues[i] = j+1; 
      }
    }
    
  }
  Serial.write('s');
  for(int i=0;i<3;i++) {
    Serial.write(stringValues[i]);
  }
  Serial.write('e');
  delay(200);
}
