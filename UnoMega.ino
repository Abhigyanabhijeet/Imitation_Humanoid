/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo;
Servo myservo1;
Servo myservo2;
Servo myservo3;
Servo myservo4;
Servo myservo5;
Servo myservo6;
Servo myservo7;
Servo myservo8;
Servo myservo9;// create servo object to control a servo
// twelve servo objects can be created on most boards

  // variable to store the servo position

void setup() {
  Serial.begin(115200);
myservo.attach(3);//
myservo1.attach(5);
myservo2.attach(6);
myservo3.attach(9);

myservo4.attach(10);
myservo5.attach(11);
myservo6.attach(A0);
myservo7.attach(A1);

myservo8.attach(A2);
myservo9.attach(A3); // attaches the servo on pin 9 to the servo object
}

String data;

void loop() {
while (Serial.available() == 0); 
char x = Serial.read();

if(x!='a'&& x!='b'&& x!='c'&& x!='d'&& x!='e'&& x!='f'&& x!='g'&& x!='h'&& x!='i'&& x!='j')
{data +=x;}

if (x=='a'){
Serial.print("Servo1: "); 
Serial.println(data);
myservo.write(data.toInt()); 

data="";
}
else if (x=='b'){
Serial.print("Servo2: "); 
Serial.println(data);
myservo1.write(data.toInt());
  
data="";
}
//
else if (x=='c'){
Serial.print("Servo3: "); 
Serial.println(data);
myservo2.write(data.toInt()); 
data="";
}
//
else if (x=='d'){
Serial.print("Servo4: "); 
Serial.println(data);
myservo3.write(data.toInt()); 
data="";


}

else if (x=='e'){
Serial.print("Servo5: "); 
Serial.println(data);
myservo4.write(data.toInt()); 
data="";}

else if (x=='f'){
Serial.print("Servo6: "); 
Serial.println(data);
myservo5.write(data.toInt()); 
data="";

}
//
else if (x=='g'){
Serial.print("Servo7: "); 
Serial.println(data);
myservo6.write(data.toInt()); 
data="";
}
//
else if (x=='h'){
Serial.print("Servo8: "); 
Serial.println(data);
myservo7.write(data.toInt()); 
data="";


}

else if (x=='i'){
Serial.print("Servo9: "); 
Serial.println(data);
myservo8.write(data.toInt()); 
data="";


}
//
else if (x=='j'){
Serial.print("Servo10: "); 
Serial.println(data);
myservo9.write(data.toInt());


data="";
}
while(Serial.available()>0) Serial.read();
}

