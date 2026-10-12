#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

// BLE server and characteristic
BLECharacteristic *pCharacteristic;
bool deviceConnected = false;

// Callback class to handle BLE server events
class MyServerCallbacks : public BLEServerCallbacks
{
    // Called when a device connects to the BLE server
    void onConnect(BLEServer *pServer) { deviceConnected = true; };
    // Called when a device disconnects from the BLE server
    void onDisconnect(BLEServer *pServer) { deviceConnected = false; }
};

void setup()
{
    // BLEDevice initialization
    BLEDevice::init("ESP32_BLE");
    // Create a BLE server and set the callback for connection events
    BLEServer *pServer = BLEDevice::createServer();
    pServer->setCallbacks(new MyServerCallbacks());
    // Create a BLE service and characteristic for battery level
    BLEService *pService = pServer->createService(BLEUUID((uint16_t)0x180F)); // Battery Service
    // Create a characteristic for battery level with read and notify properties
    pCharacteristic = pService->createCharacteristic(
        BLEUUID((uint16_t)0x2A19),
        BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_NOTIFY);
    pCharacteristic->addDescriptor(new BLE2902());
    // Start the BLE service and advertising
    pService->start();
    pServer->getAdvertising()->start();
}
void loop()
{
    // If a device is connected, send a random battery level value every 2 seconds
    if (deviceConnected)
    {
        uint8_t level = random(0, 100);
        pCharacteristic->setValue(&level, 1);
        pCharacteristic->notify();
        delay(2000);
    }
}