#include "SdsDustSensor.h"

int rxPin = 0;
int txPin = 1;

SdsDustSensor sds(rxPin, txPin);

void setup()
{
    Serial.begin(9600);
    sds.begin();

    Serial.println(sds.queryFirmwareVersion().toString());   // Prints the firmware version
    Serial.println(sds.setActiveReportingMode().toString()); // Sets the sensor to active reporting mode
    Serial.println(sds.setContinuousWorkingPeriod().toString());
}

void loop()
{
    PmResult pm = sds.readPm();

    if (pm.isOk())
    {
        Serial.print("PM2.5 = ");
        Serial.print(pm.pm25);
        Serial.print(", PM10 = ");
        Serial.println(pm.pm10);

        // If you only want to print the measured values, you can use the toString() method
        Serial.println(pm.toString());
    }
    else
    {
        // The loop delay is set to 0.5 seconds
        Serial.print("Unable to read sensor values. Reason: ");
        Serial.println(pm.statusToString());
    }

    delay(500);
}