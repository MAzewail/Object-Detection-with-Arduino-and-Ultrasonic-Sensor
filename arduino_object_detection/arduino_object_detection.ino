#include "model.h"
// this class will be different if you used another type of classifier, just check the model.h file
Eloquent::ML::Port::RandomForest classifier;

#include <Servo.h>

Servo myservo;
#define echo 13
#define trig 12
long dist=0,duration=0;


//void classify() {
//    float x_sample[] = { /* fill this vector with sample values */ };
//
//    Serial.print("Predicted class: ");
//    Serial.println(classifier.predict(x_sample));
//}

void setup() {
 pinMode(echo,0);
 pinMode(trig,1);
 Serial.begin(9600);
 myservo.attach(9);
// myservo.write(0);
}

//void us(uint8_t angel){
//   digitalWrite(trig,0);
// delayMicroseconds(2);
// digitalWrite(trig,1);
// delayMicroseconds(10);
// digitalWrite(trig,0);
// duration = pulseIn(echo,1);
// dist = duration * 0.0343/2 ;
// x_sample[angel] = (dist <40)?dist:0;
// Serial.println(String(x_sample[angel])+","+String(angel));
//// if (dist <40)x_sample[angel] = dist;
// 
//// Serial.println(String(dist)+","+String(angel));
//}

void loop() {
 float x_sample[180] = { /* fill this vector with sample values */ };
 for(uint8_t i =0; i<180; i++){
  myservo.write(i);
//  us(i);
   digitalWrite(trig,0);
 delayMicroseconds(2);
 digitalWrite(trig,1);
 delayMicroseconds(10);
 digitalWrite(trig,0);
 duration = pulseIn(echo,1);
 dist = duration * 0.0343/2 ;
 x_sample[i] = (dist <40)?dist:0;
 Serial.println(String(x_sample[i])+","+String(i));
  delay(20);
 }
    Serial.print("\nPredicted class: ");
    Serial.println(classifier.predict(x_sample));
  for(uint8_t i =180; i>0; i--){
  myservo.write(i);
//  us(i);
  delay(5);
 }
}
