int trigPin = 11;
int echoPin = 12;
int cutoffs[7] = {42, 86, 123, 165, 229, 375, 1023};
void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  pinMode(echoPin, INPUT);
  int duration = pulseIn(echoPin, HIGH);
  int cm = (duration/2) / 29.1;
  if(cm > 10) {
    //far enough away that we don't count as a strum
    return;
  }
  int voltage = analogRead(A0);
  if(voltage==0) {
    return;
  }
  for(int i=0;i<7;i++) {
    if(voltage<cutoffs[i]) {
      Serial.println(i);
      break;
    }
  }
  delay(200);
}
