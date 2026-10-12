#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME680.h>
#include <LiquidCrystal_I2C.h>

// LCD address and dimensions
LiquidCrystal_I2C lcd(0x27, 16, 2);

// BME680 object
Adafruit_BME680 bme;

void setup()
{
    Serial.begin(9600);
    lcd.init();
    lcd.backlight();
    lcd.setCursor(0, 0);
    lcd.print("BME680 test");
    if (!bme.begin())
    {
        lcd.setCursor(0, 1);
        lcd.print("Error: BME680 not found!");
        Serial.println("Error: Could not find a valid BME680 sensor, check wiring!");
        while (1);
    }
    // Sensor configuration
    bme.setTemperatureOversampling(BME680_OS_8X);
    bme.setHumidityOversampling(BME680_OS_2X);
    bme.setPressureOversampling(BME680_OS_4X);
    bme.setIIRFilterSize(BME680_FILTER_SIZE_3);
    bme.setGasHeater(320, 150); // 320°C, 150 ms
    delay(2000);
    lcd.clear();
}
void loop()
{
    if (!bme.performReading())
    {
        Serial.println("Error performing reading!");
        return;
    }
    // Print to serial monitor
    Serial.print("T: ");
    Serial.print(bme.temperature);
    Serial.print(" *C, ");
    Serial.print("H: ");
    Serial.print(bme.humidity);
    Serial.print(" %, ");
    Serial.print("P: ");
    Serial.print(bme.pressure / 100.0);
    Serial.println(" hPa");
    // Print to LCD
    lcd.setCursor(0, 0);
    lcd.print("T:");
    lcd.print(bme.temperature, 1);
    lcd.print((char)223); // symbol of degree
    lcd.print("C ");
    lcd.print("H:");
    lcd.print(bme.humidity, 0);
    lcd.print("% ");
    lcd.setCursor(0, 1);
    lcd.print("P:");
    lcd.print(bme.pressure / 100.0, 1);
    lcd.print("hPa");
    delay(2000);
}