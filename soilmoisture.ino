const int soilPin = A2; 

int sensorValue = 0;

void setup()
{
  Serial.begin(9600);  
}
void loop()                    
{
 sensorValue = analogRead(soilPin);  
 Serial.println(sensorValue);                     
 delay(1000);                                                                        
}
