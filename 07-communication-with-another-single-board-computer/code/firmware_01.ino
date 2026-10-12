// -- Firmware for Arduino to communicate with another single-board computer
// This firmware listens for commands from the single-board computer and controls an LED on pin 13
void setup()
{
    Serial.begin(9600);
    pinMode(13, OUTPUT);
}
void loop()
{
    // Send a heartbeat message every second
    Serial.println("ARDUINO_OK");
    delay(1000);
    // Reading commands
    if (Serial.available())
    {
        String cmd = Serial.readStringUntil('\n');
        cmd.trim();
        if (cmd == "LED ON")
        {
            digitalWrite(13, HIGH);
            Serial.println("ACK: LED ON");
        }
        else if (cmd == "LED OFF")
        {
            digitalWrite(13, LOW);
            Serial.println("ACK: LED OFF");
        }
        else if (cmd == "STATUS?")
        {
            Serial.println("STATUS: LED=" + String(digitalRead(13)));
        }
        else
        {
            Serial.println("ERR: Unknown CMD");
        }
    }
}