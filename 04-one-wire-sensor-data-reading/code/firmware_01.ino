#include "DHT.h" // DHT library
#define DHTPIN 2
#define DHTTYPE DHT11
// #define DHTTYPE DHT22  // for DHT 22 (AM2302), AM2321
// #define DHTTYPE DHT21 // for DHT 21 (AM2301)
// Create an instance of the DHT sensor
DHT senzor(DHTPIN, DHTTYPE);
void setup()
{
    // Start the serial communication
    Serial.begin(9600);
    senzor.begin(); // Initialize the DHT sensor
}
void loop()
{
    // Wait a few seconds between measurements
    delay(2000);
    Serial.println("-------------------------");
    // readHumidity() method returns the humidity in percentage
    float humidity = senzor.readHumidity();
    // readTemperature() method returns the temperature in Celsius
    float temperature = senzor.readTemperature();
    // Check if any reads failed and exit early (to try again).
    // The isnan() function checks if the value is "Not a Number" (NaN), which indicates a failed reading.
    if (isnan(humidity) || isnan(temperature))
    {
        Serial.println("Error reading from DHT sensor!");
        return;
    }
    // Print the temperature and humidity values to the serial monitor
    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.print(" *C\n");
    // Print the humidity value to the serial monitor
    Serial.print("Humidity: ");
    Serial.print(humidity);
    Serial.print(" %\n");
}