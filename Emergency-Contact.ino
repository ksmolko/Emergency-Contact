const int TEMPERATURE_THRESHOLD = 500;
const char EMERGENCY = '1';

void setup(){
  Serial.begin(9600);
  pinMode(A0, INPUT);
}

void loop(){
  int temperature = analogRead(A0);
  Serial.println(temperature);
  delay(3000);
  if(temperature > TEMPERATURE_THRESHOLD){
    //Serial.write(EMERGENCY);
  }
}

