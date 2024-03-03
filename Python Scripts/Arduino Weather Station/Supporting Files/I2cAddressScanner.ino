#include <Wire.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("Scanning I2C devices...");
  Wire.begin();

  for (byte i = 8; i < 127; i++) {
    Wire.beginTransmission(i);
    if (Wire.endTransmission() == 0) {
      Serial.print("Found device at address 0x");
      if (i < 16) Serial.print("0");
      Serial.println(i, HEX);
    }
  }
}

void loop() {}
