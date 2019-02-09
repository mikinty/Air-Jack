int trigPin = 11;
int echoPin = 12;
int stringPins[3] = {A0, A1, A2};

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  pinMode(echoPin, INPUT);
  int duration = pulseIn(echoPin, HIGH);
  int cm = (duration/2) / 29.1;
  Serial.print("cm: ");
  Serial.println(cm);

  int pValues[3];
  for(int i=0;i<3;i++) {
    pValues[i] = analogRead(stringPins[i]);
  }
  for(int i=0;i<3;i++) {
    //Serial.print("p meter 1: ");
    //Serial.println(pValues[i]);
  }
  delay(500);
  
}
