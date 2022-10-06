int sensorValue;
int outputValue;

void setup() {
  // put your setup code here, to run once:
  pinMode(A3,INPUT);
  pinMode(11,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(9,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  sensorValue=analogRead(A3);
  outputValue= map(sensorValue,0,1023,0,255);
  Serial.println(outputValue);
  

  char lecturaSerial = Serial.read();


  if (lecturaSerial=='H'){
    digitalWrite(11,HIGH);
    digitalWrite(10,LOW);
    digitalWrite(9,LOW);
    
    }
  else if (lecturaSerial=='N'){
    digitalWrite(11,LOW);
    digitalWrite(10,HIGH);
    digitalWrite(9,LOW);
    
    }
    else if (lecturaSerial=='F'){
    digitalWrite(11,LOW);
    digitalWrite(10,LOW);
    digitalWrite(9,HIGH);
    
    }

    delay(100);


}
