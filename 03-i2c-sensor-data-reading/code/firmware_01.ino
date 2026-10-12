#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME680.h>

// Create an instance of the BME680 sensor
Adafruit_BME680 bme;

void setup()
{
    Serial.begin(9600);
    while (!Serial);
    Serial.println(F("BME680 test!"));
    if (!bme.begin())
    {
        Serial.println("Error: Could not find a valid BME680 sensor, check wiring!");
        while (1);
    }
    // Sensor configuration
    bme.setTemperatureOversampling(BME680_OS_8X);
    bme.setHumidityOversampling(BME680_OS_2X);
    bme.setPressureOversampling(BME680_OS_4X);
    bme.setIIRFilterSize(BME680_FILTER_SIZE_3);
    bme.setGasHeater(320, 150); // 320°C 150 ms
}
void loop()
{
    if (!bme.performReading())
    {
        Serial.println("Error performing reading!");
        return;
    }
    // Print the sensor readings to the Serial Monitor
    Serial.print("Temperature = ");
    Serial.print(bme.temperature);
    Serial.println(" *C");
    Serial.print("Pressure = ");
    Serial.print(bme.pressure / 100.0);
    Serial.println(" hPa");
    Serial.print("Humidity = ");
    Serial.print(bme.humidity);
    Serial.println(" %");
    Serial.print("Gas resistance = ");
    Serial.print(bme.gas_resistance / 1000.0);
    Serial.println(" KOhms");
    Serial.println();
    delay(2000);
}