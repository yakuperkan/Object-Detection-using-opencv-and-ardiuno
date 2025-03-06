//#include <LiquidCrystal.h>
#include <Servo.h>

//LiquidCrystal lcd(6, 7, 5, 4, 3, 2);
Servo servoX, servoY;

void setup() {
  Serial.begin(115200);       // Start serial communicaiton
  servoX.attach(9);          // X axis servo
  servoY.attach(11);          // Y axis servo
//  lcd.begin(16, 2);           // Start LCD screen
 // lcd.clear();
}

void loop() {
  // İf data comes from serial communucation
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n'); // Veriyi oku
    input.trim(); // Clean the empty lines 

    // Seperate data as a x and y axis
    int commaIndex = input.indexOf(',');
    if (commaIndex > 0) {
      String x_str = input.substring(0, commaIndex);
      String y_str = input.substring(commaIndex + 1);

      // Convert datas string to integer
      int x = x_str.toInt();
      int y = y_str.toInt();

      // Scale coordinates
      int servoX_pos = map(x, 0, 640, 0, 180);
      int servoY_pos = map(y, 0, 480, 0, 180);

      // Run servomotors
      servoX.write(servoX_pos);
      servoY.write(servoY_pos);

     

      // Send feedback
      Serial.print("X: ");
      Serial.print(x);
      Serial.print(", Y: ");
      Serial.println(y);
    } else {
      Serial.println("İnvalid format. 'x,y' use.");
    }

     // Show coordinates on LCD screen
      /*lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("X:");
      lcd.print(x);
      lcd.setCursor(8, 0);
      lcd.print("Y:");
      lcd.print(y);*/
    
  }
}
