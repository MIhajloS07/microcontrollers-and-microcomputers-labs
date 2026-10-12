#include <DHT.h>
#include <SoftwareSerial.h>
#include <ESP8266WiFi.h>

#define DHTPIN 2      // DHT signal pin
#define DHTTYPE DHT11 // DHT 11 sensor type
DHT dht(DHTPIN, DHTTYPE);
SoftwareSerial espSerial(0, 1);              // RX, TX pins for ESP8266 communication
const char *ssid = "your_wifi_ssid";         // Replace with your WiFi SSID
const char *password = "your_wifi_password"; // Replace with your WiFi password
WiFiServer server(80);
void setup()
{
    Serial.begin(9600);
    WiFi.begin(ssid, password);
    Serial.print("Connecting to WiFi");
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\Connected!");
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
    dht.begin();
    server.begin();
}
void loop()
{
    WiFiClient client = server.available();
    if (!client)
        return;
    Serial.println("New client connected");
    while (!client.available())
        delay(1);
    float temp = dht.readTemperature();
    float hum = dht.readHumidity();
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println();
    client.println("<!DOCTYPE html>");
    client.println("<html>");
    client.println("<head><meta http-equiv='refresh' content='3'/>");

    client.println("<title>Arduino Web Sensor</title></head>");
    client.println("<body style='font-family:Arial; text-align:center;'>");
    client.println("<h1>Data from DHT Sensor</h1>");
    client.print("<p>Temperature: ");
    client.print(temp);
    client.println(" &deg;C</p>");
    client.print("<p>Humidity: ");
    client.print(hum);
    client.println(" %</p>");
    client.println("<p>(Page refreshes every 3 seconds)</p>");
    client.println("</body></html>");
    client.stop();
}