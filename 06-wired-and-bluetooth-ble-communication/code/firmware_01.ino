#include <SoftwareSerial.h>

// Create a software serial port for Bluetooth communication
SoftwareSerial BT(10, 11); // RX, TX

void setup()
{
    Serial.begin(9600);
    BT.begin(9600);
    Serial.println("Bluetooth communication ready.");
}
void loop()
{
    if (BT.available())
    {
        char c = BT.read();
        Serial.write(c);
    }
    if (Serial.available())
    {
        char c = Serial.read();
        BT.write(c);
    }
}