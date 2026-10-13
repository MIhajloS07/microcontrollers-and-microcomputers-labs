import time
import board
import adafruit_dht
# Define the DHT11 sensors connected to GPIO pins
dht1 = adafruit_dht.DHT11(board.D4)
dht2 = adafruit_dht.DHT11(board.D17)
while True:
    try:
        # Read data from sensor 1
        t1 = dht1.temperature
        h1 = dht1.humidity
        # Read data from sensor 2
        t2 = dht2.temperature
        h2 = dht2.humidity
        # Print data to console
        print("Sensor 1 -> T:", t1, "H:", h1)
        print("Sensor 2 -> T:", t2, "H:", h2)
        print("---------------------")
        # Delay of 5 seconds before the next reading
        time.sleep(5)
        # Handle any runtime errors that may occur during sensor reading
    except RuntimeError:
        print("Error reading sensor data")
